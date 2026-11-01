"""Preserve basic-power text starts separately from touching activation dice."""
import re


def basic_text_start(texts, baseline):
    """Use Chrome's first non-whitespace character position, not a raw text x.

 For new Upgrade Cards, supply the corresponding hero-board ability's measured
 record transformed uniformly into the card's coordinate system. An unrelated
 layout needs an explicit approved template/style gap; do not guess here.
 """
    candidates=[t for t in texts if abs(t['baseline']-baseline)<.01 and re.search(r'\bDeal\b',t['text'])]
    if len(candidates)!=1:
        raise ValueError('Basic-power row needs one measured original/template text start or an explicit approved layout setting')
    value=candidates[0].get('visibleStartX')
    if value is None:
        raise ValueError('Refresh Chrome measurements: first visible text position is required; raw x may include leading spaces')
    return float(value)


def set_basic_text_anchor(row,texts,baseline):
    row['source_text_start_x']=basic_text_start(texts,baseline)


def new_basic_row(asset, dice_count, origin=(0, 0), scale=1.0, metrics_path=None):
    """Construct approved first-placement anchors without an original asset.

    asset is 'hero_board' or 'upgrade_card'. Metrics are final SVG units;
    origin translates the selected profile and scale applies uniformly once.
    """
    import json
    from pathlib import Path
    if scale <= 0:
        raise ValueError('Layout scale must be positive and uniform')
    path = Path(metrics_path) if metrics_path else Path(__file__).resolve().parents[1] / 'Shared/style_guides/layout_metrics.json'
    metrics = json.loads(path.read_text())
    if asset == 'hero_board':
        profile = metrics['hero_board']['basic_three_rows']
    elif asset == 'upgrade_card':
        profile = metrics['cards']['basic_upgrade']
    else:
        raise ValueError('Select the hero_board or upgrade_card basic-power profile')
    row = next((r for r in profile['rows'] if r['dice'] == dice_count), None)
    if row is None:
        raise ValueError('An unsupported dice count needs an explicit approved profile')
    size = profile['square_size']
    left = profile['dice_group_center_x'] - dice_count * size / 2
    gap = row.get('text_gap', profile.get('text_gap'))
    return {
        'dice_x': [origin[0] + (left + i * size) * scale for i in range(dice_count)],
        'dice_top': origin[1] + row['top'] * scale,
        'dice_size': size * scale,
        'text_start_x': origin[0] + (left + dice_count * size + gap) * scale,
        'text_baseline': origin[1] + row['rules_baseline'] * scale,
        'text_gap': gap * scale,
    }
