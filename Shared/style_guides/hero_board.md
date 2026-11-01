# Hero Board Style Guide

## Finished board dimensions

- The full board, with all three panels assembled, must be **14⅝ inches (14.625 inches) wide**.
- The left and right side panels must each be **7.19 inches tall**. This height excludes the middle panel's upper curve.
- The middle panel's overall height varies depending on the hero board shape it is based on; there is no fixed overall height for that panel.

## Coordinate scale

Sizes in this guide use the hero board's 4500 × 2700 SVG coordinate system, corresponding to a 15 × 9 inch source canvas. The source canvas dimensions are distinct from the finished board dimensions above. Scale these measurements proportionally if the entire board uses a different coordinate scale.

## Ability title font and sizing

- Use **Gardablack** for all ability titles. Keep titles as editable SVG text, using the installed TTF or linking the font file in `Shared/fonts/Gardablack/`; do not convert the letters to vector outlines.
- Render normal ability titles at **50 px** and Ultimate ability titles at **72 px** in the board coordinate system. Use white, uppercase lettering and preserve the font's natural proportions.
- Center normal titles above their activation rows. For an Ultimate, allow the title to occupy the left portion of its top area beside the activation dice.
- A long Ultimate title may use two centered lines at the same 72 px size. Janeway's approved arrangement is “PUNCH YOUR” above “WAY THROUGH,” with a 66-unit baseline interval.
- Handle unusually long titles individually when directed; do not automatically stretch or compress letters to force a fit. The user may specify a different size.

## Rules text font and sizing

- Use **Avenir Next Condensed Regular** at an effective **41.625 px** for regular ability rules, including the damage text beside basic-power activation rows. Ultimate effects and disclaimers follow the separate rules below.
- Do not apply a universal small-note size to Ultimate disclaimers; preserve the original hero-specific effective size below.
- These are the approved final sizes: the earlier 37 px rules text and 27 px Ultimate note enlarged to **112.5%**. They exclude titles.
- Center regular ability rules lines within their panels. Ultimate effects and disclaimers are left-aligned and follow the separate layout below. Rewrap the text to provide clear, balanced side margins, using the available vertical space rather than reducing the approved font size. Preserve wording, numerals, punctuation, phase colors, and icon order.
- Set the first rules baseline to the activation viewport bottom plus **85.441 effective units**, matching Janeway's approved Get Off My Ship panel; use the first-placement tables below. Basic powers retain their three activation rows with damage rules alongside them.
- Vertically center inline icons against their text line. Keep multiword phase names together where practical and avoid isolating a number from its following icon.

## Ultimate panels: independent typography and layout

The original saved hero board is the presentation reference for its Ultimate's uniquely shaped panel. Preserve its left-aligned effects as one continuous line, its exact starting position, and the disclaimer's left alignment, font, placement, and original line breaks. Preserve the title and activation dice separately. Do not apply regular-panel centering, line widths, wrapping, or fallback font sizes to Ultimate content.

| Hero | Effective effects size | Effective disclaimer size |
| --- | ---: | ---: |
| Janeway | 49.95 SVG units | 36.5 SVG units |
| Tuvok | 49.950002 SVG units | 30.375 SVG units |

These sizes are in the full board's SVG coordinate system, after all nested transforms. Janeway's effects use local 37-unit text with both 1.2 and 1.125 scaling; her 36.5-unit disclaimer is outside those scale groups. Tuvok's effects and disclaimer declare their effective sizes directly. Do not multiply an already effective size again, or force one hero's disclaimer size onto another.

Markdown must distinguish activation, effects, and disclaimer with `data-ultimate-role` values. Keep the effects in one paragraph without forced line breaks and mark the block left-aligned and non-wrapping. Display any source disclaimer absent from gameplay rules as a separate asset note. Conversion scripts must read the actual original Ultimate layout, preserve its transforms, and validate effective sizes, anchors, and line counts. If changed wording exceeds the available line, report that for layout review; do not silently shrink, wrap, or center it.

## Effective sizes and existing transforms

The rules and icon sizes below describe their final size in the board coordinate system, including content-group scaling. Janeway's glass board retains a `scale(1.125)` content transform: its local 37 px rules text renders at 41.625 px, its local icon dimensions scale in the same way. Use either these local values with that transform or the final dimensions without it; do not apply the increase twice. Title sizes are set separately and are not multiplied by the rules-content transform.

## Standard icon size

Use an effective **60.75 × 60.75 unit** viewport for every instance of these icon types:

- Status tokens, including Coffee, Command Codes, and Reprimand.
- Normal damage.
- Undefendable damage.
- Card draw.
- Roll die.
- Damage prevention.
- CP.
- Healing.

Preserve each icon's aspect ratio within its viewport. The 60.75 × 60.75 measurement includes the icon's existing borders and excludes its surrounding shadow.

## Shadows on dice rows

Activation dice rows must have no individual or shared halo/drop shadows. This includes ordinary activation rows, three-row basic powers, Ultimates, and the composite Small Straight, Large Straight, and defense requirement icons. Remove shadow/halo filters inherited from row groups and embedded in icon instances. Preserve the icon surface shading, highlights, borders, geometry, sizes, and positions; keep icon masters unchanged.

This activation requirement overrides older shared-row shadow guidance. It does not remove the established treatment from rules text or other non-activation content. Where a non-activation die group still needs a shadow, use one group shadow rather than overlapping individual shadows.

## Punctuation after die face icons

Gameplay rules must not contain commas immediately after dice icons or groups. Preserve other punctuation. When another punctuation mark immediately follows a die face icon or die face group, leave enough horizontal space that the punctuation mark's shadow does not fall over the right edge of the die face icon. Judge the spacing using the rendered shadow as well as the visible punctuation glyph.

## Die face icon sizing

Die face icons have three separate classes, each with its own sizing rules based on where it appears on the board:

1. **Activation icons:** Use **95.625 × 95.625 units** per die face icon in the single activation row at the top of an ability panel, including the Ultimate panel. Defense die icons and large straight and small straight icons belong to this class. Scale these composite icons proportionally so their largest square measures **95.625 × 95.625 units**, including its outer black border; do not size the entire composite icon to 95.625 × 95.625 units.
2. **Basic power activation icons:** Use **67.5 × 67.5 units** per die face icon for abilities with three activation rows containing 3, 4, and 5 die face icons, respectively, with damage text to the right of each row. This sizing applies regardless of the ability's location on the board.
3. **Inline die face icons:** Use **60.75 × 60.75 units** per die face icon. These die faces appear within an ability's rules text, below its activation row or rows, and only in abilities whose rules include die face icons.

These die face sizes include the icon's existing borders and exclude its surrounding shadow.

## Spacing and first-placement profiles for new boards

The numeric companion [layout_metrics.json](layout_metrics.json) defines reusable new-asset profiles. These defaults were measured from the original Janeway board and the approved Markdown conversion spacing. They let a first-time board use the established layout without needing an existing SVG for that new hero. An existing asset's measured anchors take precedence over these defaults; do not normalize existing designs to this table.

### Coordinate origin and scaling

For each regular ability, use the transformed `(0,0)` of its `*-vector-panel` frame as the reference origin. Values below are **effective full-board SVG units** relative to that origin, not unscaled child-group coordinates. For a new panel, add its chosen origin to these offsets. Sizes already include the approved 1.125 content enlargement: apply them directly, or divide by the group's uniform scale if constructing inside a scaled group. Never apply the enlargement twice. Scale the entire profile uniformly if the board coordinate scale changes; do not independently stretch x/y spacing with the old frame's slight nonuniform transforms.

### Gaps between icons and following text

Within a consecutive die-face group, outer borders touch: **zero gap**, zero margin, and no overlap. Source whitespace between icon tags has no visual width.

For inline dice/status/damage icons followed by prose, use **0.185 em** of clear horizontal space at the rules-text font size (about **7.701 units** at 41.625). Apply the gap once, not both as SVG positioning and a rendered space. Treat a consecutive dice group as one item. Do not insert the gap between its dice. Follow the rules below for basic-power text, which needs a larger measured gap.

For a new three-row basic power, keep the dice-group centers aligned at **x = 230.6975** relative to the frame origin. Use 67.5-unit squares and position the first visible rules character from the last die's right edge using the row-specific gap:

| Dice count | Activation top y | Rules baseline y | Gap to following text |
| --- | ---: | ---: | ---: |
| 3 | 142.868 | 194.618 | 20.8125 |
| 4 | 247.493 | 299.243 | 18.5625 |
| 5 | 350.993 | 402.743 | 23.0625 |

For each row, `dice_left = 230.6975 − dice_count × 67.5 ÷ 2` and `text_start_x = dice_left + dice_count × 67.5 + gap`. Measure the first non-whitespace character, not the text element's raw `x` if it contains leading spaces. These gaps reproduce Fire Phasers' original spacing; do not replace them with a normal space or add literal spaces to `rules.md`.

### Activation rows with rules underneath

Center the complete activation symbol/group beneath the title. The composite viewport includes its label pill; scale straight and defense symbols by the largest square as described above, not by total width.

| Activation profile | Viewport top y | Viewport height | First rules baseline y |
| --- | ---: | ---: | ---: |
| Ordinary die-face row | 142.868 | 95.625 | 323.933 |
| Small or Large Straight | 143.439 | 128.436 | 357.315 |
| Defense requirement | 143.438 | 94.485 | 323.364 |

The general rule is **first baseline = activation viewport bottom + 85.441 units**. This is a baseline clearance, not a gap to the top of the letters. The tiny composite top/height differences are part of the measured reference. Use the complete symbol viewport when measuring; keep activation shadows disabled. Values rounded to three decimals may differ from a saved source by up to 0.002 unit.

### Subsequent regular rules lines

Retain the fixed first baseline above. For later lines, preserve the Markdown conversion spacing: minimum line-box height **49.95**, enlarged to the tallest inline icon on that line (normally **60.75**); empty gap **5.625** before a continuation line or **13.5** before a new paragraph. Center inline icons vertically in the line box. Put the text baseline **13.32** below its line-box center.

Thus the baseline advance is `previous_height ÷ 2 + gap + next_height ÷ 2`. Anchor the first line box from its required baseline rather than adding another default top gap. Do not let whole-block vertical centering move the title, activation row, or first baseline. Basic-power rows and Ultimates retain their separate positions.

### First-time Ultimate panels

Use an explicitly selected existing shaped-panel template; regular ability profiles do not apply. For the current wide Ultimate frame, the effects start is **x = 14**, baseline **y = 259.72844**, left-aligned at an effective **49.95-unit** size on one line. Preserve the chosen template's frame, title and text treatment.

| Ultimate template | First activation x | Activation top y | Dice size | Disclaimer x | Disclaimer baselines | Disclaimer size |
| --- | ---: | ---: | ---: | ---: | --- | ---: |
| Janeway | 799.37113 | 54.146 | 95.625 | 297.346154 | 378.047547; 415.131865 | 36.5 |
| Tuvok | 792.9375 | 70.1875 | 95.625 | 297 | 378; 415 | 30.375 |

Ultimate coordinates are relative to the chosen `*-vector-panel` origin and already include all source scaling. Keep the original two disclaimer lines left-aligned. Do not mix one template's activation placement with the other's disclaimer settings. A new panel shape requires an explicit new profile rather than guessed offsets or automatic shrinking/wrapping.

## Hero board print kit

Create the print kit from the hero's saved `hero_board.svg` using Google Chrome so installed fonts render correctly.

1. Divide the board into three equal vertical panels by splitting its horizontal width into thirds: left, middle, and right. On a 4500 × 2700 board, each third is 1500 units wide.
2. Scale each panel proportionally to **4⅞ inches (4.875 inches) wide before any rotation**. A full-height third then measures 4.875 × 8.775 inches.
3. Use two **US letter pages in landscape orientation (11 × 8.5 inches)**, with no browser headers or footers.
4. On page 1, place the middle panel alone, rotated 90 degrees and centered. After rotation, it measures 8.775 × 4.875 inches.
5. On page 2, place the left and right panels side by side, in that order. Crop only the blank whitespace above their artwork so both fit, preserving their 4.875-inch widths and all artwork, icons, and text. For a board with 600 blank units at the top, crop those 600 units; each side panel then measures 4.875 × 6.825 inches. Center the pair on the page with a 0.25-inch gap.
6. Add thin black cut-guide lines in the white space on both pages. Extend the alignment of every flat component edge in both directions to the page edges, leaving **⅛ inch (0.125 inch) of clearance** from the actual board components. Keep the guides entirely in white space and clear of every component, including the curved dome near a tangent extension. Where another component interrupts an extension, stop before it and resume beyond it with the same clearance. Omit any segment where the required clearances leave no room for a line.
7. Print through Chrome at the specified physical dimensions, with backgrounds enabled and no fit-to-page scaling. Preserve vector content where possible and retain at least 300 dpi effective resolution for raster artwork.
8. Verify the exported PDF has exactly two letter-size pages, the requested panel order and rotation, correct physical sizes, cut guides aligned to all flat edges with the required clearance, and no clipped content. Render and inspect both final PDF pages before reporting completion.
9. Save the PDF in `STDT Outputs`, using the current hero's lowercase name in the filename: `<hero>_svg_hero_board _print_kit.pdf`.

For physical printing, select **Actual Size / 100%**, rather than a setting that shrinks or fits the PDF to the printable area.

## Matching passive and basic-power layouts across board and upgrades

Use the explicit Markdown layout profiles and `matched_ability_layouts` in `layout_metrics.json`. These authorized corrections override preservation of a mismatched original anchor. Existing profiles without these markers retain their established positions.

- `data-passive-layout="title_rules_v1"`: place the first rules baseline **79 effective SVG units below the ability/card title baseline**, matching Kolinar II. Apply on both the passive board panel and its Upgrade Card. Use `scripts/passive_layout.py`; keep subsequent Markdown line spacing, approved font sizes, title, artwork, and PASSIVE label unchanged. A passive ability has no activation row, so do not use an activation-to-text clearance.
- `data-basic-layout="touching_deal_v1"`: for each three-, four-, and five-die damage row, leave **16.667 effective SVG units** from the final die's right border to the first visible character of **Deal**, on both board and Upgrade Cards. Use `set_standard_deal_anchor` in `scripts/basic_power_layout.py`. Consecutive dice still touch. Keep their original positions, sizes and vertical anchors. Remove colons between these activation groups and Deal in `rules.md`; never preserve a deleted colon's x position or insert a colon during conversion.

Measure in final root SVG coordinates and compensate for nested transforms exactly once. Scale both constants uniformly if the whole asset coordinate scale changes. Apply the same selected profile to an ability and all its upgrades, including first-time generation, rather than inheriting incompatible legacy offsets. Verify the gaps and starting baselines numerically before saving; do not change unrelated abilities merely to normalize them.
