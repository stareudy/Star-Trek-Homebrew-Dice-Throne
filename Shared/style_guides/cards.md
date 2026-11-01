# Cards Style Guide

## Finished card dimensions

Render each individual card for print at **2.25 inches wide × 3.5 inches tall**.

## Card types

Cards have five types:

- **Roll Phase Action:** An action card identified as a Roll Phase Action.
- **Main Phase Action:** An action card identified as a Main Phase Action.
- **Instant Action:** An action card identified as an Instant Action.
- **Upgrade Card:** A card that upgrades a hero-board ability. Its title matches the ability name followed by `II` or `III`, and its rules occupy a full panel rather than the bottom-half rules box used by action cards.
- **Two Panel Upgrade Card:** An upgrade card with two ability panels. The larger top panel matches an existing ability on the hero board, while the smaller lower panel introduces a new ability. Both the upper and lower panels have their own row of activation die face icons.

The three action types identify the card's timing category. Standard Cards and Hero Action Cards are separate classifications describing whether an action card is shared across decks or unique to a hero; either classification can contain cards from the action types above.

## Artwork and rules panels

Most cards have separate panels, with artwork on top and rules text below on a black background.

### Fixed divider for artwork-and-rules cards

Use the approved Janeway `cards/resolve.svg` as the layout reference for action cards with an upper artwork panel and a lower black rules panel. In the individual card's **675 × 1050 unit** coordinate system, preserve these dimensions:

- **Artwork viewport:** `x=31`, `y=159`, `width=613`, `height=476`, ending at `y=635`. Its aspect ratio is **613:476**.
- **Middle divider:** `x=24`, `y=635`, `width=627`, `height=8`. Its bottom edge is at `y=643`.
- **Rules panel:** starts at `x=31`, `y=643`, spans `613` units in width, and ends at `y=1020`, including its rounded bottom corners. Its bounding dimensions are **613 × 377 units**, with an aspect ratio of **613:377**.

Keep the divider and both panel dimensions fixed. Fit rules text and icons within the rules panel; do not move the divider or resize either panel to accommodate the content. Preserve the artwork's crop and placement from the matching PNG card when rebuilding an existing asset, and clip the artwork to its viewport so it stays inside the colored frame and leaves the outer black border clear.

These coordinates use the same 300-units-per-inch scale as the card-page coordinate system below. Scale all coordinates uniformly if using a different coordinate scale. The finished card remains **2.25 × 3.5 inches**.

This layout applies to artwork-and-rules action cards. It does **not** set the divider position for Two Panel Upgrade Cards, whose two panels contain separate abilities.

Text and icons in these black rules panels do not need shadows, including shared shadows around die face groups. This is an exception to the shadow guidance below; that guidance applies where shadows are needed for readability over artwork.

## CP tags

- Every card must have a CP tag.
- Roll Phase Action, Main Phase Action, and Instant Action cards must each use a CP tag matching their timing class.
- All versions of Upgrade Cards, including Two Panel Upgrade Cards, must use a **blue Main Phase Action CP tag**.

## Upgrade card colors

All Upgrade Cards, including Two Panel Upgrade Cards, must have their borders and title headers color matched to the corresponding level-one ability on the hero board.

## Upgrade card artwork

All Upgrade Cards, including Two Panel Upgrade Cards, have artwork behind their rules text. Whenever possible, position the text to avoid covering important features of the artwork. When there is a large amount of rules text, covering those features is acceptable if it cannot reasonably be avoided.

## Coordinate scale

Sizes in this guide use a 3300 × 2550 card-page SVG coordinate system, corresponding to an 11 × 8.5 inch source canvas. This uses the same scale of 300 units per inch as the hero board style guide. Scale these measurements proportionally if the entire card page uses a different coordinate scale.

## Card title font and sizing

Use **Gardablack** for all card titles. Keep titles as editable SVG text, using the installed TTF or linking the font file in `Shared/fonts/Gardablack/`; do not convert the letters to vector outlines.

Render card titles at **86 px** by default. The user may specify a different size.

## Standard icon size

Use a 54 × 54 unit viewport for every instance of these icon types:

- Status tokens, including Coffee, Command Codes, and Reprimand.
- Normal damage.
- Undefendable damage.
- Card draw.
- Roll die.
- Damage prevention.
- CP.
- Healing.

Preserve each icon's aspect ratio within its viewport. The 54 × 54 measurement includes the icon's existing borders and excludes its surrounding shadow.

## Shadows on dice rows

Activation dice rows must have no individual or shared halo/drop shadows. This includes ordinary activation rows, three-row basic powers, Ultimates, and the composite Small Straight, Large Straight, and defense requirement icons. Remove shadow/halo filters inherited from row groups and embedded in icon instances. Preserve the icon surface shading, highlights, borders, geometry, sizes, and positions; keep icon masters unchanged.

This activation requirement overrides older shared-row shadow guidance. It does not remove the established treatment from rules text or other non-activation content. Where a non-activation die group still needs a shadow, use one group shadow rather than overlapping individual shadows.

## Punctuation after die face icons

Gameplay rules must not contain commas immediately after dice icons or groups. Preserve other punctuation. When another punctuation mark immediately follows a die face icon or die face group, leave enough horizontal space that the punctuation mark's shadow does not fall over the right edge of the die face icon. Judge the spacing using the rendered shadow as well as the visible punctuation glyph.

## Die face icon sizing

Use the same three die face icon classes as the hero board, with the card-specific sizes listed below. The hero board's enlarged icon sizes do not change these card sizes. On Upgrade Cards, classify icons by their role in the corresponding ability; use the inline class for die faces within card rules text.

1. **Activation icons:** Use **85 × 85 units** per die face icon in the single activation row at the top of an ability panel, including the Ultimate panel. Defense die icons and large straight and small straight icons belong to this class. Scale these composite icons proportionally so their largest square measures **85 × 85 units**, including its outer black border; do not size the entire composite icon to 85 × 85 units.
2. **Basic power activation icons:** Use **60 × 60 units** per die face icon for abilities with three activation rows containing 3, 4, and 5 die face icons, respectively, with damage text to the right of each row. Use this class when that arrangement appears on an Upgrade Card, regardless of the corresponding ability's location on the hero board.
3. **Inline die face icons:** Use **54 × 54 units** per die face icon. These die faces appear within rules text, below any activation row or rows when present, and only where the rules include die face icons.

These die face sizes include the icon's existing borders and exclude its surrounding shadow.

## Spacing and first-placement profiles for new cards

Use [layout_metrics.json](layout_metrics.json) for the same constants in machine-readable form. These new-asset profiles reproduce the established Janeway Upgrade Card layouts and the Markdown conversion's regular line spacing. Existing card measurements override defaults; no saved card is repositioned merely to match this table.

### Coordinates and effective sizing

All positioning tables below use the **individual card's final `viewBox="0 0 675 1050"` coordinates**, with origin at the top left. They already include the approved references' **1.125 content scale**. Their effective square sizes are **95.625** for an ordinary activation die, **67.5** for a basic-power die, and **60.75** for an inline Upgrade Card icon. These correspond to the local construction sizes 85, 60, and 54 listed above, followed by the source 1.125 scale. Use either the construction sizes inside that same transform or these final sizes directly; do not mix the two systems or apply scaling twice. Upgrade rules use the reference's effective **41.625-unit** font. Action rules use **37.5-unit** text and **54-unit** inline icons.

A new Upgrade Card normally copies its matching hero-board ability panel. Map the panel uniformly into the card coordinate system, retaining its style and artwork registration, then use the applicable card placement profile. Choose the profile by layout role, not by the hero's name. Do not move a fixed action-card divider to accommodate these values.

### Horizontal icon-to-text spacing

Consecutive die-face icons touch with **zero gap**, zero margin and no overlap. After a completed inline icon/group, use **0.185 em** before following prose: about **7.701 units** at the Upgrade Card font or **6.938 units** at the Action Card font. Apply this once, independently of markup whitespace. Keep activation rows shadow-free and omit commas immediately after dice icons.

For a three-row basic Upgrade Card, use **67.5-unit** dice, align the dice-group centers at **x = 222.647625**, and leave **16.667 units** from the last die's right border to the first visible rules character on every row. Compute `dice_left = 222.647625 − dice_count × 67.5 ÷ 2`, then `text_start_x = dice_left + dice_count × 67.5 + 16.667`. This reproduces the original Fire Phasers II/III spacing; a normal word space is too small. Ignore leading whitespace when measuring the text start.

| Dice count | Activation top y | Rules baseline y |
| --- | ---: | ---: |
| 3 | 145 | 192.25 |
| 4 | 248.5 | 295.75 |
| 5 | 352 | 399.25 |

### Single activation row and first rules baseline

Center the activation group at **x = 337.5**. Preserve symbol proportions and scale composite icons by their largest square, including the outer border. For straight/defense symbols, their full viewport includes the label or remaining composite geometry.

| Upgrade layout profile | Activation top y | Activation viewport height | First rules baseline y | Baseline after viewport bottom |
| --- | ---: | ---: | ---: | ---: |
| Standard effects (Shore Leave II reference) | 145 | 95.625 | 347.5 | 106.875 |
| Roll-resolution effects (Tactical Exercises II reference) | 145 | 95.625 | 362.125 | 121.5 |
| Defense (Shields Up II/III reference) | 145.570 | 94.485 | 343.5625 | 103.5075 |

The standard-effects profile is the default for a new single-row Upgrade Card. Select roll-resolution when its rules open with a separate roll instruction, and defense for a defensive ability. For a newly introduced straight symbol, retain its full composite viewport height and calculate the first baseline as its bottom plus the selected profile's clearance; do not pretend the whole symbol is one square. Two-panel Upgrade Cards use the corresponding local panel profiles and need explicit lower-panel origins from their template; do not reuse these full-card absolute y values for the lower panel.

### Subsequent lines and Action Cards

For Upgrade Cards, use line-box height `max(49.95, tallest inline icon height)`, normally 60.75 when icons occur; gap **5.625** before a continuation line and **13.5** before a new paragraph. Put the text baseline **13.32** below the line-box center. Keep the first baseline fixed from the selected profile. The advance is `previous_height ÷ 2 + gap + next_height ÷ 2`; do not vertically recenter the entire block afterward.

Action Cards have no activation-dice header row. Keep their fixed rules panel at `x=31`, `y=643`, width `613`, bottom `1020`; center the rules block at `(337.5, 831.5)` while fitting within that panel. Use line-box height `max(45, tallest inline icon height)`, normally 54; continuation gap **5**, paragraph gap **12**, and baseline **12** below each line-box center. The number of lines determines the first baseline through block centering, not a borrowed Upgrade Card y value. Preserve the original/template's safe margins and artwork/divider geometry.

If a chosen profile does not fit a genuinely new panel shape or content arrangement, report the conflict for explicit layout review. Do not silently reduce the font, change activation/text starting anchors, invent an arbitrary gap, or insert manual spaces into `rules.md`. New shapes need named placement profiles with defined origins and scales.

## Matching passive and basic-power layouts across board and upgrades

Use the explicit Markdown layout profiles and `matched_ability_layouts` in `layout_metrics.json`. These authorized corrections override preservation of a mismatched original anchor. Existing profiles without these markers retain their established positions.

- `data-passive-layout="title_rules_v1"`: place the first rules baseline **79 effective SVG units below the ability/card title baseline**, matching Kolinar II. Apply on both the passive board panel and its Upgrade Card. Use `scripts/passive_layout.py`; keep subsequent Markdown line spacing, approved font sizes, title, artwork, and PASSIVE label unchanged. A passive ability has no activation row, so do not use an activation-to-text clearance.
- `data-basic-layout="touching_deal_v1"`: for each three-, four-, and five-die damage row, leave **16.667 effective SVG units** from the final die's right border to the first visible character of **Deal**, on both board and Upgrade Cards. Use `set_standard_deal_anchor` in `scripts/basic_power_layout.py`. Consecutive dice still touch. Keep their original positions, sizes and vertical anchors. Remove colons between these activation groups and Deal in `rules.md`; never preserve a deleted colon's x position or insert a colon during conversion.

Measure in final root SVG coordinates and compensate for nested transforms exactly once. Scale both constants uniformly if the whole asset coordinate scale changes. Apply the same selected profile to an ability and all its upgrades, including first-time generation, rather than inheriting incompatible legacy offsets. Verify the gaps and starting baselines numerically before saving; do not change unrelated abilities merely to normalize them.
