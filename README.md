# ☕ Coffee Buddy

A lightweight macOS menubar app that teaches you specialty coffee in short, friendly snippets.

## What it does

- Sits in your menubar as a ☕ icon
- Shows a coffee fact or tip (with category label) each time you open it
- Click **Next →** to cycle through all 50 snippets in random order — it reshuffles once you've seen them all
- Covers: espresso, pour over, French press, AeroPress, cold brew, tasting, roasting, origins, processing, grind size, water, beginner tips, and fun facts

## Requirements

- macOS (10.14+)
- Python 3.8+

## Setup & launch

```bash
# 1. Install the dependency
pip install rumps

# 2. Run the app
python app.py
```

The ☕ icon will appear in your menubar immediately.

> **Tip:** On macOS Ventura+, you may need to grant Accessibility or Automation permissions the first time you run it. Follow the system prompt if one appears.

## Project structure

```
coffee-buddy/
├── app.py           # Main app
├── requirements.txt # Python dependencies
└── README.md        # This file
```

## Running as a background app (optional)

To keep it running without a terminal window:

```bash
nohup python app.py &>/dev/null &
```

To stop it, click **Quit** in the menubar dropdown.
