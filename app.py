import random
import objc
import rumps
from AppKit import (
    NSObject, NSPopover, NSViewController, NSView,
    NSTextField, NSButton, NSColor, NSFont, NSBezierPath,
    NSMakeRect, NSPopoverBehaviorTransient,
    NSTextAlignmentLeft, NSForegroundColorAttributeName, NSFontAttributeName,
)
from Foundation import NSMakeSize, NSAttributedString

# NSRectEdge.maxY — popover opens downward from the menu bar
NSMaxYEdge = 3

SNIPPETS = [
    # ── Brewing · Espresso ──────────────────────────────────────────────────
    {
        "category": "Brewing · Espresso",
        "text": (
            "Espresso is brewed by pushing hot water (around 93 °C / 200 °F) through "
            "finely-ground coffee at high pressure — typically 9 bars. The result is a "
            "concentrated shot with a rich layer of crema on top. That crema is actually "
            "emulsified oils and CO₂, a sign of fresh coffee."
        ),
    },
    {
        "category": "Brewing · Espresso",
        "text": (
            "A standard espresso shot is about 18–20 g of ground coffee extracted into "
            "36–40 g of liquid in roughly 25–30 seconds. This 1:2 ratio is a great "
            "starting point. If your shot pulls too fast it'll taste sour; too slow and "
            "it'll taste bitter."
        ),
    },
    {
        "category": "Brewing · Espresso",
        "text": (
            "Tamping — pressing the ground coffee into the portafilter basket — matters "
            "more than most beginners expect. Aim for about 15–20 kg of even, level "
            "pressure. An uneven tamp causes water to channel through weak spots, "
            "producing an uneven extraction."
        ),
    },
    # ── Brewing · Pour Over ─────────────────────────────────────────────────
    {
        "category": "Brewing · Pour Over",
        "text": (
            "Pour over coffee (Chemex, V60, Kalita Wave) lets you control every variable: "
            "water temperature, pour speed, and bloom time. Start with a 30-second bloom "
            "— pour just enough water to wet all the grounds and let CO₂ escape. This "
            "prepares the coffee for a more even extraction."
        ),
    },
    {
        "category": "Brewing · Pour Over",
        "text": (
            "For a V60, pour in slow, steady circles from the center outward. This "
            "agitates the bed evenly and prevents dry pockets. A gooseneck kettle gives "
            "you far more precision than a standard kettle — the flow rate is easier "
            "to control."
        ),
    },
    {
        "category": "Brewing · Pour Over",
        "text": (
            "A good starting ratio for pour over is 1 g of coffee per 15–16 g of water "
            "(roughly 1:15 to 1:16). Total brew time for a V60 should land around "
            "3–4 minutes. Adjust grind size first if things are too fast or slow before "
            "changing anything else."
        ),
    },
    # ── Brewing · French Press ──────────────────────────────────────────────
    {
        "category": "Brewing · French Press",
        "text": (
            "French press uses immersion brewing — the grounds sit in hot water for the "
            "entire brew time (~4 minutes). This produces a full-bodied, heavy cup because "
            "the metal filter lets oils and fine particles through, unlike a paper filter "
            "which traps them."
        ),
    },
    {
        "category": "Brewing · French Press",
        "text": (
            "Don't plunge the French press too aggressively — press slowly and steadily. "
            "Then pour all the coffee out immediately. If you leave it sitting on the "
            "grounds, extraction keeps going and the cup turns bitter and muddy."
        ),
    },
    {
        "category": "Brewing · French Press",
        "text": (
            "Use a coarse grind for French press — think breadcrumbs, not table salt. "
            "Fine grounds slip through the mesh filter, making the cup gritty and causing "
            "over-extraction. Coarser grinds also make pressing much easier."
        ),
    },
    # ── Brewing · AeroPress ─────────────────────────────────────────────────
    {
        "category": "Brewing · AeroPress",
        "text": (
            "The AeroPress is incredibly versatile — you can brew espresso-style "
            "concentrates or clean, filter-style cups depending on grind size and steep "
            "time. It's also nearly impossible to break and great for travel. Specialty "
            "coffee nerds love it for how forgiving it is."
        ),
    },
    {
        "category": "Brewing · AeroPress",
        "text": (
            "Try the inverted AeroPress method: flip it upside-down, add coffee and water, "
            "steep for 1–2 minutes, then flip onto your cup and press. This prevents "
            "drip-through during steeping, giving you more control over contact time."
        ),
    },
    {
        "category": "Brewing · AeroPress",
        "text": (
            "AeroPress World Championship recipes use wildly different approaches — some "
            "use ice-cold water, some use extra fine grinds, some steep for 30 seconds. "
            "The takeaway: experiment freely. There's no single 'right' way, and the "
            "AeroPress is forgiving enough to reward curiosity."
        ),
    },
    # ── Brewing · Cold Brew ─────────────────────────────────────────────────
    {
        "category": "Brewing · Cold Brew",
        "text": (
            "Cold brew is made by steeping coarsely-ground coffee in cold or room-"
            "temperature water for 12–24 hours. The slow extraction produces a smooth, "
            "low-acid concentrate. Since no heat is used, the volatile acidic compounds "
            "never develop — making it gentler on the stomach."
        ),
    },
    {
        "category": "Brewing · Cold Brew",
        "text": (
            "A typical cold brew ratio is 1:5 to 1:8 (coffee to water) for concentrate. "
            "You then dilute it 1:1 with water or milk before drinking. Using a finer "
            "grind or steeping longer makes it stronger — just strain well to avoid "
            "a muddy result."
        ),
    },
    # ── Coffee Tasting · Acidity ────────────────────────────────────────────
    {
        "category": "Coffee Tasting · Acidity",
        "text": (
            "In specialty coffee, 'acidity' is a good thing — it's the bright, lively "
            "quality that makes a cup feel vibrant rather than flat. Think of the "
            "pleasant tartness of a ripe apple or citrus fruit. Ethiopian coffees are "
            "celebrated for their bright, wine-like acidity."
        ),
    },
    {
        "category": "Coffee Tasting · Acidity",
        "text": (
            "Acidity decreases as roast level increases. A light roast from Ethiopia "
            "might taste like lemon and blueberry; the same bean dark-roasted loses "
            "those delicate acids and tastes more chocolatey and smoky. Neither is "
            "wrong — it's just a different expression of the same seed."
        ),
    },
    # ── Coffee Tasting · Body & Sweetness ───────────────────────────────────
    {
        "category": "Coffee Tasting · Body",
        "text": (
            "'Body' describes the weight or texture of coffee in your mouth — the "
            "difference between skim milk and whole milk. French press tends to be "
            "full-bodied because oils pass through the metal filter. Pour over through "
            "paper tends to be lighter and cleaner."
        ),
    },
    {
        "category": "Coffee Tasting · Sweetness",
        "text": (
            "Well-extracted coffee is naturally sweet — no sugar needed. That sweetness "
            "comes from sugars in the bean that were caramelised during roasting. "
            "If your coffee tastes only bitter or sour, the sweetness is being masked "
            "by under- or over-extraction."
        ),
    },
    {
        "category": "Coffee Tasting · Aftertaste",
        "text": (
            "A great coffee has a pleasant aftertaste that lingers — called the 'finish.' "
            "Specialty coffees can finish with notes of caramel, dark chocolate, jasmine, "
            "or fruit. A bad finish feels harsh, drying, or disappears instantly. "
            "Sit with it for a moment after you swallow."
        ),
    },
    # ── Roasting ────────────────────────────────────────────────────────────
    {
        "category": "Roasting · Levels",
        "text": (
            "Light roasts preserve the most origin character — the flavors unique to "
            "where and how the bean was grown. They're higher in caffeine (heat destroys "
            "caffeine over time) and often taste fruity or floral. Many specialty "
            "roasters prefer light roasts precisely because they showcase the farmer's work."
        ),
    },
    {
        "category": "Roasting · Levels",
        "text": (
            "Medium roasts strike a balance: some origin character remains, but roast "
            "flavors (caramel, hazelnut, milk chocolate) start to emerge. Most "
            "supermarket 'breakfast blends' are medium roasts. They're crowd-pleasers "
            "that work well in almost any brew method."
        ),
    },
    {
        "category": "Roasting · Levels",
        "text": (
            "Dark roasts are roasted past 'second crack' — the point where the bean "
            "structure starts to break down. You'll taste roast-forward flavors: dark "
            "chocolate, smoke, bittersweet. Origin notes are mostly gone. The oils "
            "coat the bean surface, giving dark roasts their shiny appearance."
        ),
    },
    {
        "category": "Roasting · Process",
        "text": (
            "Roasting transforms green coffee (which smells like hay and tastes vegetal) "
            "into the aromatic bean we recognize. During roasting, the Maillard reaction "
            "and caramelisation create hundreds of aromatic compounds. It's similar to "
            "the chemistry that makes bread crust or seared steak taste so good."
        ),
    },
    # ── Origin & Terroir ────────────────────────────────────────────────────
    {
        "category": "Origin · Ethiopia",
        "text": (
            "Ethiopia is the birthplace of coffee — wild coffee plants still grow in its "
            "forests. Ethiopian coffees are prized for their complexity: Yirgacheffe beans "
            "often taste like jasmine tea and blueberries, while Sidama coffees lean toward "
            "citrus and peach. No two growing regions taste alike."
        ),
    },
    {
        "category": "Origin · Colombia",
        "text": (
            "Colombia's varied geography — mountains, valleys, microclimates — produces "
            "a wide range of cup profiles. Colombian coffees are often described as "
            "balanced and accessible: mild acidity, medium body, notes of red fruit and "
            "caramel. They're a great entry point into specialty coffee."
        ),
    },
    {
        "category": "Origin · Kenya",
        "text": (
            "Kenyan coffees are bold and complex with a distinct 'blackcurrant' quality "
            "that's almost savory. Kenya's SL28 and SL34 varieties are beloved by "
            "specialty roasters for their juicy, wine-like acidity. Kenyan coffee is "
            "often processed using a double-wash, which amplifies clarity."
        ),
    },
    {
        "category": "Origin · Guatemala",
        "text": (
            "Guatemala's Antigua region sits between three volcanoes at high altitude — "
            "ideal conditions for slow cherry development, which builds complexity. "
            "Guatemalan coffees often taste like dark chocolate and dried fruit, sometimes "
            "with a pleasant smoky or spice note."
        ),
    },
    {
        "category": "Origin · Terroir",
        "text": (
            "Like wine, coffee is heavily influenced by terroir — the combination of "
            "soil, altitude, rainfall, and temperature where it's grown. High-altitude "
            "farms (above 1,500 m) produce denser beans that develop more complex flavors. "
            "Volcanic soils add minerals that contribute to brightness."
        ),
    },
    # ── Processing Methods ───────────────────────────────────────────────────
    {
        "category": "Processing · Washed",
        "text": (
            "In the washed (or 'wet') process, the fruit skin is removed from the coffee "
            "cherry before drying. This produces a clean, bright cup where the bean's "
            "origin character comes through clearly. Most Ethiopian and Kenyan specialty "
            "coffees you'll find are washed processed."
        ),
    },
    {
        "category": "Processing · Natural",
        "text": (
            "Natural (or 'dry') processing leaves the whole cherry intact while it dries "
            "in the sun for weeks. The fruit sugars ferment into the bean, producing "
            "a funky, fruity, wine-like cup. Ethiopian natural coffees often taste like "
            "blueberry jam. It's polarising — some people love it, others find it too wild."
        ),
    },
    {
        "category": "Processing · Honey",
        "text": (
            "Honey processing is a middle ground: the skin is removed, but some or all "
            "of the sticky fruit mucilage is left on the bean during drying. More mucilage "
            "= more sweetness and body. 'Yellow honey,' 'red honey,' and 'black honey' "
            "refer to how much mucilage is left — black honey is the most fruit-forward."
        ),
    },
    # ── Grind Size ──────────────────────────────────────────────────────────
    {
        "category": "Grind Size · Extraction",
        "text": (
            "Grind size controls how quickly water extracts compounds from coffee. "
            "Finer grinds expose more surface area — extraction happens faster. Coarser "
            "grinds slow things down. Espresso uses fine grinds (high pressure, short "
            "time); cold brew uses coarse grinds (no pressure, many hours)."
        ),
    },
    {
        "category": "Grind Size · Extraction",
        "text": (
            "If your coffee tastes sour or weak, try grinding finer — you're under-"
            "extracting (not pulling enough flavor out). If it tastes bitter or harsh, "
            "try grinding coarser — you're over-extracting (pulling out too much). "
            "Grind size is the most powerful dial you can turn."
        ),
    },
    {
        "category": "Grind Size · Burr Grinders",
        "text": (
            "A burr grinder crushes beans between two abrasive surfaces for a consistent "
            "particle size. A blade grinder chops randomly, producing both powder and "
            "chunks in the same grind — wildly inconsistent extraction. If you want to "
            "improve your coffee without spending much, a decent burr grinder is the "
            "single best upgrade."
        ),
    },
    # ── Water ────────────────────────────────────────────────────────────────
    {
        "category": "Water · Temperature",
        "text": (
            "Water temperature dramatically affects extraction. The specialty coffee "
            "sweet spot is 90–96 °C (195–205 °F). Boiling water (100 °C) scorches "
            "delicate light roasts and exaggerates bitterness. Cooler water under-extracts "
            "and produces a flat, sour cup. Let boiled water rest 30 seconds before pouring."
        ),
    },
    {
        "category": "Water · Quality",
        "text": (
            "Coffee is about 98% water, so water quality matters a lot. Soft water "
            "under-extracts (not enough minerals to bond with coffee compounds); very "
            "hard water over-extracts and tastes metallic. Filtered tap water is usually "
            "ideal — you want some minerals, just not too many."
        ),
    },
    {
        "category": "Water · Ratios",
        "text": (
            "The SCA (Specialty Coffee Association) recommends a brew ratio of around "
            "1:15 to 1:17 (coffee to water by weight) for filter coffee. A kitchen "
            "scale changes the game — volumetric scoops are inconsistent because grind "
            "density varies. Weigh your coffee and water and your results become "
            "dramatically more repeatable."
        ),
    },
    # ── Common Mistakes ──────────────────────────────────────────────────────
    {
        "category": "Beginner Tips · Mistakes",
        "text": (
            "One of the most common mistakes: using pre-ground coffee that's been open "
            "for weeks. Coffee goes stale fast — most of its aromatics are gone within "
            "days of grinding. Buy whole beans and grind just before brewing. It makes "
            "a shocking difference."
        ),
    },
    {
        "category": "Beginner Tips · Mistakes",
        "text": (
            "Another common mistake: storing coffee in the freezer or fridge. Condensation "
            "damages the bean and transfers fridge smells. Instead, store beans in an "
            "airtight container at room temperature, away from light. Consume within "
            "3–4 weeks of the roast date for peak flavor."
        ),
    },
    {
        "category": "Beginner Tips · Mistakes",
        "text": (
            "Skipping the bloom when doing pour over is a subtle but real mistake. "
            "Fresh coffee releases CO₂ gas that repels water during extraction. The "
            "30-second bloom lets that gas escape first, so subsequent pours extract "
            "evenly. Old coffee barely blooms — minimal bubbling is a sign it's stale."
        ),
    },
    {
        "category": "Beginner Tips · Freshness",
        "text": (
            "Look for the roast date on specialty coffee bags — not a 'best by' date. "
            "The sweet spot for most filter coffees is 7–21 days after roasting. "
            "Too fresh and CO₂ is still escaping aggressively; too old and the best "
            "aromatics have faded. Espresso can benefit from resting a bit longer, "
            "up to 3–4 weeks post-roast."
        ),
    },
    # ── Fun Facts & Culture ──────────────────────────────────────────────────
    {
        "category": "Fun Facts · Culture",
        "text": (
            "The term 'specialty coffee' has a specific definition: beans that score "
            "80 points or above on a 100-point scale by a trained Q-Grader (a certified "
            "coffee taster). Only a small percentage of global coffee production qualifies. "
            "It's the equivalent of fine wine compared to table wine."
        ),
    },
    {
        "category": "Fun Facts · Culture",
        "text": (
            "Coffee was discovered — according to legend — by an Ethiopian goat herder "
            "named Kaldi, who noticed his goats were unusually energetic after eating "
            "berries from a particular tree. Whether or not it's true, Ethiopia remains "
            "the genetic homeland of Coffea arabica."
        ),
    },
    {
        "category": "Fun Facts · Culture",
        "text": (
            "The 'third wave' of coffee refers to the movement (starting in the early "
            "2000s) that treats coffee like craft: emphasizing origin, traceability, "
            "and light roasting to highlight terroir. The first wave was mass "
            "commercialisation (Folgers, Maxwell House); the second wave was the "
            "espresso bar boom (Starbucks)."
        ),
    },
    {
        "category": "Fun Facts · Science",
        "text": (
            "Coffee has over 800 aromatic compounds — more than wine, which has around "
            "200. This is why cupping (professional coffee tasting) can identify notes "
            "like bergamot, jasmine, peach, dark chocolate, or tobacco. Your nose does "
            "most of the tasting; much of what we call 'flavor' is actually aroma."
        ),
    },
    {
        "category": "Fun Facts · Science",
        "text": (
            "Caffeine is a natural pesticide — the coffee plant evolved it to deter "
            "insects from eating its seeds. Robusta beans (used in cheap instant coffee) "
            "have nearly twice the caffeine of Arabica beans, and also a harsher, more "
            "rubbery flavor. Specialty coffee focuses almost exclusively on Arabica."
        ),
    },
    {
        "category": "Fun Facts · Culture",
        "text": (
            "A 'cupping' session is how coffee professionals evaluate beans. They grind "
            "coffee directly into cups, pour hot water, let it brew 4 minutes, then break "
            "the crust and slurp loudly with a spoon. The loud slurp sprays the coffee "
            "across your palate, helping you assess it fully. Yes, slurping loudly is "
            "encouraged."
        ),
    },
    # ── Espresso Drinks ──────────────────────────────────────────────────────
    {
        "category": "Brewing · Espresso Drinks",
        "text": (
            "A flat white originated in Australia and New Zealand — it's essentially "
            "a smaller, stronger latte. Where a latte uses 1 shot in ~240 mL of milk, "
            "a flat white uses 2 ristretto shots in ~160 mL of milk. The higher "
            "coffee-to-milk ratio means you actually taste the espresso."
        ),
    },
    {
        "category": "Brewing · Espresso Drinks",
        "text": (
            "A ristretto ('restricted' in Italian) is a shorter espresso pull — same "
            "amount of coffee but half the water. The result is sweeter and more "
            "concentrated, because you stop before the bitter compounds extract. "
            "Many specialty cafes use ristretto shots as the base for milk drinks."
        ),
    },
    {
        "category": "Brewing · Espresso Drinks",
        "text": (
            "Milk texture matters as much as espresso quality in a latte. Properly "
            "steamed milk should look like wet paint — glossy, velvety microfoam with "
            "no visible bubbles. The goal is to incorporate air in tiny amounts so "
            "the milk gets silky, not frothy. Tilt the pitcher and keep the steam "
            "wand just below the surface."
        ),
    },
    # ── Tasting · How to Taste ───────────────────────────────────────────────
    {
        "category": "Coffee Tasting · How to Taste",
        "text": (
            "To really taste coffee, let it cool a little first. Hot liquid numbs "
            "your palate to subtlety. Around 60–70 °C you start picking up sweetness "
            "and fruit. As it cools further to 40–50 °C, acidity and complexity open "
            "up. A coffee that tastes flat when hot often reveals beautiful notes as "
            "it cools."
        ),
    },
    {
        "category": "Coffee Tasting · How to Taste",
        "text": (
            "Try the 'retronasal' trick: take a sip, swallow, then exhale slowly "
            "through your nose. Aromatic compounds travel up from your throat and "
            "you'll detect flavors you couldn't before. This is the same reason food "
            "tastes flat when your nose is blocked — most 'flavor' is actually smell."
        ),
    },
]


# ── Custom view with a warm parchment background ─────────────────────────────

class ParchmentView(NSView):
    def drawRect_(self, rect):
        NSColor.colorWithSRGBRed_green_blue_alpha_(0.99, 0.96, 0.90, 1.0).set()
        NSBezierPath.fillRect_(self.bounds())


# ── Popover content view controller ──────────────────────────────────────────

class SnippetViewController(NSViewController):

    @objc.python_method
    def setup(self, app_ref):
        self._app = app_ref
        self._snippet = None

    def loadView(self):
        W, H = 300, 190

        view = ParchmentView.alloc().initWithFrame_(NSMakeRect(0, 0, W, H))

        # ── category label (top, muted brown) ────────────────────────────────
        self._cat = NSTextField.alloc().initWithFrame_(NSMakeRect(14, H - 30, W - 28, 18))
        self._cat.setEditable_(False)
        self._cat.setBezeled_(False)
        self._cat.setDrawsBackground_(False)
        self._cat.setFont_(NSFont.systemFontOfSize_(10))
        self._cat.setTextColor_(
            NSColor.colorWithSRGBRed_green_blue_alpha_(0.55, 0.30, 0.08, 1.0)
        )

        # ── snippet text (wrapping) ───────────────────────────────────────────
        self._text = NSTextField.alloc().initWithFrame_(NSMakeRect(14, 50, W - 28, H - 88))
        self._text.setEditable_(False)
        self._text.setBezeled_(False)
        self._text.setDrawsBackground_(False)
        self._text.setFont_(NSFont.systemFontOfSize_(12))
        self._text.setTextColor_(
            NSColor.colorWithSRGBRed_green_blue_alpha_(0.15, 0.07, 0.02, 1.0)
        )
        self._text.setAlignment_(NSTextAlignmentLeft)
        self._text.cell().setWraps_(True)

        # ── "One more cup" button — borderless, styled to match the theme ────
        brown = NSColor.colorWithSRGBRed_green_blue_alpha_(0.55, 0.30, 0.08, 1.0)
        label = NSAttributedString.alloc().initWithString_attributes_(
            "One more cup",
            {
                NSForegroundColorAttributeName: brown,
                NSFontAttributeName: NSFont.systemFontOfSize_(12),
            },
        )
        next_btn = NSButton.alloc().initWithFrame_(NSMakeRect(W - 114, 10, 100, 22))
        next_btn.setAttributedTitle_(label)
        next_btn.setBordered_(False)
        next_btn.setTarget_(self)
        next_btn.setAction_("onNext:")

        for sub in (self._cat, self._text, next_btn):
            view.addSubview_(sub)

        self.setView_(view)

        if self._snippet is not None:
            self._render()

    @objc.python_method
    def _render(self):
        self._cat.setStringValue_(self._snippet["category"])
        self._text.setStringValue_(self._snippet["text"])

    @objc.python_method
    def update(self, snippet):
        self._snippet = snippet
        if self.isViewLoaded():
            self._render()

    def onNext_(self, sender):
        self._app.advance()


# ── Thin NSObject to receive the status-bar button click ──────────────────────

class ClickHandler(NSObject):

    @objc.python_method
    def setup(self, app_ref):
        self._app = app_ref

    def onClicked_(self, sender):
        self._app.toggle_popover()


# ── Main app ──────────────────────────────────────────────────────────────────

class CoffeeBuddyApp(rumps.App):

    def __init__(self):
        super().__init__("☕", quit_button=None)

        # snippet deck
        self._deck = list(range(len(SNIPPETS)))
        random.shuffle(self._deck)
        self._current = self._deck.pop()

        # view controller + popover
        self._vc = SnippetViewController.alloc().init()
        self._vc.setup(self)
        self._vc.update(SNIPPETS[self._current])

        self._popover = NSPopover.alloc().init()
        self._popover.setContentViewController_(self._vc)
        self._popover.setBehavior_(NSPopoverBehaviorTransient)
        self._popover.setContentSize_(NSMakeSize(300, 190))

        # nsstatusitem is created during run() → defer click-handler wiring
        self._click_handler = ClickHandler.alloc().init()
        self._click_handler.setup(self)
        rumps.events.before_start.register(self._wire_status_item)

    def _wire_status_item(self):
        """Called by before_start, after initializeStatusBar() creates nsstatusitem."""
        si = self._nsapp.nsstatusitem
        si.setMenu_(None)
        btn = si.button()
        btn.setTarget_(self._click_handler)
        btn.setAction_("onClicked:")

    def toggle_popover(self):
        btn = self._nsapp.nsstatusitem.button()
        if self._popover.isShown():
            self._popover.performClose_(btn)
        else:
            self._popover.showRelativeToRect_ofView_preferredEdge_(
                btn.bounds(), btn, NSMaxYEdge
            )

    def advance(self):
        if not self._deck:
            self._deck = list(range(len(SNIPPETS)))
            random.shuffle(self._deck)
        self._current = self._deck.pop()
        self._vc.update(SNIPPETS[self._current])


if __name__ == "__main__":
    CoffeeBuddyApp().run()
