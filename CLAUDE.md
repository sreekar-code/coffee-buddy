# Coffee Buddy — Agent Instructions

## Overview

Single-file macOS menubar app (`app.py`, ~4900 lines). Shows specialty coffee education snippets via a floating popup. Built with Python + rumps + PyObjC.

## Running the app

```bash
python3 app.py
```

Or from Spotlight after running `bash make_app.sh` once.

## Key architecture

### Data
- `SNIPPETS` — list of 502 dicts `{category, text}`, lines 15–4731

### Classes (all in app.py)
| Class | Purpose |
|---|---|
| `ParchmentView(NSView)` | Warm cream background (SRGB 0.99, 0.96, 0.90) |
| `SnippetViewController(NSViewController)` | Popup content: category label, text, "One more cup" button |
| `ClickHandler(NSObject)` | Receives status bar button click → calls `toggle_popover()` |
| `CoffeeBuddyApp(rumps.App)` | Main app; owns the NSPanel popup and snippet deck |

### Popup window
- `NSPanel` with `NSWindowStyleMaskNonactivatingPanel` (1<<7) — floats above all windows including full-screen apps without stealing focus
- Level: `NSPopUpMenuWindowLevel` set at creation time
- Collection behavior: `1 | 8 | 256` = CanJoinAllSpaces | Transient | FullScreenAuxiliary
  - `FullScreenAuxiliary` (256) is required to appear in full-screen Spaces
- Auto-dismiss: global `NSEvent` mouse monitor; ignores clicks on the status bar button to avoid toggle race condition
- **Do NOT use NSPopover** — it manages its own window level internally and cannot reliably appear above full-screen apps

### Snippet deck
Shuffled list of all indices; pops one at a time; reshuffles when exhausted. Ensures all 502 snippets are seen before any repeats.

### Deferred wiring
`NSStatusItem` doesn't exist until `rumps.App.run()` is called. The click handler is attached via `rumps.events.before_start`.

## Spotlight launch (make_app.sh)

Creates `~/Applications/CoffeeBuddy.app`. Key steps:
1. `osacompile` — creates bundle with Apple-signed `applet` binary (Gatekeeper-trusted)
2. PlistBuddy — patches `LSUIElement=true`, bundle name, identifier
3. `codesign --force --deep --sign -` — re-signs to cover the patched plist

Plain shell-script bundles are rejected by Gatekeeper on macOS Sequoia — always use `osacompile`.

## UI theme
- Background: parchment (SRGB 0.99, 0.96, 0.90)
- Brown accent: SRGB 0.55, 0.30, 0.08
- Dark text: SRGB 0.15, 0.07, 0.02
- Popup size: 300×190 px
- Fonts: category 10pt system, body 12pt system
