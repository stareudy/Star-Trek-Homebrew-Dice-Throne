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

## Shared shadows for die face rows

Where shadows are needed, consecutive die face icons in the same row must share a single shadow around the entire icon group, including when their borders touch.

- Remove the individual shadows from the die face icons in that group.
- Build the shared shadow from the combined silhouette of all icons in the group.
- Render that shadow behind the complete group, so no icon's shadow falls over a neighboring icon or reveals the order in which the icons were drawn.

## Punctuation after die face icons

When a punctuation mark immediately follows a die face icon or die face group, leave enough horizontal space that the punctuation mark's shadow does not fall over the right edge of the die face icon. Judge the spacing using the rendered shadow as well as the visible punctuation glyph.

## Die face icon sizing

Use the same three die face icon classes and sizes as the hero board. On Upgrade Cards, classify icons by their role in the corresponding ability; use the inline class for die faces within card rules text.

1. **Activation icons:** Use **85 × 85 units** per die face icon in the single activation row at the top of an ability panel, including the Ultimate panel. Defense die icons and large straight and small straight icons belong to this class. Scale these composite icons proportionally so their largest square measures **85 × 85 units**, including its outer black border; do not size the entire composite icon to 85 × 85 units.
2. **Basic power activation icons:** Use **60 × 60 units** per die face icon for abilities with three activation rows containing 3, 4, and 5 die face icons, respectively, with damage text to the right of each row. Use this class when that arrangement appears on an Upgrade Card, regardless of the corresponding ability's location on the hero board.
3. **Inline die face icons:** Use **54 × 54 units** per die face icon. These die faces appear within rules text, below any activation row or rows when present, and only where the rules include die face icons.

These die face sizes include the icon's existing borders and exclude its surrounding shadow.
