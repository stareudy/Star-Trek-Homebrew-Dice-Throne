# Manual cloud builds

The three GitHub Actions workflows are intentionally **manual only** (`workflow_dispatch`).
They do not run on pushes, pull requests, or a schedule.

After the web app and SVG rendering are finalized, open GitHub > Actions and choose:
- **Playtest Android APK (manual)** for an installable debug APK.
- **Playtest iOS unsigned IPA (manual)** for an unsigned IPA to upload to Signulous for signing. The IPA is not directly installable without signing; each device must be eligible with the signing service.
- **Playtest macOS app (manual)** for a macOS .app and possibly .dmg (unsigned/unnotarized). Gatekeeper may warn when opening it.

Select **Run workflow** when ready. Download the resulting artifact from the workflow run.

These are untested build recipes until their first manual run. The app source remains entirely within `playtest-app/`; the only repository-root changes are the three GitHub Actions workflow files. No signing credentials are stored or required for these builds.
