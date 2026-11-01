#!/usr/bin/env python3
"""Refresh or check the current icon inventory embedded in hero rules.md files.

Usage:
    python3 scripts/rules_metadata.py Heroes/Janeway/rules.md
    python3 scripts/rules_metadata.py --check Heroes/Janeway/rules.md

The JSON metadata is an HTML comment so it does not render as game rules.
It contains current data only. Refresh replaces the previous block in place.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET

MARKER = "stdt-icon-inventory:v1"
BLOCK = re.compile(r"\n<!-- " + re.escape(MARKER) + r"\n(.*?)\n-->\n?\Z", re.S)
SECTIONS = {
    "LEAFLET": "leaflet", "HERO BOARD": "hero_board", "CARDS": "cards",
    "HERO ACTION CARDS": "cards", "UPGRADE CARDS": "cards",
}
VOID = {"img", "br", "hr", "meta", "link", "input", "source", "wbr"}


def split_metadata(text: str) -> tuple[str, dict | None]:
    matches = list(BLOCK.finditer(text))
    if not matches:
        if "<!-- " + MARKER in text:
            raise ValueError("Malformed or misplaced icon-inventory metadata")
        return text, None
    match = matches[0]
    body = text[:match.start()]
    if "<!-- " + MARKER in body:
        raise ValueError("Duplicate icon-inventory metadata")
    return body, json.loads(match.group(1))


class RulesIcons(HTMLParser):
    """Read gameplay icons only, excluding titles, cost badges and prose notes."""
    def __init__(self) -> None:
        super().__init__()
        self.section: str | None = None
        self.entries: list[dict] = []
        self.stack: list[dict] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs = dict(attrs)
        frame = dict(self.stack[-1]) if self.stack else {"entry": None, "rules": False, "icon": None}
        frame["tag"] = tag
        if attrs.get("data-rule"):
            entry = {"section": self.section, "name": attrs["data-rule"], "status": "written", "icons": []}
            if self.section is None:
                raise ValueError("Rule entry outside a recognized rules section")
            self.entries.append(entry)
            frame.update(entry=entry, rules=False, icon=None)
        if "data-source-line" in attrs:
            frame["rules"] = attrs["data-source-line"] == "rules"
        if attrs.get("data-icon") and frame["entry"] is not None and frame["rules"]:
            value = attrs.get("data-value")
            if value is not None:
                value = int(value) if re.fullmatch(r"\d+", value) else value
            icon = {"file": attrs["data-icon"], "number": value, "path": None}
            frame["entry"]["icons"].append(icon)
            frame["icon"] = icon
        if tag == "img" and frame["icon"] is not None:
            frame["icon"]["path"] = attrs.get("src")
        if tag == "b" and frame["rules"] and frame["icon"] is not None:
            frame["number_text"] = ""
        if tag not in VOID:
            self.stack.append(frame)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag: str) -> None:
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index]["tag"] == tag:
                frame = self.stack[index]
                if "number_text" in frame and frame["number_text"].strip() != str(frame["icon"]["number"]):
                    raise ValueError("Displayed icon numeral disagrees with data-value; update both together")
                del self.stack[index:]
                break


    def handle_data(self, data: str) -> None:
        for frame in reversed(self.stack):
            if "number_text" in frame:
                frame["number_text"] += data
                break


def plain_entries(body: str) -> list[dict]:
    """Keep unfinished plain-Markdown slots explicit, without inferred icons."""
    entries: list[dict] = []
    section = None
    current = None
    for line in body.splitlines():
        if line.startswith("## "):
            section = SECTIONS.get(line[3:].strip())
            current = None
        elif line.startswith("### ") and section:
            current = {"section": section, "name": line[4:].strip(), "status": "written", "icons": []}
            entries.append(current)
        elif current is not None and "TBD" in line:
            current["status"] = "placeholder"
    return entries


def leaflet_observation(path: Path) -> dict:
    """Count saved legend images separately from gameplay rules references."""
    leaflet = path.parent / "leaflet.svg"
    if not leaflet.is_file():
        return {"file": "leaflet.svg", "status": "not_present"}
    root = ET.parse(leaflet).getroot()
    legend = next((e for e in root.iter() if e.get("id") == "die-reference-legend"), None)
    if legend is None:
        return {"file": "leaflet.svg", "status": "no_die_reference_legend"}
    # Images are the displayed dependencies in the current legend. Do not count
    # both an image and its surrounding SVG's obsolete import annotations.
    images = [e for e in legend.iter() if e.tag.rsplit("}", 1)[-1] == "image"]
    counts = Counter(e.get("href") or e.get("{http://www.w3.org/1999/xlink}href") for e in images)
    if not images:
        raise ValueError(f"{leaflet}: legend has no supported image references; inspect before inventorying")
    for reference in counts:
        if not reference or not (leaflet.parent / reference).is_file():
            raise ValueError(f"{leaflet}: missing legend dependency {reference}")
    return {
        "file": "leaflet.svg", "status": "observed", "scope": "die_reference_legend",
        "sha256": hashlib.sha256(leaflet.read_bytes()).hexdigest(),
        "icons": [{"path": ref, "instances": count} for ref, count in sorted(counts.items())],
    }


def build_inventory(path: Path, body: str) -> dict:
    parser = RulesIcons()
    for line in body.splitlines(keepends=True):
        if line.startswith("## "):
            parser.section = SECTIONS.get(line[3:].strip())
        parser.feed(line)
    entries = parser.entries or plain_entries(body)
    lookup: dict[str, list] = defaultdict(list)
    references: Counter = Counter()
    for entry in entries:
        counts: Counter = Counter()
        for icon in entry["icons"]:
            if not icon["path"] or not (path.parent / icon["path"]).is_file():
                raise ValueError(f"{path}: missing icon dependency {icon['path']}")
            if Path(icon["path"]).name != icon["file"]:
                raise ValueError(f"{path}: icon identifier and displayed image disagree: {icon}")
            counts[(icon["file"], icon["number"], icon["path"])] += 1
        entry["icons"] = []
        for (file, number, source), count in sorted(counts.items(), key=lambda item: (item[0][0], str(item[0][1]), item[0][2])):
            entry["icons"].append({"file": file, "path": source, "number": number, "references": count})
            lookup[file].append({"section": entry["section"], "entry": entry["name"], "number": number, "references": count})
            references[entry["section"]] += count
    status = "current" if any(e["status"] == "written" for e in entries) else "placeholders" if entries else "awaiting_rules"
    return {
        "schema_version": 1,
        "status": status,
        "source": "rules.md",
        "content_sha256": hashlib.sha256(body.encode("utf-8")).hexdigest(),
        "counting": {
            "scope": "explicit gameplay icon references in rendered rules blocks",
            "excludes": ["CP cost/timing metadata", "titles", "design notes and brainstorming", "shared Standard Cards", "artwork-only icons"],
            "number": "explicit data-value, or null for an unnumbered reference; excludes intrinsic die labels",
            "references": "occurrences, not quantities of tokens gained, dice rolled, or damage dealt",
            "asset_observations": "separate saved-artwork instances; never added to rules reference totals",
        },
        "coverage": {section: {"entries": sum(e["section"] == section for e in entries), "references": references[section]} for section in ["leaflet", "hero_board", "cards"]},
        "total_rules_references": sum(references.values()),
        "entries": entries,
        "usage_by_icon": dict(sorted(lookup.items())),
        "asset_observations": [leaflet_observation(path)],
    }


def refresh(path: Path, check: bool = False) -> dict:
    body, existing = split_metadata(path.read_text(encoding="utf-8"))
    current = build_inventory(path, body)
    if check:
        if existing != current:
            raise ValueError(f"{path}: missing or stale icon inventory; run scripts/rules_metadata.py on this file")
    else:
        payload = json.dumps(current, indent=2, ensure_ascii=False).replace("-->", "--\\u003e")
        path.write_text(body + "\n<!-- " + MARKER + "\n" + payload + "\n-->\n", encoding="utf-8")
    return current


def load_icon_inventory(path: Path) -> dict:
    """Fail closed on stale metadata rather than applying an outdated allowlist."""
    return refresh(path, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    for path in args.paths:
        try:
            inventory = refresh(path, args.check)
        except (ValueError, ET.ParseError, OSError) as error:
            parser.exit(1, str(error) + "\n")
        print(f"{path}: {'verified' if args.check else 'updated'} current icon inventory ({inventory['total_rules_references']} rules references)")


if __name__ == "__main__":
    main()
