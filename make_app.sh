#!/bin/bash
# Creates CoffeeBuddy.app in ~/Applications so it appears in Spotlight.
# Re-run this if you move the project or change your Python install.

set -e

PYTHON="$(which python3)"
PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
APP="$HOME/Applications/CoffeeBuddy.app"

echo "Python:  $PYTHON"
echo "Project: $PROJECT_DIR"
echo "App:     $APP"

mkdir -p "$APP/Contents/MacOS"
mkdir -p "$APP/Contents/Resources"

# ── Info.plist ────────────────────────────────────────────────────────────────
cat > "$APP/Contents/Info.plist" << 'PLIST'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleName</key>
    <string>Coffee Buddy</string>
    <key>CFBundleDisplayName</key>
    <string>Coffee Buddy</string>
    <key>CFBundleIdentifier</key>
    <string>com.coffeebuddy.app</string>
    <key>CFBundleVersion</key>
    <string>1.0</string>
    <key>CFBundleExecutable</key>
    <string>CoffeeBuddy</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>LSUIElement</key>
    <true/>
    <key>NSHighResolutionCapable</key>
    <true/>
</dict>
</plist>
PLIST

# ── Launcher (bake in Python + project paths) ─────────────────────────────────
cat > "$APP/Contents/MacOS/CoffeeBuddy" << LAUNCHER
#!/bin/bash
exec "$PYTHON" "$PROJECT_DIR/app.py"
LAUNCHER

chmod +x "$APP/Contents/MacOS/CoffeeBuddy"

# Tell Spotlight to re-index the bundle
touch "$APP"

echo ""
echo "Done! Search 'Coffee Buddy' in Spotlight to launch."
