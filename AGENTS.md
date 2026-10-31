# Project Instructions

## Working in this project

- Read this file at the start of each task and follow it throughout the work.
- Treat the directory containing this file as the project root. Check exact target paths before listing, moving, renaming, or deleting files.
- Make only changes needed for the user's request. Check for destination conflicts before moving or renaming, and verify file operations afterward.
- For inventory or comparison requests, state the scope and method briefly; do not change files unless asked.
- When the user asks to push a commit but has not specified a commit message, ask them what message to use before creating or pushing the commit. Do not create or push a commit without a message that notes what changed.
- Whenever the user says work is approved or finished, ask whether they want to commit it to GitHub. Do not create or push a commit unless they say yes; if they do, follow the commit-message rule above.
- When the user says a to-do item is finished, remove that item from the relevant `todo.md`. If it seems finished but the user has not said so, ask them before removing it.
- Keep progress updates concise, and report completed changes with the affected paths.
- Every time the user sends a message, check its timestamp against earlier available message timestamps for this project on the same day, using the user's local timezone. If message timestamps are unavailable, use the current time as the observation time and retain it in conversation context for later checks; do not invent earlier timestamps. When the timestamps indicate more than two hours of project work since the start of the current session, briefly remind the user that it is time to take a break. Account for breaks the user reports, and begin a new session after a reported break; do not count known breaks as working time.
- At the end of every completed task, give a short usage report with only the weekly usage remaining, the percent used by the task, and when the weekly limit resets. Estimate task consumption by comparing the last reported weekly usage with the current usage; use decimal precision when available. If usage is reported only in whole percentages and the task consumed less than 1%, say “less than 1%” rather than rounding it to 0%. If no earlier weekly usage report is available for comparison, say task usage cannot be determined.
- When making raster image pixels fully transparent, set their RGB channels to zero at the same time as setting alpha to zero, unless the user explicitly asks to preserve the hidden RGB data.
- Whenever showing a preview of an image with transparency, composite it over a bright neon color that does not appear in the image so transparent areas are easy to see.

## SVG rendering

- Before creating or editing any SVG asset, check `Shared/` for an applicable style guide, including `Shared/style_guides/`. If a guide exists, read it and adhere to it when creating or editing that asset.
- When an SVG contains editable text, use Google Chrome to render it, including SVG-to-PNG and SVG-to-PDF exports, so installed fonts render consistently with the browser.
- For Chrome rendering, reuse a dedicated rendering script at a stable path and invoke it with a consistent command prefix so saved “Always approve” permissions can apply. Run file creation, edits, and other preparation separately from the rendering command; do not bundle them into changing shell scripts or heredocs with the Chrome launch. When approval is required, request a reusable permission scoped to the rendering command and reuse it for future renders.
- When an SVG contains no editable text, use whichever renderer is most effective for accurate output; Chrome is not required.

## SVG artwork references

- Do not embed PNGs or other raster images inside SVG files, including as base64 or data URIs.
- Link to the existing original artwork files using relative paths. Reuse those originals rather than creating duplicate artwork copies, to avoid redundant disk usage.
- Keep artwork references linked so replacing or editing an original artwork file at the same path automatically updates every SVG that renders it on the next render.

## Image edit verification

- Whenever editing any image-format file, inspect a freshly rendered preview of the saved result before reporting completion. Confirm the preview reflects the current file; do not rely on a stale, cached, or earlier render.

## Asset format

- Primary SVG files contain the editable rules text, icons, and layout. Make asset updates directly in those SVGs; do not create or update separate overlays.
- The playtest app stores separate asset versions under `playtest-app/public/assets/`. Rules updates must cover the corresponding primary and playtest app SVGs for the active hero. Preserve each version's artwork, linked resources, and app-specific presentation.
- Raster source artwork and existing exports may still be used where applicable; SVGs are the editable source of truth for asset presentation, while `rules.txt` remains the source of truth for rules.

## Heroes and task scope

- `Shared/` contains materials that may be read for any project task, regardless of which hero is active.
- Do not write to or delete `Shared/` or any of its subfolders or files unless the user explicitly says to do so.
- `Heroes/` contains separate subfolders for multiple Dice Throne heroes.
- Unless the user says otherwise, each task concerns only one hero. The user will identify the hero at the start of each chat; treat that hero's folder as the active scope.
- When considering a hero's abilities, tokens, or cards, treat that hero's `rules.txt` as the primary and definitive source of information.
- Edit a hero's `rules.txt` only when the user directly orders that edit. Otherwise, the user will edit the file manually.
- It is okay to read files in another hero's folder when the user asks. Otherwise, ignore other heroes' folders: do not inspect or change them as part of the task.
- `Heroes/Future Heroes/` is exempt from the file organization and naming conventions in this document.

## Protecting hero files

- Store assistant-created temporary files, drafts, previews, and working backups in a Codex-provided writable workspace outside this project.
- Write, edit, move, or delete files in this project only when the user explicitly asks for that project-file change. A request to inspect or preview an asset does not authorize changing project files. When the user asks to update an asset, make only the requested final project-file changes after following the approval steps below; keep intermediate work outside the project.

## Hero folder organization

Use `Heroes/Janeway/` as the reference layout for hero folders, except for `Heroes/Future Heroes/`:

- The hero folder root holds the hero's primary/final deliverables, including editable SVGs, `rules.txt`, and `todo.md` when present.
- `art/` holds source art/canvas files for the assets. Use the matching asset name as the filename stem. For example, `cards_page_1.png` through `cards_page_N.png`, `hero_board.png`, and `leaflet.png`. Do not keep PDF copies of PNG assets in this folder.
- Rules text and icons live in the primary SVG files, not in separate overlay files. Any legacy `overlays/` files are not part of the current update workflow; do not alter or delete them unless explicitly requested.
- `icons/` holds individual reusable icon and token image files, using descriptive filenames that identify their content (for example, `coffee_die.png` or `combadge_token.png`).
- `backups/` is a reserved subfolder at the root of each hero folder. Do not infer this as the destination from a generic request to back files up. Keep working or safety backups in a Codex-provided writable workspace outside this project unless the user explicitly names another destination. Add, edit, move, or delete anything in the hero-root `backups/` folder only when the user explicitly directs that location. If a persistent backup destination is needed and none is specified, use the external Codex workspace.

## Asset dimensions and resolution

- Whenever an authorized edit adds or removes canvas width or height, crops an asset, or changes its SVG `viewBox`, synchronize its declared physical print dimensions with the applicable style guide and any explicit user size overrides. Do this as part of the edit, without requiring a separate request. Distinguish finished trim size from source-canvas, bleed, and page size.
- For SVGs, declare root `width` and `height` in physical units (`in` or `mm`), preserving the required print size and uniform scale. If the guide fixes width and allows height to vary, calculate `height = declared width × viewBox height ÷ viewBox width`; if height is fixed and width varies, use the inverse calculation. If both dimensions are fixed, preserve both and adapt the canvas/layout without stretching the artwork. Content edits within an unchanged canvas do not require dimension changes.
- Verify the saved asset's resulting physical size and aspect ratio after these edits. Keep PDF page dimensions and raster resolution metadata consistent when generating exports within the requested scope; do not assume internal SVG transforms or unitless pixel dimensions establish the intended print size.
- Card page PNG assets, including source art, must be 3300 × 2550 px. Card PDFs must render at 11 × 8.5 inches per page.
- Hero board PNG assets, including source art, must be 4500 × 2700 px. Hero board PDFs must render at 15 × 9 inches per page.
- Hero art PNG assets must be 1500 × 2700 px. Hero art PDFs must render at 5 × 9 inches per page.
- Nameplate PNG assets must be 402 × 1665 px. Nameplate PDFs must render at 1.3386 × 5.5512 inches per page.
- Leaflet PNG assets, including source art, must be 1350 × 2550 px. Leaflet PDFs must render at 4.5 × 8.5 inches per page.
- The expected effective print resolution for all raster assets is 300 dpi at their intended physical size. Keep vector PDF content vector where possible; raster content in PDFs must retain 300 dpi effective resolution at final print size.
- When inspecting or preparing assets, check their pixel dimensions, PDF page size, and effective DPI against these standards. If an asset does not match an expected value, bring the discrepancy to the user's attention.

## Card types and rules coverage

- **Standard Cards** are the following shared cards: Transference!, What Status Effects?, Vegas Baby!, Get That Outta Here!, Twice as Wild!, Try, Try Again!, So Wild!, Samesies!, Triple Up!, Double Up!, Buh, Bye!, Tip It!, One More Time!, Helping Hand, Better D!, Six-It!, Getting Paid!, and Not This Time!. Their rules are the same across Dice Throne decks. Treat them as correct: do not revise their rules or edit their assets. Do not include Standard Cards in `rules.txt` at all: neither their rules text nor their CP costs need to be listed there.
- **Upgrade Cards** are cards whose title matches a hero-board ability name followed by the suffix `II` or `III` (for example, `Fire Phasers II`). Each upgrades a power on the hero board and has a full panel for its rules text. Put the upgrade rules without the CP cost in the SVG's full panel. In `rules.txt`, include the upgrade rules together with the CP cost.
- **Hero Action Cards** are any cards that are neither Standard Cards nor Upgrade Cards. These are unique to the active hero. Put their rules text without the CP cost in the SVG's rules box. In `rules.txt`, include their rules together with the CP cost. Their card layout has original artwork in the top half and a rules text box in the bottom half.
- Hero Action Cards and Upgrade Cards have CP costs recorded in `rules.txt`; Standard Cards are excluded from `rules.txt`, including their costs. In both primary and playtest app Hero Action and Upgrade Card SVGs, CP costs are hard-coded in an area outside the rules box or panel and require case-by-case attention to change. If a recorded CP cost differs from either asset version, report the mismatch to the user and wait for their correction instructions. Do not change either cost unless directed.
- `rules.txt` does not include the die breakdown area at the bottom right of the leaflet. That breakdown is hard-coded into the leaflet SVG and must remain unchanged unless the user specifically requests a change.
- For the Janeway leaflet and future updates to it, set rules text inside the black token-panel rules boxes in Avenir Next Condensed at 11 pt at the 1350 × 2550 SVG working scale. Keep the rules text left-aligned and wrap it within equal 26 px margins from the left and right interior edges of each black rules box. Preserve the black header text, including panel titles and status/stack-limit lines, in its original font and size; apply Avenir Next Condensed only to the lighter rules text.
- For leaflet token-panel headers, render the token name in Helvetica Compressed Regular at 64 px. Render the status type and stack-limit line in Avenir Next Condensed Demi Bold at 38 px. Use black text at the 1350 × 2550 SVG working scale and follow Janeway's existing header alignment, relative placement, and spacing. Align the status type and stack-limit text to a shared baseline.

## Previewing rules text

- When the user asks to **preview rules**, use `rules.txt` to create a temporary page showing how the rules text and icons will render. The preview is for proofreading the output before SVG asset updates.
- The temporary page does not need to place the rules into the actual rules boxes or panels on the assets. Focus on accurately rendering the text and icons; do not treat this request as authorization to update primary or playtest app assets.
- Save the temporary preview in a Codex-provided writable workspace outside this project. Keep the preview temporary unless the user asks otherwise.
- When previewing or updating rules, reproduce the wording and punctuation in `rules.txt` exactly. Preserve numerals as numerals; do not spell them out. Carry forward every punctuation mark.

## Updating assets from rules text

- When the user asks to update an asset from `rules.txt`, first compare both the current primary SVG and the corresponding saved playtest app SVG with `rules.txt`. This first step is read-only: report what matches and what needs updating in each version, including any differences between the two versions. Get the user's approval to proceed before preparing any changes.
- Identify the exact primary and playtest app asset paths for the active hero. The app assets live under `playtest-app/public/assets/`, normally mirroring the hero's project-relative paths. Inspect and freshly render the actual saved SVGs directly from disk, plus any existing primary PDF that will be updated. Do not rely on earlier previews, thumbnails, or cached renders. Verify disputed text in the actual saved SVG before reporting a mismatch. If a corresponding app asset is missing or its mapping is unclear, report that and ask for direction before creating or substituting an asset.
- After approval to proceed, back up every existing file this process may change, including both versions' SVGs and any affected PDF or app export. Keep these working backups in a Codex-provided writable workspace outside this project until the entire process receives final approval.
- Prepare revised primary and playtest app SVGs only as temporary files in a Codex-provided writable workspace outside this project. Edit the rules directly in each SVG, preserving each version's formatting, spacing, alignment, artwork, and resource references. Do not modify saved project or app assets during preparation. Keep the app assets self-contained; do not replace them wholesale with primary SVGs or introduce dependencies outside the app. Make corresponding rules changes in both versions without overwriting unrelated differences.
- When placing a die face icon whose primary color is not black in an SVG, give the icon a 1 px rounded-edge inner border in a lighter shade of that die face's primary color, surrounded by a 1 px rounded-edge outer border in black. In most cases, choose the lighter shade by examining the borders around die faces in previous versions of the asset in question.
- When multiple die face icons appear in a row, make them all the same size and height, and space them so their borders touch without overlapping.
- When placing an icon within a line of text, vertically center the icon against that line of text.
- When adding rules text to hero board or card SVGs, use Avenir Next Condensed Regular at 9 pt. Render any icon placed inline with that text at the same point size as the text in that context.
- In rules text on hero board, card, Upgrade Card, and leaflet SVGs, capitalize these phase names exactly as “Main Phase,” “Offensive Roll Phase,” and “Defensive Roll Phase.” Render “Main Phase” in blue RGB `(51, 106, 156)` (`#336A9C`), sampled from the Main Phase Action CP badges in the Janeway cards PDF. Render “Offensive Roll Phase” and “Defensive Roll Phase” in orange RGB `(235, 148, 58)` (`#EB943A`), sampled from the Roll Phase Action CP tags in the Janeway cards PDF.
- When adding text or icons to hero board, card, or Upgrade Card SVGs, apply a black radial halo shadow around each text glyph or icon. Match the shadow treatment in the approved Janeway hero board SVG at the same working scale: sample its reach, darkness, softness, and centered placement, then reproduce those qualities with a smooth fade and no directional offset. Build each shadow mask from the visible glyph or icon silhouette, not a rectangular source-image canvas, and pad it before filtering so the halo is not clipped at mask, word, row, or canvas edges and extends consistently left, right, up, and down. For a repeatable starting point, use pure black at up to about 80% peak opacity, expand the silhouette mask by about 15% of that glyph or icon's visible height, then apply a Gaussian blur with a radius about 12% of its visible height; let the halo fade smoothly to transparent. Scale these proportions with the rendered glyph/icon size, then tune only as needed to match the approved Janeway treatment. Composite the halo behind the foreground glyph/icon so white pixels stay crisp and unobscured. For white text or icons on transparent SVG backgrounds, preview the SVG composited over a bright, varied test backdrop so the dark halo can be judged against light pixels; a black viewer background hides a black halo and is not sufficient for visual approval.
- Center rules text on hero boards and cards within its panel. The exception is the three rules rows beneath a panel’s three top rows of die face icons; those three rows may follow their established layout.
- For each changed card or panel, create a four-panel comparison preview in PDF format in a Codex-provided writable workspace outside this project. Use a clearly labeled 2 × 2 grid: original primary at top left, revised primary at top right, original playtest app at bottom left, and revised playtest app at bottom right. Render originals from the actual saved SVGs and revisions from the temporary SVGs. Show the same card or panel in all four positions, at matching visual scale. If only one version needs a change, show the unchanged version in both of its positions. Present comparisons one at a time and wait for approval of both versions before presenting the next comparison.
- Keep all comparison previews temporary. After the user approves every changed card or panel, create complete previews of both versions from the temporary SVGs, including unchanged pages or assets in the requested update scope. Assemble the primary asset into a PDF preview where applicable and show the complete playtest app asset set as well. Wait for approval of both complete versions before replacing any saved SVGs or exports.
- After that approval, replace only the affected primary and playtest app SVGs with their approved revisions, and replace any affected primary PDF with its approved full-asset preview PDF. Update existing app exports only when required by the app's asset workflow and included in the approved scope. Check alignment and resource references after replacement.
- Reopen and freshly render the saved primary SVGs, any replaced primary PDF, and the saved playtest app assets. Verify the app loads its updated assets correctly. Show the saved results from both versions for one final approval so the user can confirm the replacements worked correctly.
- Only after the user approves both saved versions at this final check may you delete the backups and temporary files created for this update from the external Codex workspace. Preserve unrelated or pre-existing files there. If the user rejects any preview, keep all backups and temporary files, pause at that stage, and wait for instructions to revise the preview or restore the backup. Do not continue to the next stage or clean up those files until directed.
- If a CP cost differs between `rules.txt` and either asset version, report the mismatch and wait for the user's correction instructions; do not change any cost on your own.
- Do not edit the large status-token emblems on the leaflet as part of a `rules.txt` or asset update. They are separate design elements and should remain as they are unless the user explicitly directs a change to them.

### Comparison checklist

- Compare each affected rules line with `rules.txt`, preserving the exact wording, capitalization, numerals, punctuation, and icon order.
- Compare the updated text with the original asset's styling and placement. Check boldness, font size, line breaks, alignment, spacing, and drop shadows, matching shadows already used in the corresponding SVG or on white text.
- Confirm the requested changes are present in both the primary and playtest app assets, both match `rules.txt`, and unrelated text and artwork remain unchanged. Verify saved SVGs and exports with fresh renders, and confirm the playtest app resolves its asset references.

## Hero-root filenames

Follow the established Janeway naming pattern for final assets. Use descriptive lowercase names with underscores and keep each asset's filename stem consistent across related files. Examples include:

- `cards.pdf` (and the corresponding primary SVG files)
- `hero_art.pdf`
- `hero_board.pdf`
- `leaflet.pdf`
- `nameplate.pdf`
- `rules.txt`

Do not add a hero-name prefix to files already contained in that hero's folder. Preserve extensions and page-number suffixes, and keep each file in the subfolder matching its purpose.
