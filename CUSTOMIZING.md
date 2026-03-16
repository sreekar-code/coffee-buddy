# Customizing This App — Agent Instructions

This file is written for both humans and AI coding agents (e.g. Claude Code). If you are an AI agent and the user has told you what topic they want (books, wine, stoicism, chess, language learning, etc.), read this file in full and then carry out every step described. Do not ask clarifying questions unless a required value is genuinely ambiguous. Make all changes in a single pass.

---

## What this app is

A macOS menubar app that shows short educational snippets on a topic, one at a time, in a floating popup. The user clicks the menubar icon to see a snippet and clicks "One more cup ☕️" to advance.

Everything is in one file: `app.py`. Customizing the app means editing `app.py` (and optionally `make_app.sh`). No other files need to change for a basic customization.

---

## The five things you customize

| # | What | Where in app.py | Effort |
|---|------|-----------------|--------|
| 1 | Snippets (the content) | `SNIPPETS` list, lines 15–~902 | High — write 80–100 new snippets |
| 2 | Menubar icon | `super().__init__("☕", ...)` | Trivial — swap one emoji |
| 3 | "Next" button label | `"One more cup ☕️"` string in `loadView` | Trivial — one string |
| 4 | Color theme | three SRGB color constants in `loadView` + `drawRect_` | Low — change ~4 color values |
| 5 | App bundle name | `make_app.sh` (APP_NAME, bundle id) | Low — two strings |

---

## Step-by-step instructions for AI agents

### Step 1 — Determine the topic and its subcategories

Before writing any code, decide on:

- **Topic name** — e.g. "Wine Tasting", "Book Appreciation", "Stoic Philosophy", "Chess Strategy"
- **Subcategories** — 8–12 subcategories that carve the topic into meaningful areas. Good subcategories are specific enough to feel educational but broad enough to yield 7–10 snippets each.

**Examples:**

| Topic | Example subcategories |
|-------|-----------------------|
| Wine Tasting | Aroma, Tannins, Acidity, Body, Finish, Terroir, Grape Varieties, Food Pairing, How to Taste |
| Books | Genre, Narrative Voice, Character, Plot, Themes, Style, How to Read Closely, Building a Reading Habit |
| Stoicism | Dichotomy of Control, Virtue, Daily Practice, Emotions, Resilience, Key Figures, Core Texts |
| Chess | Openings, Tactics, Strategy, Endgames, Piece Values, Time Management, Study Habits |
| Language Learning | Vocabulary, Grammar, Listening, Speaking, Reading, Writing, Immersion, Motivation |

Choose subcategories that reflect real depth in the topic — not just surface labels.

---

### Step 2 — Write the SNIPPETS list

Replace the entire `SNIPPETS` list (everything from line 15 to the closing `]` before the class definitions) with new content.

**Format — each snippet is a dict:**

```python
{
    "category": "<Topic> · <Subcategory>",
    "text": (
        "The snippet text goes here. It should be two to four sentences. "
        "Keep it tight — the popup text area fits about six lines at 12pt. "
        "Aim for roughly 200–280 characters of body text."
    ),
},
```

**Mandatory rules for every snippet:**

1. `"category"` must follow the pattern `"<Topic> · <Subcategory>"` — the dot-separator (` · `) is the visual divider shown in the popup. Use the same Topic name across all snippets.
2. `"text"` must be 2–4 sentences. Never more than ~280 characters. The popup text area is fixed at 300×102 px at 12pt; text that is too long will be cut off visually.
3. Each snippet must be self-contained — no references to "the previous tip" or "as mentioned".
4. Write factual, educational content. No filler. Each snippet should teach one concrete, specific thing.
5. Group snippets by subcategory in the list (use a comment header for each group: `# ── Subcategory ──`). Within a group, order from foundational to nuanced.
6. Aim for **at least 80 snippets** total, ideally 100. More is better — the deck reshuffles only when exhausted.
7. Distribute snippets roughly evenly across subcategories (7–10 per subcategory). Avoid making one subcategory dominate.

**Good snippet (Wine — Tannins):**
```python
{
    "category": "Wine Tasting · Tannins",
    "text": (
        "Tannins are polyphenols found in grape skins, seeds, and stems. They "
        "create that drying, grippy sensation on your gums. Red wines have far "
        "more tannins than whites — skin contact during fermentation is the reason."
    ),
},
```

**Bad snippet (too long, will overflow):**
```python
{
    "category": "Wine Tasting · Tannins",
    "text": (
        "Tannins are polyphenols found in grape skins, seeds, stems, and oak barrels. "
        "They create a drying, astringent sensation on your gums and the inside of your "
        "cheeks. Red wines have far more tannins than whites because of skin contact "
        "during fermentation. Tannins also act as a natural preservative, which is why "
        "tannic wines can age for decades. Cabernet Sauvignon and Nebbiolo are among "
        "the most tannic grapes."
    ),
},
```

---

### Step 3 — Update the menubar icon

Find this line near the bottom of `app.py`:

```python
super().__init__("☕", quit_button=None)
```

Replace the `"☕"` emoji with a single emoji that fits the new topic. One character only — the status bar button is small.

**Suggestions:**

| Topic | Icon |
|-------|------|
| Wine | 🍷 |
| Books | 📖 |
| Chess | ♟️ |
| Stoicism / Philosophy | 🏛️ |
| Language Learning | 🗣️ |
| Music | 🎵 |
| Cooking | 🍳 |
| Fitness | 💪 |
| Astronomy | 🔭 |
| History | 📜 |

---

### Step 4 — Update the "Next" button label

Find this string in `loadView` inside `SnippetViewController`:

```python
"One more cup ☕️",
```

Replace it with something that fits the new topic. Keep it short — the button frame is 122 px wide at 12pt. Around 15–18 characters is the safe maximum.

**Examples:**

| Topic | Button label |
|-------|-------------|
| Wine | `"Next pour 🍷"` |
| Books | `"Next page 📖"` |
| Chess | `"Next move ♟️"` |
| Stoicism | `"Next thought 🏛️"` |
| Language | `"Next word 🗣️"` |
| Cooking | `"Next tip 🍳"` |

---

### Step 5 — Update the color theme

There are three color roles used throughout the popup. All are defined in `loadView` and `drawRect_`. Change them to match the topic's mood.

**The three roles:**

| Role | Current value (Coffee) | Where it appears |
|------|----------------------|-----------------|
| Background fill | SRGB `0.99, 0.96, 0.90` (warm parchment) | `ParchmentView.drawRect_` |
| Accent color | SRGB `0.55, 0.30, 0.08` (brown) | Category label, button text |
| Body text color | SRGB `0.15, 0.07, 0.02` (near-black warm) | Snippet text field |

**How to find them in code:**

The background color is in `ParchmentView.drawRect_`:
```python
NSColor.colorWithSRGBRed_green_blue_alpha_(0.99, 0.96, 0.90, 1.0).set()
```

The accent and body text colors appear in `SnippetViewController.loadView`:
```python
# accent (category label)
NSColor.colorWithSRGBRed_green_blue_alpha_(0.55, 0.30, 0.08, 1.0)

# body text
NSColor.colorWithSRGBRed_green_blue_alpha_(0.15, 0.07, 0.02, 1.0)

# button text (same brown variable)
brown = NSColor.colorWithSRGBRed_green_blue_alpha_(0.55, 0.30, 0.08, 1.0)
```

**Suggested palettes by topic:**

| Topic | Background (SRGB) | Accent (SRGB) | Body text (SRGB) |
|-------|-------------------|---------------|-----------------|
| Wine | `0.98, 0.95, 0.96` (blush) | `0.55, 0.10, 0.20` (deep red) | `0.18, 0.05, 0.08` |
| Books | `0.97, 0.96, 0.91` (aged paper) | `0.30, 0.20, 0.10` (dark tan) | `0.10, 0.08, 0.05` |
| Chess | `0.96, 0.96, 0.96` (off-white) | `0.15, 0.15, 0.15` (near-black) | `0.10, 0.10, 0.10` |
| Stoicism | `0.95, 0.94, 0.90` (stone) | `0.35, 0.30, 0.20` (marble) | `0.12, 0.10, 0.06` |
| Language | `0.94, 0.96, 0.99` (pale blue) | `0.15, 0.35, 0.65` (ink blue) | `0.06, 0.12, 0.22` |
| Cooking | `0.99, 0.97, 0.93` (warm white) | `0.65, 0.25, 0.10` (terracotta) | `0.15, 0.08, 0.04` |
| Fitness | `0.95, 0.98, 0.95` (pale green) | `0.15, 0.45, 0.20` (forest) | `0.06, 0.15, 0.08` |
| Music | `0.96, 0.94, 0.99` (pale violet) | `0.35, 0.15, 0.55` (purple) | `0.12, 0.06, 0.18` |

If the user specifies a color or mood, derive SRGB values from it (all values 0.0–1.0; alpha is always 1.0). The body text color should always be a very dark version of the accent hue for readability.

---

### Step 6 — Update make_app.sh (optional, but recommended)

If the user wants to launch from Spotlight, update the bundle name in `make_app.sh`.

Find these two lines near the top:
```bash
APP_NAME="CoffeeBuddy"
BUNDLE_ID="com.local.coffeebuddy"
```

Change them to match the new app. Use PascalCase for `APP_NAME` (no spaces), lowercase dotted reverse-domain for `BUNDLE_ID`.

**Examples:**

| Topic | APP_NAME | BUNDLE_ID |
|-------|----------|-----------|
| Wine | `WineBuddy` | `com.local.winebuddy` |
| Books | `BookBuddy` | `com.local.bookbuddy` |
| Chess | `ChessBuddy` | `com.local.chessbuddy` |

The Spotlight search phrase becomes whatever the user types to find it — they'll type the APP_NAME (lowercased, spaced). No other changes to `make_app.sh` are needed.

---

### Step 7 — Update the class name (optional)

The main class is named `CoffeeBuddyApp`. If the user cares about code cleanliness, rename it at both the class definition and the instantiation at the bottom:

```python
# definition
class CoffeeBuddyApp(rumps.App):  →  class WineBuddyApp(rumps.App):

# instantiation (last two lines)
if __name__ == "__main__":
    CoffeeBuddyApp().run()  →  WineBuddyApp().run()
```

This is purely cosmetic and does not affect runtime behavior. Only do this if the user asked or if it makes the code noticeably cleaner.

---

## What NOT to change

Do not modify anything in the popup window architecture section of `CoffeeBuddyApp.__init__` — the `NSPanel` setup, `setLevel_`, `setCollectionBehavior_`, and the global `NSEvent` mouse monitor. These are non-obvious PyObjC requirements for the popup to appear above full-screen apps. Changing them will break the app in subtle ways (popup appears on wrong screen, disappears behind full-screen windows, steals focus, etc.). Leave them exactly as they are.

Do not change the popup size (`W, H = 300, 190`) unless the user explicitly asks. The snippet text area height (`H - 88 = 102 px`) is sized for exactly ~6 lines of 12pt text. If you change the size, adjust the subview frames in `loadView` proportionally.

---

## Verification checklist

After making all changes, confirm:

- [ ] Every snippet's `"category"` follows `"<Topic> · <Subcategory>"` with a consistent Topic name
- [ ] No snippet's `"text"` exceeds ~280 characters (count if unsure)
- [ ] There are at least 80 snippets total
- [ ] Subcategories are distributed — no single subcategory has more than 15 snippets
- [ ] The menubar icon is a single emoji character
- [ ] The button label fits in ~18 characters
- [ ] The `SNIPPETS` list closes with `]` followed by two blank lines before the class definitions
- [ ] The app still runs: `python3 app.py`

---

## Minimal example — full topic swap

If the user says something like *"customize this for wine tasting"*, your output should be:

1. A revised `SNIPPETS` list in `app.py` (80–100 wine tasting snippets across 8–12 subcategories)
2. Updated menubar icon (`🍷`)
3. Updated button label (`"Next pour 🍷"`)
4. Updated color theme (blush background, deep red accent)
5. Updated `make_app.sh` bundle name (`WineBuddy`, `com.local.winebuddy`)
6. Optionally rename `CoffeeBuddyApp` → `WineBuddyApp`

Do all of this in a single response. Do not ask the user to confirm intermediate steps unless a specific value (like the exact subcategory list) is genuinely ambiguous and the user has given no indication of their preference.
