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

- Use **Avenir Next Condensed Regular** at an effective **41.625 px** for ability rules, including the damage text beside basic-power activation rows.
- Use an effective **30.375 px** for the Ultimate's explanatory restriction text, matching the smaller note on Janeway's glass board.
- These are the approved final sizes: the earlier 37 px rules text and 27 px Ultimate note enlarged to **112.5%**. They exclude titles.
- Center rules lines within their panels. Rewrap the text to provide clear, balanced side margins, using the available vertical space rather than reducing the approved font size. Preserve wording, numerals, punctuation, phase colors, and icon order.
- Match the first rules line's gap below its activation row to Janeway's approved Get Off My Ship panel. Basic powers retain their three activation rows with damage rules alongside them.
- Vertically center inline icons against their text line. Keep multiword phase names together where practical and avoid isolating a number from its following icon.

## Effective sizes and existing transforms

The rules and icon sizes below describe their final size in the board coordinate system, including content-group scaling. Janeway's glass board retains a `scale(1.125)` content transform: its local 37 px rules text renders at 41.625 px, its local 27 px Ultimate note at 30.375 px, and its local icon dimensions scale in the same way. Use either these local values with that transform or the final dimensions without it; do not apply the increase twice. Title sizes are set separately and are not multiplied by the rules-content transform.

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

## Shared shadows for die face rows

Consecutive die face icons in the same row must share a single shadow around the entire icon group, including when their borders touch.

- Remove the individual shadows from the die face icons in that group.
- Build the shared shadow from the combined silhouette of all icons in the group.
- Render that shadow behind the complete group, so no icon's shadow falls over a neighboring icon or reveals the order in which the icons were drawn.

## Punctuation after die face icons

When a punctuation mark immediately follows a die face icon or die face group, leave enough horizontal space that the punctuation mark's shadow does not fall over the right edge of the die face icon. Judge the spacing using the rendered shadow as well as the visible punctuation glyph.

## Die face icon sizing

Die face icons have three separate classes, each with its own sizing rules based on where it appears on the board:

1. **Activation icons:** Use **95.625 × 95.625 units** per die face icon in the single activation row at the top of an ability panel, including the Ultimate panel. Defense die icons and large straight and small straight icons belong to this class. Scale these composite icons proportionally so their largest square measures **95.625 × 95.625 units**, including its outer black border; do not size the entire composite icon to 95.625 × 95.625 units.
2. **Basic power activation icons:** Use **67.5 × 67.5 units** per die face icon for abilities with three activation rows containing 3, 4, and 5 die face icons, respectively, with damage text to the right of each row. This sizing applies regardless of the ability's location on the board.
3. **Inline die face icons:** Use **60.75 × 60.75 units** per die face icon. These die faces appear within an ability's rules text, below its activation row or rows, and only in abilities whose rules include die face icons.

These die face sizes include the icon's existing borders and exclude its surrounding shadow.

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
