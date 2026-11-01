"""Place leaflet token rules from the header, including first-time layouts."""
import json
from pathlib import Path

from ultimate_rules import matrices

SVG = '{http://www.w3.org/2000/svg}'
METRICS = Path(__file__).resolve().parents[1] / 'Shared/style_guides/layout_metrics.json'


def first_rules_baseline(header_baseline, scale=1.0):
    if scale <= 0:
        raise ValueError('Leaflet scale must be positive')
    profile = json.loads(METRICS.read_text())['leaflet']['token_panel_v1']
    return header_baseline + profile['header_to_first_rules_baseline'] * scale


def apply_token_spacing(root, rules_group, profile='token_panel_v1'):
    """Move the whole rules block once; retain all its internal line spacing.

    Measure both baselines in root coordinates, accounting for nested transforms.
    Existing typography remains intact. No previous SVG or token-specific y is needed.
    """
    if profile != 'token_panel_v1':
        raise ValueError('Unknown leaflet layout profile: ' + profile)
    parents = {c: p for p in root.iter() for c in p}
    # Some saved leaflets keep rules and the frame/header as sibling groups.
    panel_id = rules_group.get('id', '').removesuffix('-text-rules')
    panel = next((e for e in root.iter() if e.get('id') == panel_id), None)
    if panel is None:
        panel = parents[rules_group]
    while panel is not None:
        headers = [e for e in panel.iter() if e.tag == SVG+'text'
                   and ('Status Effect' in ''.join(e.itertext())
                        or 'Stack limit:' in ''.join(e.itertext()))]
        if headers:
            break
        panel = parents.get(panel)
    if panel is None:
        raise ValueError('Missing containing token panel/type/stack-limit header')
    ctm = matrices(root)

    def baseline(e):
        m = ctm[e]
        return m[1]*float(e.get('x', '0')) + m[3]*float(e.get('y', '0')) + m[5]

    header_positions = [baseline(e) for e in headers]
    if max(header_positions)-min(header_positions) > .01:
        raise ValueError('Type and stack-limit headers must share one baseline')
    body = [e for e in rules_group.iter() if e.tag == SVG+'text'
            and e.get('data-md-text') and (e.text or '').strip()]
    if not body:
        raise ValueError('No generated rules text to position')
    viewbox = [float(v) for v in root.get('viewBox').replace(',', ' ').split()]
    scale = viewbox[2] / 1350
    if abs(viewbox[3]/2550-scale) > .0001:
        raise ValueError('A different leaflet aspect ratio needs an explicit layout profile')
    desired = first_rules_baseline(header_positions[0], scale)
    current = min(baseline(e) for e in body)
    matrix = ctm[rules_group]
    if abs(matrix[1])+abs(matrix[2]) > .00001 or matrix[3] <= 0:
        raise ValueError('Rotated/skewed rules groups need an explicit layout profile')
    local_shift = (desired-current)/matrix[3]
    if abs(local_shift) > .000001:
        rules_group.set('transform', (rules_group.get('transform', '')
                                     + f' translate(0 {local_shift:.8f})').strip())
    rules_group.set('data-leaflet-layout', profile)
    return {'header_baseline': header_positions[0], 'first_rules_baseline': desired,
            'root_shift': desired-current}
