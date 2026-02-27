#!/bin/bash
# Creates CoffeeBuddy.app in ~/Applications so it appears in Spotlight.
# Uses osacompile so the applet binary is Apple-signed, then patches the
# Info.plist and re-signs so Gatekeeper accepts it.
# Re-run this if you move the project or change your Python install.

set -e

PYTHON="$(which python3)"
PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
APP="$HOME/Applications/CoffeeBuddy.app"
PLIST="$APP/Contents/Info.plist"

echo "Python:  $PYTHON"
echo "Project: $PROJECT_DIR"
echo "App:     $APP"

mkdir -p "$HOME/Applications"
rm -rf "$APP"

# ── 1. Compile AppleScript launcher (gets Apple-signed applet binary) ─────────
TMPSCRIPT=$(mktemp /tmp/coffeebuddy_XXXXXX.applescript)
cat > "$TMPSCRIPT" << APPLESCRIPT
do shell script "pgrep -qf '$PROJECT_DIR/app.py' || (nohup '$PYTHON' '$PROJECT_DIR/app.py' > /tmp/coffeebuddy.log 2>&1 &)"
APPLESCRIPT

osacompile -o "$APP" "$TMPSCRIPT"
rm "$TMPSCRIPT"

# ── 2. Patch Info.plist keys (before re-signing) ──────────────────────────────
PB="/usr/libexec/PlistBuddy"
set_key() { "$PB" -c "Set :$1 $2" "$PLIST" 2>/dev/null || "$PB" -c "Add :$1 $3 $2" "$PLIST"; }

set_key CFBundleName          "Coffee Buddy"  string
set_key CFBundleDisplayName   "Coffee Buddy"  string
set_key CFBundleIdentifier    "com.coffeebuddy.app" string
set_key CFBundleVersion       "1.0"           string
set_key LSUIElement           true            bool
set_key NSHighResolutionCapable true          bool

# ── 3. Re-sign the whole bundle so the patched plist is covered ───────────────
codesign --force --deep --sign - "$APP"

# ── 4. Tell Spotlight to re-index ─────────────────────────────────────────────
touch "$APP"

echo ""
echo "Done! Search 'Coffee Buddy' in Spotlight to launch."
