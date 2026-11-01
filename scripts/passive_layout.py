"""Shared title-to-rules clearance for passive board abilities and upgrades."""
import json
from pathlib import Path

from ultimate_rules import matrices


def first_passive_baseline(root, group, scale=1.0):
    parents = {c: p for p in root.iter() for c in p}
    panel = parents[group]
    while panel is not None:
        titles = [e for e in panel.iter() if e.tag.endswith('}text')
                  and (e.get('id', '').endswith('-title')
                       or e.get('id') == 'card-title-text')
                  and 'Gardablack' in e.get('font-family', '')]
        if titles:
            break
        panel = parents.get(panel)
    if panel is None or len(titles) != 1:
        raise ValueError('Passive rules need one unambiguous ability/card title')
    metric = Path(__file__).resolve().parents[1] / 'Shared/style_guides/layout_metrics.json'
    if scale <= 0:
        raise ValueError('Layout scale must be positive')
    gap = json.loads(metric.read_text())['matched_ability_layouts']['passive_title_to_first_rules_baseline'] * scale
    ctm = matrices(root); title = titles[0]; tm = ctm[title]; gm = ctm[group]
    if gm[3] <= 0 or abs(gm[1])+abs(gm[2]) > .00001:
        raise ValueError('Rotated/skewed passive rules need a separate profile')
    title_y = tm[1]*float(title.get('x', '0')) + tm[3]*float(title.get('y')) + tm[5]
    return (title_y + gap - gm[5])/gm[3]
