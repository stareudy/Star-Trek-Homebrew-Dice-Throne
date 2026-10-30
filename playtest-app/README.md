# Voyager Dice Throne — local playtest prototype

A single-hero, offline-first manual tabletop for **Janeway** and **Tuvok**. All changes for this application live under `playtest-app/`. The source files in `Heroes/` and `Shared/` are read-only build inputs.

## Development (Mac)

Requires Node.js 20+. From the repository root:

```sh
cd playtest-app
npm install
npm run dev
```

Open the local URL printed by Vite. No hosting or network connection is required for gameplay. The initial `npm install` requires downloading developer dependencies. `npm run build` creates a self-contained `dist/` bundle with the art copied from the repository. It does not edit the source art.

## Native apps (planned next step)

```sh
npm run build
npx cap add android
npx cap add ios
npx cap sync
```

Open `ios/App/App.xcworkspace` in Xcode to sign/install on your own iPhone or iPad. Android Studio can build an installable APK from `android/`. These native platform folders are generated inside `playtest-app/`; they are not included in this first commit. Android/iOS SDK tooling is needed for native builds.

## Implemented prototype

* Hero selector; Janeway and Tuvok boards and dice face SVGs.
* Five independently lockable dice, reroll unlocked dice, tap a die to set 1–6 manually.
* Randomized 32-card deck (14 hero-specific + 18 shared), draw, inspect hand, discard, reshuffle discard, peek top 1–3 and reorder or move cards to bottom.
* Upgrade cards can be played to an ability slot, tracked in the upgrade list and displayed as an overlay in the board viewer.
* Manual health, CP, and hero-specific status token counters.
* Local session persistence, new-session reset.

## Limitations / validation needed

* The 18 shared named card SVGs are each included once. Confirm this matches the intended printed deck and any duplicate card quantities.
* Upgrade targets are mapped by filename. Precise ability-panel overlay coordinates have **not** yet been calibrated to the actual hero-board SVGs; the prototype shows a tappable upgrade badge and a separate upgrade-card viewer instead of claiming pixel-perfect placement.
* No rules enforcement, CP deductions, damage automation, multiplayer, accounts, or servers.
* The local dev server is only a development tool; packaged native builds use bundled assets.
* Check card artwork and fonts on actual iPhone/Android hardware before distributing.
