# Hero Board Style Guide

## Finished board dimensions

- The full board, with all three panels assembled, must be **14⅝ inches (14.625 inches) wide**.
- The left and right side panels must each be **7.19 inches tall**. This height excludes the middle panel's upper curve.
- The middle panel's overall height varies depending on the hero board shape it is based on; there is no fixed overall height for that panel.

## Coordinate scale

Sizes in this guide use the hero board's 4500 × 2700 SVG coordinate system, corresponding to a 15 × 9 inch source canvas. The source canvas dimensions are distinct from the finished board dimensions above. Scale these measurements proportionally if the entire board uses a different coordinate scale.

## Ability title sizing

- Render hero board ability titles, including Ultimate ability titles, at **86 px** at the desired print size. The user may specify a different size.

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

Consecutive die face icons in the same row must share a single shadow around the entire icon group, including when their borders touch.

- Remove the individual shadows from the die face icons in that group.
- Build the shared shadow from the combined silhouette of all icons in the group.
- Render that shadow behind the complete group, so no icon's shadow falls over a neighboring icon or reveals the order in which the icons were drawn.

## Punctuation after die face icons

When a punctuation mark immediately follows a die face icon or die face group, leave enough horizontal space that the punctuation mark's shadow does not fall over the right edge of the die face icon. Judge the spacing using the rendered shadow as well as the visible punctuation glyph.

## Die face icon sizing

Die face icons have three separate classes, each with its own sizing rules based on where it appears on the board:

1. **Activation icons:** Use **85 × 85 units** per die face icon in the single activation row at the top of an ability panel, including the Ultimate panel. Defense die icons and large straight and small straight icons belong to this class. Scale these composite icons proportionally so their largest square measures **85 × 85 units**, including its outer black border; do not size the entire composite icon to 85 × 85 units.
2. **Basic power activation icons:** Use **60 × 60 units** per die face icon for abilities with three activation rows containing 3, 4, and 5 die face icons, respectively, with damage text to the right of each row. This sizing applies regardless of the ability's location on the board.
3. **Inline die face icons:** Use **54 × 54 units** per die face icon. These die faces appear within an ability's rules text, below its activation row or rows, and only in abilities whose rules include die face icons.

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
