import random
import objc
import rumps
from AppKit import (
    NSObject, NSViewController, NSView,
    NSTextField, NSButton, NSColor, NSFont, NSBezierPath,
    NSMakeRect,
    NSTextAlignmentLeft, NSForegroundColorAttributeName, NSFontAttributeName,
    NSPopUpMenuWindowLevel,
    NSPanel, NSBackingStoreBuffered,
    NSEvent,
)
from Foundation import NSAttributedString

SNIPPETS = [
    # ── Acidity ───────────────────────────────────────────────────────────────
    {
        "category": "Coffee Tasting · Acidity",
        "text": (
            "In specialty coffee, acidity is a good thing. It is the bright, lively "
            "quality that makes a cup feel vibrant. Think of the tartness of a ripe "
            "apple. Ethiopian coffees are celebrated for their bright, wine-like acidity."
        ),
    },
    {
        "category": "Coffee Tasting · Acidity",
        "text": (
            "Acidity goes down as roast level goes up. A light Ethiopian might taste "
            "like lemon and blueberry. The same bean roasted dark loses those acids "
            "and tastes more like chocolate and smoke. Both are valid — just different."
        ),
    },
    {
        "category": "Coffee Tasting · Acidity",
        "text": (
            "Acidity and sourness are not the same. Sourness means under-extraction "
            "— harsh and unpleasant. Acidity means brightness — lively and clean. "
            "Think of fresh lemonade (bright acidity) versus vinegar (sour)."
        ),
    },
    {
        "category": "Coffee Tasting · Acidity",
        "text": (
            "Coffee grown above 1,500 metres tends to have brighter acidity. Cooler "
            "temperatures slow down cherry ripening, allowing more complex acids to "
            "develop. This is why Ethiopian and Kenyan highland coffees taste so lively."
        ),
    },
    {
        "category": "Coffee Tasting · Acidity",
        "text": (
            "Different acids create different flavors. Citric acid gives lemon and "
            "orange notes. Malic acid gives apple and pear. Phosphoric acid creates "
            "a clean, fizzy quality found in some Kenyan coffees."
        ),
    },
    {
        "category": "Coffee Tasting · Acidity",
        "text": (
            "If your coffee tastes too sharp, try lowering your water temperature "
            "by 3–4 degrees. Cooler water (around 90°C) extracts fewer harsh acids. "
            "This simple fix often makes a big difference without changing your recipe."
        ),
    },
    {
        "category": "Coffee Tasting · Acidity",
        "text": (
            "Grind size affects acidity. A coarser grind leaves acidity more prominent. "
            "A finer grind extracts more sweetness to balance the acid. If your coffee "
            "tastes too tart, try grinding a little finer first."
        ),
    },
    {
        "category": "Coffee Tasting · Acidity",
        "text": (
            "Washed coffees have cleaner, more defined acidity. The fruit pulp is "
            "removed before drying, so the bean's natural acids shine clearly. "
            "Natural-processed coffees have more fruit sweetness, which softens "
            "the acidity."
        ),
    },
    {
        "category": "Coffee Tasting · Acidity",
        "text": (
            "Unpleasant sourness — not brightness, just harshness — almost always "
            "means under-extraction. Try a finer grind, hotter water, or longer brew "
            "time. Sourness is a brewing problem you can fix, not a flaw in the bean."
        ),
    },
    # ── Body ──────────────────────────────────────────────────────────────────
    {
        "category": "Coffee Tasting · Body",
        "text": (
            "Body describes the weight or texture of coffee in your mouth — like the "
            "difference between skim milk and whole milk. French press tends to feel "
            "heavy. Pour over through paper tends to feel lighter and cleaner."
        ),
    },
    {
        "category": "Coffee Tasting · Body",
        "text": (
            "French press feels heavier than pour over because the metal filter lets "
            "oils and fine particles through. Paper filters absorb those oils, "
            "producing a lighter cup. The beans are the same — the filter changes "
            "the texture."
        ),
    },
    {
        "category": "Coffee Tasting · Body",
        "text": (
            "Sumatran coffees are famous for their heavy, syrupy body. This comes "
            "from a process called wet-hulling, which creates a full, earthy mouthfeel. "
            "If you have never tried one, the thick body alone is worth experiencing."
        ),
    },
    {
        "category": "Coffee Tasting · Body",
        "text": (
            "Espresso has the heaviest body of any brew method. High pressure "
            "extracts more oils and dissolved solids than gravity-fed methods. "
            "That rich, syrupy texture is a big part of what makes espresso "
            "satisfying in a tiny cup."
        ),
    },
    {
        "category": "Coffee Tasting · Body",
        "text": (
            "A light body is not a flaw. A clean, delicate pour over from a washed "
            "Ethiopian can feel almost tea-like, which suits its floral character "
            "perfectly. Body should match the coffee's flavor profile."
        ),
    },
    {
        "category": "Coffee Tasting · Body",
        "text": (
            "Higher brew ratios increase body. Using more coffee — say 1:14 instead "
            "of 1:16 — extracts more dissolved solids, making the cup feel heavier. "
            "If your coffee tastes thin and watery, try using a little more coffee."
        ),
    },
    {
        "category": "Coffee Tasting · Body",
        "text": (
            "Milk adds its own body to coffee drinks. A flat white made with a "
            "light espresso can still feel satisfying because the milk fills in "
            "the weight. Milk drinks are forgiving of lighter-bodied coffees."
        ),
    },
    {
        "category": "Coffee Tasting · Body",
        "text": (
            "Body and bitterness can feel similar to beginners. The difference: "
            "body is physical weight you feel, like thickness. Bitterness is a "
            "taste you perceive, like dark chocolate. They are different sensations."
        ),
    },
    {
        "category": "Coffee Tasting · Body",
        "text": (
            "Cold brew tends to feel smooth and medium-bodied. Cold water extracts "
            "fewer sharp acids, so the result feels rounder and less aggressive. "
            "Good body without the edge."
        ),
    },
    # ── Sweetness ─────────────────────────────────────────────────────────────
    {
        "category": "Coffee Tasting · Sweetness",
        "text": (
            "Well-extracted coffee is naturally sweet — no sugar needed. That "
            "sweetness comes from sugars caramelized during roasting. If your "
            "coffee tastes only bitter or sour, sweetness is being blocked "
            "by under- or over-extraction."
        ),
    },
    {
        "category": "Coffee Tasting · Sweetness",
        "text": (
            "Sweetness comes from sucrose that survived roasting. Some sucrose "
            "caramelizes into pleasant sweet compounds; some burns into bitter ones. "
            "Light to medium roasts preserve more sweetness than very dark roasts."
        ),
    },
    {
        "category": "Coffee Tasting · Sweetness",
        "text": (
            "Natural-processed coffees often taste sweeter. When the coffee cherry "
            "dries around the bean, fruit sugars migrate into the seed. A natural "
            "Ethiopian can taste like fruit juice — intensely sweet with no added sugar."
        ),
    },
    {
        "category": "Coffee Tasting · Sweetness",
        "text": (
            "Sweetness is easiest to detect as coffee cools. Hot liquid suppresses "
            "your tongue's sweet receptors. A cup that tastes flat at 70°C can reveal "
            "rich, caramel-like sweetness at 50°C. Let it cool before judging."
        ),
    },
    {
        "category": "Coffee Tasting · Sweetness",
        "text": (
            "If you add sugar to every cup, try lighter-roasted coffee first. "
            "Dark roasts often taste bitter because the sugars burned off during "
            "roasting. A medium roast from a good source can be sweet enough "
            "to drink black."
        ),
    },
    {
        "category": "Coffee Tasting · Sweetness",
        "text": (
            "The bloom in pour over brewing helps extract sweetness evenly. "
            "Pouring a small amount of water first and waiting 30 seconds lets "
            "CO₂ escape. Skipping the bloom can cause uneven extraction that "
            "hurts sweetness."
        ),
    },
    {
        "category": "Coffee Tasting · Sweetness",
        "text": (
            "Sweetness and bitterness balance each other. A coffee can be quite "
            "bitter but still feel pleasant if its sweetness is high enough — "
            "like dark chocolate. Coffee without sweetness will always taste harsh."
        ),
    },
    {
        "category": "Coffee Tasting · Sweetness",
        "text": (
            "Under-extraction kills sweetness. Sour acids extract first, and the "
            "sweet sugars that extract later never make it into the cup. A sour, "
            "thin coffee is not low-sweetness by nature — it is under-extracted."
        ),
    },
    {
        "category": "Coffee Tasting · Sweetness",
        "text": (
            "Honey-processed coffees sit between washed and natural in sweetness. "
            "Some fruit pulp is left on the bean during drying, adding a moderate "
            "sweetness boost. The result is often syrupy and peachy."
        ),
    },
    # ── Aftertaste ────────────────────────────────────────────────────────────
    {
        "category": "Coffee Tasting · Aftertaste",
        "text": (
            "A great coffee has a pleasant aftertaste that lingers — called the "
            "finish. Specialty coffees can finish with caramel, dark chocolate, "
            "jasmine, or fruit. Sit quietly after you swallow and notice what stays."
        ),
    },
    {
        "category": "Coffee Tasting · Aftertaste",
        "text": (
            "The SCA scoring system gives aftertaste its own score. Judges rate "
            "both how long it lasts and whether it is pleasant. A coffee that "
            "scores well is one where you are still enjoying the finish a full "
            "minute later."
        ),
    },
    {
        "category": "Coffee Tasting · Aftertaste",
        "text": (
            "A long aftertaste is a sign of quality. Well-grown, carefully "
            "processed coffee leaves complex compounds that linger pleasantly. "
            "Over-roasted coffee often has a short finish — or leaves an "
            "unpleasant dryness."
        ),
    },
    {
        "category": "Coffee Tasting · Aftertaste",
        "text": (
            "Fruity aftertastes are common in light-roasted Ethiopian and Kenyan "
            "coffees. After swallowing, you might notice blueberry or red fruit "
            "lingering at the back of your throat — delicate aromatic compounds "
            "releasing slowly."
        ),
    },
    {
        "category": "Coffee Tasting · Aftertaste",
        "text": (
            "Roasty or smoky aftertastes are normal in dark roasts. But if that "
            "is all you taste — just ash and char — the roast may have gone too "
            "far. The best dark roasts finish with bittersweet chocolate lingering "
            "behind the roasty note."
        ),
    },
    {
        "category": "Coffee Tasting · Aftertaste",
        "text": (
            "An unpleasant aftertaste often points to a specific problem. A harsh, "
            "drying finish usually means over-extraction. A thin, sharp finish "
            "usually means under-extraction. A papery finish usually means "
            "stale coffee."
        ),
    },
    {
        "category": "Coffee Tasting · Aftertaste",
        "text": (
            "The finish changes as coffee cools. A cup with a flat aftertaste when "
            "hot can develop a longer, more interesting finish at 45–50°C. Some "
            "light-roasted naturals are best experienced warm, not hot, "
            "for this reason."
        ),
    },
    {
        "category": "Coffee Tasting · Aftertaste",
        "text": (
            "Aftertaste and aroma are closely linked. Many flavors in the finish "
            "are aromatic compounds traveling from your throat to your nasal cavity "
            "as you breathe out. Exhaling slowly through your nose after a sip "
            "deepens the aftertaste."
        ),
    },
    # ── How to Taste ──────────────────────────────────────────────────────────
    {
        "category": "Coffee Tasting · How to Taste",
        "text": (
            "Let your coffee cool before tasting. Hot liquid numbs your palate. "
            "Around 60–70°C you start picking up sweetness and fruit. At 40–50°C, "
            "acidity and complexity open up. A cup that tastes flat when hot often "
            "reveals beautiful notes as it cools."
        ),
    },
    {
        "category": "Coffee Tasting · How to Taste",
        "text": (
            "Try the retronasal trick: take a sip, swallow, then exhale slowly "
            "through your nose. Aromatic compounds travel up from your throat and "
            "you will detect flavors you missed before. Most of what we call "
            "'flavor' is actually smell."
        ),
    },
    {
        "category": "Coffee Tasting · How to Taste",
        "text": (
            "Before you sip, smell the coffee. Inhale slowly and try to name "
            "what you smell in broad categories: fruity, floral, nutty, chocolatey, "
            "or earthy? Aroma primes your brain for what to expect and often "
            "predicts the flavor accurately."
        ),
    },
    {
        "category": "Coffee Tasting · How to Taste",
        "text": (
            "Take a small sip and roll it around your mouth before swallowing. "
            "This coats your entire palate and gives all taste receptors a chance "
            "to register. Flavor is richer when coffee reaches the sides and "
            "back of your tongue."
        ),
    },
    {
        "category": "Coffee Tasting · How to Taste",
        "text": (
            "Professional cuppers slurp coffee loudly on purpose. The forceful "
            "inhale sprays coffee across the whole palate and aerates it, "
            "intensifying the aroma. It sounds rude, but the difference in "
            "flavor intensity is real."
        ),
    },
    {
        "category": "Coffee Tasting · How to Taste",
        "text": (
            "Notice where you feel flavors in your mouth. Sweetness is strongest "
            "at the tip of the tongue. Acidity sits on the sides. Bitterness "
            "appears at the back. Paying attention to these zones helps you "
            "identify what is happening."
        ),
    },
    {
        "category": "Coffee Tasting · How to Taste",
        "text": (
            "Rate each cup on three things: acidity (bright or flat?), sweetness "
            "(present or absent?), and finish (long and pleasant, or short and "
            "harsh?). This simple framework makes it easy to compare cups "
            "over time."
        ),
    },
    {
        "category": "Coffee Tasting · How to Taste",
        "text": (
            "Keep a short tasting note — even just two or three words — for every "
            "coffee you try. Writing forces you to commit to a description. Over "
            "weeks, you will see which origins and brew methods consistently give "
            "you cups you love."
        ),
    },
    {
        "category": "Coffee Tasting · How to Taste",
        "text": (
            "Your ability to taste improves with deliberate practice. Each time "
            "you try to name what you notice, you are building a sensory vocabulary. "
            "After a few months, you will detect flavors in everyday coffee that "
            "you previously missed."
        ),
    },
    {
        "category": "Coffee Tasting · How to Taste",
        "text": (
            "Avoid vague words like 'good' or 'smooth.' Try to be specific: "
            "'bright and lemony,' 'heavy with dark chocolate,' 'light and floral.' "
            "Precise descriptions help your palate develop faster and make it "
            "easier to find coffees you will love."
        ),
    },
    # ── Aroma ─────────────────────────────────────────────────────────────────
    {
        "category": "Coffee Tasting · Aroma",
        "text": (
            "Dry fragrance is what you smell from freshly ground, dry coffee "
            "before water is added. Wet aroma is what rises from the cup right "
            "after hot water hits the grounds. Both reveal different things "
            "about the coffee's character."
        ),
    },
    {
        "category": "Coffee Tasting · Aroma",
        "text": (
            "During professional cupping, tasters evaluate dry fragrance before "
            "water is added, then wet aroma after pouring, and again after "
            "breaking the crust on top. Each phase reveals a different layer "
            "of the aromatic profile."
        ),
    },
    {
        "category": "Coffee Tasting · Aroma",
        "text": (
            "Aroma accounts for about 70–80% of what we perceive as flavor. "
            "Most of the 'taste' of coffee actually enters through your nose "
            "as you swallow. This is why coffee tastes flat when you have "
            "a blocked nose."
        ),
    },
    {
        "category": "Coffee Tasting · Aroma",
        "text": (
            "Freshly ground coffee smells dramatically better than pre-ground. "
            "Grinding exposes the bean's internal surface, releasing trapped "
            "aromatics. Within 15 minutes of grinding, much of the delicate "
            "fragrance has already evaporated."
        ),
    },
    {
        "category": "Coffee Tasting · Aroma",
        "text": (
            "Roast level shifts aroma dramatically. Light roasts smell floral "
            "and fruity. Medium roasts shift toward caramel and chocolate. "
            "Dark roasts smell smoky and boldly roasted — original "
            "bean aromas replaced by roast-derived compounds."
        ),
    },
    {
        "category": "Coffee Tasting · Aroma",
        "text": (
            "Coffee contains over 800 volatile aromatic compounds. Many are "
            "shared with fruits, flowers, and spices — which is why coffee can "
            "genuinely smell like blueberries or jasmine. These are natural "
            "products of fermentation and roasting."
        ),
    },
    {
        "category": "Coffee Tasting · Aroma",
        "text": (
            "Earthy and woody aromas are typical of wet-hulled Indonesian coffees "
            "like Sumatra. The process leaves the bean porous and prone to "
            "picking up environmental flavors during drying. This earthiness "
            "is a feature, not a defect."
        ),
    },
    {
        "category": "Coffee Tasting · Aroma",
        "text": (
            "Fermentation aromas — wine, grape, tropical fruit — are common in "
            "natural-processed coffees. High-quality fermentation creates complex, "
            "pleasant aromas. Poor fermentation smells sour or rotten — "
            "a clear sign of a processing defect."
        ),
    },
    {
        "category": "Coffee Tasting · Aroma",
        "text": (
            "Your sense of smell is sharpest before you have eaten or had strong "
            "flavors. Morning is often the best time to evaluate a coffee's aroma "
            "because your olfactory receptors are fresh. Many professional tasters "
            "cup in the morning for this reason."
        ),
    },
    # ── Balance ───────────────────────────────────────────────────────────────
    {
        "category": "Coffee Tasting · Balance",
        "text": (
            "Balance means no single flavor dominates uncomfortably. A balanced "
            "cup has bright acidity, present but gentle bitterness, and sweetness "
            "that ties everything together. You taste multiple things at once "
            "without any one demanding all the attention."
        ),
    },
    {
        "category": "Coffee Tasting · Balance",
        "text": (
            "Colombia and Guatemala are often cited as examples of balanced coffees. "
            "Enough acidity to be interesting, enough sweetness to be approachable, "
            "enough body to be satisfying — none overpowering the others. "
            "Balance is universally appealing."
        ),
    },
    {
        "category": "Coffee Tasting · Balance",
        "text": (
            "A coffee can be intense and still be balanced. A very acidic Ethiopian "
            "is balanced if its sweetness is high enough to match. A very full-bodied "
            "Sumatran is balanced if it has enough brightness to cut through."
        ),
    },
    {
        "category": "Coffee Tasting · Balance",
        "text": (
            "Extraction quality is the biggest driver of balance. Under-extracted "
            "coffee tips toward sour and thin. Over-extracted coffee tips toward "
            "bitter and flat. A well-extracted cup sits in the sweet spot where "
            "all compounds are in pleasing proportion."
        ),
    },
    {
        "category": "Coffee Tasting · Balance",
        "text": (
            "When tasting several coffees side by side, the most balanced one "
            "often is not the most exciting — but it is the one you would most "
            "want to drink every day. Balance is what makes a coffee great for "
            "daily drinking."
        ),
    },
    {
        "category": "Coffee Tasting · Balance",
        "text": (
            "You can nudge balance by adjusting your brew ratio. If the coffee "
            "tastes too sharp, use slightly more coffee (1:15 instead of 1:16). "
            "If it tastes too bitter, use slightly less. Small ratio changes "
            "move the balance noticeably."
        ),
    },
    {
        "category": "Coffee Tasting · Balance",
        "text": (
            "Milk finds the balance that black coffee sometimes lacks. Milk "
            "proteins bind to bitter compounds, milk sugars add sweetness, "
            "and milk fats add body. A coffee that tastes unbalanced black "
            "often works beautifully as a latte."
        ),
    },
    {
        "category": "Coffee Tasting · Balance",
        "text": (
            "Water quality affects balance. Very soft water makes coffee taste "
            "flat and under-extracted. Very hard water makes it taste bitter. "
            "The ideal is around 150 ppm total dissolved solids — enough minerals "
            "to extract properly without dominating."
        ),
    },
    {
        "category": "Coffee Tasting · Balance",
        "text": (
            "Medium-roasted coffees tend to be the most balanced. They sit "
            "between the bright acidity of light roasts and the heavy bitterness "
            "of dark roasts. This is one reason medium roasts are the "
            "most popular worldwide."
        ),
    },
    # ── Bitterness ────────────────────────────────────────────────────────────
    {
        "category": "Coffee Tasting · Bitterness",
        "text": (
            "Bitterness in coffee is not automatically bad. It is a natural "
            "background note that adds depth. The problem is when bitterness is "
            "sharp or dominates everything else. A well-extracted dark roast has "
            "pleasant bitterness balanced by sweetness."
        ),
    },
    {
        "category": "Coffee Tasting · Bitterness",
        "text": (
            "Most unpleasant bitterness in espresso comes from over-extraction — "
            "pulling the shot too long, grinding too fine, or brewing too hot. "
            "Stopping the shot a few seconds earlier often dramatically improves "
            "sweetness and removes the bite."
        ),
    },
    {
        "category": "Coffee Tasting · Bitterness",
        "text": (
            "Caffeine is bitter, but most of the bitterness people dislike does "
            "not come from caffeine. It comes from over-extracted chlorogenic acid "
            "breakdown products — quinic acids and phenolic compounds produced "
            "by excess heat and time."
        ),
    },
    {
        "category": "Coffee Tasting · Bitterness",
        "text": (
            "A tiny pinch of salt in bitter coffee genuinely works. Salt suppresses "
            "bitterness perception by blocking bitter taste receptors — not by "
            "adding a salty taste. It is especially useful for drip coffee "
            "that has been sitting on a hot plate."
        ),
    },
    {
        "category": "Coffee Tasting · Bitterness",
        "text": (
            "Roast level is the single biggest driver of bitterness. Light roasts "
            "have mild bitterness and more acidity. As the roast darkens, more "
            "bitter compounds form. Dark roasts can have three to four times "
            "more bitter compounds than light roasts."
        ),
    },
    {
        "category": "Coffee Tasting · Bitterness",
        "text": (
            "Grind size directly controls bitterness. A finer grind increases "
            "extraction — more compounds dissolve, including bitter ones. If your "
            "coffee is consistently too bitter, try a slightly coarser grind. "
            "It is often the only fix needed."
        ),
    },
    {
        "category": "Coffee Tasting · Bitterness",
        "text": (
            "Brew temperature affects bitterness. Water above 96°C extracts "
            "bitter compounds more aggressively. If your coffee tastes harsh, "
            "try lowering water temperature by 2–3 degrees. This is especially "
            "helpful with dark roasts."
        ),
    },
    {
        "category": "Coffee Tasting · Bitterness",
        "text": (
            "What you call 'bitter' might actually be a roasted or smoky flavor. "
            "True bitterness is a physical sensation at the back of the tongue. "
            "Roasty and smoky are flavor-based. Learning to tell them apart "
            "helps you diagnose brew problems accurately."
        ),
    },
    {
        "category": "Coffee Tasting · Bitterness",
        "text": (
            "Dark chocolate contains the same bitter compounds as dark-roasted "
            "coffee. People who enjoy dark chocolate often appreciate darker "
            "coffees for the same reason — balanced bitterness paired with "
            "enough sweetness to be enjoyable."
        ),
    },
    # ── Flavor Notes ──────────────────────────────────────────────────────────
    {
        "category": "Coffee Tasting · Flavor Notes",
        "text": (
            "Flavor notes on a bag — blueberry, jasmine, dark chocolate — "
            "are not added ingredients. They are natural compounds created "
            "during growth, fermentation, and roasting. Coffee has over 800 "
            "volatile compounds, many shared with fruits and flowers."
        ),
    },
    {
        "category": "Coffee Tasting · Flavor Notes",
        "text": (
            "To identify fruit notes, let your coffee cool to around 55–60°C. "
            "Cup your hands around the mug and inhale slowly. Try to categorize "
            "the aroma: citrus (bright, sharp), stone fruit (peachy), "
            "or berry (sweet, jammy)?"
        ),
    },
    {
        "category": "Coffee Tasting · Flavor Notes",
        "text": (
            "Chocolate notes come from Maillard reaction products formed during "
            "roasting. Milk chocolate appears in medium roasts; dark chocolate "
            "deepens with the roast. Brazil and Guatemala are classic sources "
            "of chocolate-forward coffees."
        ),
    },
    {
        "category": "Coffee Tasting · Flavor Notes",
        "text": (
            "Floral notes are most common in light roasts from Ethiopia, Yemen, "
            "and Panama. Jasmine, rose, and chamomile are found in high-quality "
            "arabica. These compounds evaporate quickly — floral coffees are "
            "best tasted around 60°C."
        ),
    },
    {
        "category": "Coffee Tasting · Flavor Notes",
        "text": (
            "Nutty flavors — hazelnut, almond, walnut — come from pyrazines "
            "formed during medium roasting. They are warm, comforting, and "
            "broadly appealing. Brazilian naturals and Central American medium "
            "roasts are reliably nutty."
        ),
    },
    {
        "category": "Coffee Tasting · Flavor Notes",
        "text": (
            "Caramel and toffee notes develop during medium roasting as sugars "
            "caramelize. They are warm, sweet, and easy to identify — a great "
            "starting point for training your palate. Medium-roasted Colombian "
            "coffees are a reliable source."
        ),
    },
    {
        "category": "Coffee Tasting · Flavor Notes",
        "text": (
            "Spice notes — cinnamon, cardamom, clove — appear in some Ethiopian, "
            "Yemeni, and Indian coffees. They come from compounds formed during "
            "fermentation and drying. Breathe out slowly through your nose "
            "after swallowing to catch them."
        ),
    },
    {
        "category": "Coffee Tasting · Flavor Notes",
        "text": (
            "Berry notes — blueberry, raspberry, strawberry — are most common "
            "in natural-processed Ethiopian coffees. The drying cherry ferments "
            "around the bean and transfers real berry-like compounds. "
            "These flavors are natural, not added."
        ),
    },
    {
        "category": "Coffee Tasting · Flavor Notes",
        "text": (
            "Stone fruit notes — peach, apricot, nectarine — are common in "
            "washed coffees from Central America and East Africa. They are "
            "more subtle than berry notes and often come with a smooth, "
            "medium body. Costa Rican coffees are a good example."
        ),
    },
    # ── Mouthfeel ─────────────────────────────────────────────────────────────
    {
        "category": "Coffee Tasting · Mouthfeel",
        "text": (
            "Mouthfeel describes the physical sensation of coffee in your mouth — "
            "its weight, texture, and how it coats your palate. Common descriptors "
            "include watery, light, full, heavy, velvety, silky, dry, or chalky. "
            "It is separate from flavor."
        ),
    },
    {
        "category": "Coffee Tasting · Mouthfeel",
        "text": (
            "Coffee oils contribute significantly to mouthfeel. French press and "
            "full-immersion methods preserve more oils, producing a richer, heavier "
            "feel. Paper filters absorb most oils, producing a lighter, cleaner cup. "
            "Same bean, very different texture."
        ),
    },
    {
        "category": "Coffee Tasting · Mouthfeel",
        "text": (
            "Astringency is that drying, puckering sensation similar to over-steeped "
            "tea. In coffee it usually indicates over-extraction or low-quality beans. "
            "A little adds structure; a lot means too many harsh "
            "compounds were extracted."
        ),
    },
    {
        "category": "Coffee Tasting · Mouthfeel",
        "text": (
            "Viscosity is how thick or syrupy a coffee feels. Espresso has very "
            "high viscosity due to emulsified oils and dissolved solids. A well-"
            "brewed pour over is lighter. Higher dissolved solids generally mean "
            "a heavier mouthfeel."
        ),
    },
    {
        "category": "Coffee Tasting · Mouthfeel",
        "text": (
            "Silky or velvety mouthfeel is considered ideal in well-made espresso "
            "and full-bodied pour overs. It comes from dissolved sugars, emulsified "
            "oils, and fine particles. Nitro cold brew achieves creaminess through "
            "nitrogen bubbles."
        ),
    },
    {
        "category": "Coffee Tasting · Mouthfeel",
        "text": (
            "Chalky mouthfeel is often a sign of under-extraction. The early-"
            "extracting compounds include starches that create a rough, powdery "
            "texture. Better extraction — finer grind, hotter water — balances "
            "these with sugars for a smoother feel."
        ),
    },
    {
        "category": "Coffee Tasting · Mouthfeel",
        "text": (
            "Cold brew has a uniquely smooth mouthfeel. Cold water extracts fewer "
            "harsh acids, removing much of the sharpness. The result feels rounder "
            "and less aggressive on the palate — good body without the edge."
        ),
    },
    {
        "category": "Coffee Tasting · Mouthfeel",
        "text": (
            "Creamy mouthfeel in a latte starts with the espresso. A well-extracted "
            "shot with emulsified oils integrates beautifully with steamed milk. "
            "A thin or watery espresso produces a flat-feeling latte regardless "
            "of how well the milk is steamed."
        ),
    },
    {
        "category": "Coffee Tasting · Mouthfeel",
        "text": (
            "Your mouthfeel perception improves when you drink coffee slowly, in "
            "small sips. Your lips, tongue, cheeks, and throat all contribute to "
            "what you sense as texture. Rushing through a cup makes everything "
            "feel the same. Slow down."
        ),
    },
    # ── Comparing Coffees ─────────────────────────────────────────────────────
    {
        "category": "Coffee Tasting · Comparing Coffees",
        "text": (
            "The best way to train your palate is to taste two coffees side by "
            "side. Brew them identically — same ratio, temperature, and brew time. "
            "Contrast makes differences obvious that would be invisible when "
            "tasting either coffee alone."
        ),
    },
    {
        "category": "Coffee Tasting · Comparing Coffees",
        "text": (
            "Reset your palate between sips with plain water or unsalted crackers. "
            "A bite of banana also works — its starchy, neutral flavor cleanses "
            "the tongue without introducing competing aromas. Avoid mint before "
            "a tasting session."
        ),
    },
    {
        "category": "Coffee Tasting · Comparing Coffees",
        "text": (
            "Try comparing a washed and a natural version of the same origin. "
            "The difference in sweetness, fruit intensity, and mouthfeel is "
            "striking. You will learn more about processing in one tasting "
            "than from hours of reading about it."
        ),
    },
    {
        "category": "Coffee Tasting · Comparing Coffees",
        "text": (
            "Compare the same coffee at different temperatures. At 70°C it tastes "
            "mostly roasty. At 55°C sweetness and fruit emerge. At 40°C acidity "
            "becomes most prominent. Retasting as your cup cools is a tasting "
            "exercise all on its own."
        ),
    },
    {
        "category": "Coffee Tasting · Comparing Coffees",
        "text": (
            "Blind tasting removes the power of labels and expectations. Pour "
            "three coffees into unmarked cups and have someone else randomize "
            "them. You will be surprised how often your palate disagrees with "
            "what you think you prefer."
        ),
    },
    {
        "category": "Coffee Tasting · Comparing Coffees",
        "text": (
            "Compare coffees from different continents. African coffees tend "
            "toward fruit and flowers. Central American toward chocolate and nuts. "
            "Indonesian toward earth and spice. Tasting them side by side makes "
            "these patterns unmistakably clear."
        ),
    },
    {
        "category": "Coffee Tasting · Comparing Coffees",
        "text": (
            "When comparing two coffees, taste the milder one first. Starting "
            "with a bold dark roast will overwhelm your palate and make the next "
            "cup taste thin. Always build from subtle to intense."
        ),
    },
    {
        "category": "Coffee Tasting · Comparing Coffees",
        "text": (
            "Compare the same coffee roasted at light, medium, and dark levels. "
            "This isolates roast as the single variable and shows you how much "
            "roast alone shapes flavor. It is one of the most educational "
            "exercises you can do at home."
        ),
    },
    {
        "category": "Coffee Tasting · Comparing Coffees",
        "text": (
            "Brew the same beans as a pour over and as a French press and taste "
            "them side by side. The difference in body, clarity, and flavor "
            "intensity reveals how much the brew method shapes the cup — sometimes "
            "more than origin or roast level."
        ),
    },
    {
        "category": "Coffee Tasting · Comparing Coffees",
        "text": (
            "When you find a coffee you love, note its origin, processing method, "
            "roast level, and roaster. Use those notes to guide future purchases. "
            "Over time you are building a personal flavor map that helps you find "
            "great coffee every time."
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
            "One more cup ☕️",
            {
                NSForegroundColorAttributeName: brown,
                NSFontAttributeName: NSFont.systemFontOfSize_(12),
            },
        )
        next_btn = NSButton.alloc().initWithFrame_(NSMakeRect(W - 136, 10, 122, 22))
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

        # Non-activating panel — floats above full-screen apps without stealing focus
        # NSWindowStyleMaskNonactivatingPanel = 1 << 7
        # Collection: CanJoinAllSpaces(1) | Transient(8) | FullScreenAuxiliary(256)
        W, H = 300, 190
        self._popup = NSPanel.alloc().initWithContentRect_styleMask_backing_defer_(
            NSMakeRect(0, 0, W, H), 1 << 7, NSBackingStoreBuffered, False
        )
        self._popup.setLevel_(NSPopUpMenuWindowLevel)
        self._popup.setCollectionBehavior_(1 | 8 | 256)
        self._popup.setHasShadow_(True)
        self._popup.setOpaque_(False)
        self._popup.setBackgroundColor_(NSColor.clearColor())
        self._popup.setContentView_(self._vc.view())
        self._event_monitor = None

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
        if self._popup.isVisible():
            self._hide_popup()
        else:
            self._show_popup()

    @objc.python_method
    def _show_popup(self):
        btn = self._nsapp.nsstatusitem.button()
        btn_win = btn.window()
        if btn_win is None:
            return
        btn_rect = btn_win.convertRectToScreen_(
            btn.convertRect_toView_(btn.bounds(), None)
        )
        W, H = 300, 190
        x = btn_rect.origin.x + btn_rect.size.width - W
        y = btn_rect.origin.y - H
        self._popup.setFrameOrigin_((x, y))
        self._popup.orderFrontRegardless()

        def on_outside_click(event):
            loc = NSEvent.mouseLocation()
            b = self._nsapp.nsstatusitem.button()
            bw = b.window()
            if bw:
                br = bw.convertRectToScreen_(b.convertRect_toView_(b.bounds(), None))
                if (br.origin.x <= loc.x <= br.origin.x + br.size.width and
                        br.origin.y <= loc.y <= br.origin.y + br.size.height):
                    return  # click on status button — let toggle_popover handle it
            self._hide_popup()

        self._event_monitor = NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(
            (1 << 1) | (1 << 3),  # LeftMouseDown | RightMouseDown
            on_outside_click,
        )

    @objc.python_method
    def _hide_popup(self):
        self._popup.orderOut_(None)
        if self._event_monitor:
            NSEvent.removeMonitor_(self._event_monitor)
            self._event_monitor = None

    def advance(self):
        if not self._deck:
            self._deck = list(range(len(SNIPPETS)))
            random.shuffle(self._deck)
        self._current = self._deck.pop()
        self._vc.update(SNIPPETS[self._current])


if __name__ == "__main__":
    CoffeeBuddyApp().run()
