# Voyager Dice Throne playtest app

This folder is self-contained. Its source code and all 64 required SVGs live here, under `public/assets/`. The SVGs are independent copies of the originals: PNG artwork was replaced with solid black vector rectangles, while vector paths and editable text remain. No fonts or PNG files are required from outside this folder.

Run `npm install` and `npm run dev` from `playtest-app/`. Build with `npm run build` and sync Capacitor with `npm run sync`. A network connection is needed for initial npm dependency installation, but not for the bundled app's runtime.

The original project files outside `playtest-app/` are not modified.
