# Leaflet Style Guide

## Token-panel header and rules spacing

Use the `token_panel_v1` profile in [layout_metrics.json](layout_metrics.json) for new leaflet token panels. Janeway's approved Coffee panel is the spacing reference. At the standard **1350 × 2550** SVG scale, place the first rules-text baseline **113.82 units below the shared type/stack-limit baseline**:

`first_rules_baseline = type_and_stack_limit_baseline + 113.82`

This is a baseline-to-baseline measurement, not a blank line, a margin from the panel edge, or a distance from the bottom of an icon. Measure after all nested transforms. Scale the clearance uniformly once if the entire leaflet uses a different coordinate scale. Do not copy a token-specific absolute y position or reuse the old position of a deleted summary line.

For first-time generation, position the type and stack-limit text on their shared baseline, calculate the first rules baseline with this formula, then flow subsequent lines below it. No original SVG is needed. For a spacing correction, move the complete rules block, including inline icons, as a unit; preserve its font, wrapping, paragraph gaps, and internal line spacing. Do not vertically center the block afterward. Keep titles, header rows, panel artwork, large token emblems, and die-reference legends fixed. If the block no longer fits its panel, report the conflict instead of shrinking text or reducing this clearance.

Janeway uses 38-unit header text and 46-unit rules text in this reference. Preserve established hero-specific typography on existing leaflets; this profile sets the starting anchor, not a universal replacement font size.

## Markdown and converters

Mark leaflet rule blocks in `rules.md` with `data-leaflet-layout="token_panel_v1"`. This is presentation metadata, not gameplay text. HTML spacer divs and Markdown blank lines do not establish SVG positioning. Do not recreate removed summary/tagline text to fill the header gap.

Conversion scripts must use `scripts/leaflet_layout.py` (`first_rules_baseline` for new layouts; `apply_token_spacing` after generating a rules group). The helper reads the shared metric and accounts for existing transforms. Validate all token panels' resulting baseline clearances numerically, and check the saved leaflet for panel overflow.

Janeway's reference root-coordinate baselines:

| Panel | Type/stack-limit baseline | First rules baseline | Clearance |
| --- | ---: | ---: | ---: |
| Coffee | 201.5 | 315.32 | 113.82 |
| Command Codes | 961.5 | 1075.32 | 113.82 |
| Reprimand | 1766.5 | 1880.32 | 113.82 |

These absolute positions document the current reference only. New panel positions use the formula above.
