# ☕ Coffee Buddy

A lightweight macOS menubar app that teaches you specialty coffee in short, friendly snippets.

## What it does

- Sits in your menubar as a ☕ icon
- Click it to see a coffee tasting tip (category + text) in a floating popup
- Click **One more cup ☕️** to cycle through all 100 snippets in random order — reshuffles when exhausted
- Popup floats above all windows, including full-screen apps — no need to minimize anything
- Covers: acidity, body, sweetness, aftertaste, aroma, balance, bitterness, flavor notes, mouthfeel, comparing coffees, and how to taste

## Requirements

- macOS 12+
- Python 3.9+
- `rumps` and `pyobjc` (PyObjC ships with the macOS Python from Command Line Tools)

## Setup

```bash
pip install rumps
```

## Launch options

### Option A — Spotlight (recommended)

Run once to install the app bundle:

```bash
bash make_app.sh
```

Then launch anytime with `Cmd+Space` → "coffee buddy" → `Enter`. No terminal needed.

> Re-run `make_app.sh` if you move the project folder or change your Python install.

### Option B — Terminal

```bash
python3 app.py
```

## Project structure

```
coffee-buddy/
├── app.py           # Entire app (~1100 lines, includes 100 SNIPPETS)
├── make_app.sh      # One-time installer: creates ~/Applications/CoffeeBuddy.app
├── requirements.txt # Python dependencies
└── README.md        # This file
```
