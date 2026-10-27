#!/usr/bin/env python3
"""Apply approved Tuvok/Janeway die-face colors and sync embedded SVG copies.

The icon inventory's Update lookup table is the allowlist for die-face icon
types. Only the active hero's hero_board.svg and cards/*.svg that embed one of
those listed icons are updated. The script is idempotent.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PALETTES = {
    "Tuvok": {
        "background_old": "#B3263A",
        "background": "#55286F",
        "border_old": "#FF0000",
        "border": "#FF00FF",
        "skin_old": "#4B2B21",
        "skin_alt_old": "#4C2D20",
        "skin": "#A95F32",
        "idic_red_old": "#B3263A",
    },
    "Janeway": {
        "background_old": "#084064",
        "background": "#003085",
        "border_old": "#086480",
        "border": "#00BFFF",
    },
}


def inventory_die_icons(inventory: Path) -> set[str]:
    text = inventory.read_text(encoding="utf-8")
    section = text.split("## Update lookup", 1)[-1]
    icons: set[str] = set()
    for line in section.splitlines():
        match = re.match(r"\|\s*`([^`]+)`\s*\|\s*(.*?)\s*\|", line)
        if not match:
            continue
        icon, references = match.groups()
        if icon.endswith("_die.svg") and ("Board:" in references or "Card:" in references):
            icons.add(icon)
    if not icons:
        raise RuntimeError(f"No die-face references found in {inventory}")
    return icons


def apply_palette(hero: str, icon_dir: Path, inventory_icons: set[str], dry_run: bool) -> dict[str, str]:
    palette = PALETTES[hero]
    names = set(inventory_icons)
    names.update(f"{hero.lower()}-die-{number}.svg" for number in range(1, 7))
    transformed: dict[str, str] = {}
    for name in sorted(names):
        path = icon_dir / name
        text = path.read_text(encoding="utf-8")
        text = text.replace(palette["background_old"], palette["background"])
        text = text.replace(palette["border_old"], palette["border"])
        if hero == "Tuvok":
            # Preserve the phaser's small red detail; only die backgrounds,
            # the IDIC's inner red area, and the requested hand/numeral art change.
            if path.name in {"idic_die.svg", "tuvok-die-6.svg"}:
                text = text.replace(palette["idic_red_old"], palette["background"])
            if path.name in {"salute_die.svg", "tuvok-die-4.svg", "tuvok-die-5.svg"}:
                text = text.replace(palette["skin_old"], palette["skin"])
            if path.name in {"tuvok-die-4.svg", "tuvok-die-5.svg"}:
                text = text.replace(palette["skin_alt_old"], palette["skin"])
        transformed[name] = text
        if not dry_run and text != path.read_text(encoding="utf-8"):
            path.write_text(text, encoding="utf-8")
    return transformed


def source_inner(svg_text: str) -> str:
    text = re.sub(r"^\s*<\?xml[^>]*\?>", "", svg_text, count=1)
    opening = re.search(r"<svg\b[^>]*>", text)
    closing = text.rfind("</svg>")
    if not opening or closing < opening.end():
        raise RuntimeError("Could not extract SVG source contents")
    inner = text[opening.end():closing]
    if re.search(r"<svg\b", inner):
        raise RuntimeError("Nested SVG source elements are not supported")
    return inner


SVG_TOKEN = re.compile(r"<svg\b[^>]*>|</svg>")
SOURCE_ATTR = re.compile(
    r"(?:data-source|data-vector-source|data-original-icon|data-vector-icon)=\"([^\"]+)\""
)


def replace_embedded_svg(text: str, allowed: set[str], sources: dict[str, str]) -> tuple[str, int]:
    tokens = list(SVG_TOKEN.finditer(text))
    stack: list[re.Match[str]] = []
    pairs: list[tuple[re.Match[str], re.Match[str]]] = []
    for token in tokens:
        if token.group().startswith("</"):
            if stack:
                pairs.append((stack.pop(), token))
        else:
            stack.append(token)

    replacements: list[tuple[int, int, str]] = []
    for opening, closing in pairs:
        attrs = opening.group()
        basenames = set()
        for value in SOURCE_ATTR.findall(attrs):
            basename = Path(value).name
            basenames.add(basename if basename.endswith(".svg") else basename + ".svg")
        match = next((name for name in basenames if name in allowed), None)
        if match:
            replacements.append((opening.end(), closing.start(), sources[match]))
    for start, end, inner in reversed(replacements):
        text = text[:start] + inner + text[end:]
    return text, len(replacements)


def sync_hero(hero: str, allowed: set[str], updated_sources: dict[str, str], dry_run: bool) -> tuple[int, int]:
    hero_dir = ROOT / "Heroes" / hero
    icon_dir = hero_dir / "icons"
    sources = {
        name: source_inner(updated_sources.get(name, (icon_dir / name).read_text(encoding="utf-8")))
        for name in allowed
    }
    files = [hero_dir / "hero_board.svg"]
    leaflet = hero_dir / "leaflet.svg"
    if leaflet.is_file():
        files.append(leaflet)
    files.extend(sorted((hero_dir / "cards").glob("*.svg")))
    changed_files = changed_icons = 0
    for path in files:
        original = path.read_text(encoding="utf-8")
        updated, count = replace_embedded_svg(original, allowed, sources)
        if count:
            changed_icons += count
            if updated != original:
                changed_files += 1
                if not dry_run:
                    path.write_text(updated, encoding="utf-8")
    return changed_files, changed_icons


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--hero", choices=tuple(PALETTES) + ("all",), default="all")
    parser.add_argument("--dry-run", action="store_true", help="Report changes without writing files")
    args = parser.parse_args()
    heroes = tuple(PALETTES) if args.hero == "all" else (args.hero,)
    total_files = total_icons = 0
    for hero in heroes:
        inventory = ROOT / "Heroes" / hero / "icon_inventory.md"
        icon_dir = ROOT / "Heroes" / hero / "icons"
        # Shared die types may appear in the inventory, but only local hero
        # die-face masters are in scope for this color update.
        allowed = {name for name in inventory_die_icons(inventory) if (icon_dir / name).is_file()}
        updated_sources = apply_palette(hero, icon_dir, allowed, args.dry_run)
        files, icons = sync_hero(hero, allowed, updated_sources, args.dry_run)
        total_files += files
        total_icons += icons
        verb = "would update" if args.dry_run else "updated"
        print(f"{hero}: found {icons} embedded die-face icons; {verb} {files} SVG files")
    print(f"Total: found {total_icons} embedded icons; {verb} {total_files} files")


if __name__ == "__main__":
    main()
