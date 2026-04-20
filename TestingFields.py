import json

# --- CONFIG: cards you want to test ---
TEST_CARDS = [
    "Nicol Bolas, Planeswalker",
    "The Eldest Reborn",
    "Smothering Tithe",
    "Fire // Ice",
    "Valakut Awakening",
]

def normalize_card(c):
    return {
        "name": c.get("name"),
        "manaCost": c.get("manaCost"),
        "convertedManaCost": c.get("convertedManaCost"),
        "colors": c.get("colors", []),
        "types": c.get("types", []),
        "subtypes": c.get("subtypes"),
        "supertypes": c.get("supertypes"),
        "text": c.get("text"),
        "rarity": c.get("rarity"),
        "purchaseUrls": c.get("purchaseUrls", {})
    }

print("Loading JSON...")

with open("AtomicCards.json", "r", encoding="utf-8") as f:
    raw = json.load(f)

data = raw["data"]

print("\n=== RAW DATA (simulating raw SQL rows) ===\n")

raw_cards = []

for name in TEST_CARDS:
    if name not in data:
        print(f"[!] Missing: {name}")
        continue

    c = data[name][0]
    raw_cards.append(c)

    print(f"\n--- {name} ---")
    print(json.dumps(c, indent=2))


input("\n\nPress ENTER to clean and compare...\n")

print("\n=== CLEANED DATA ===\n")

for c in raw_cards:
    cleaned = normalize_card(c)

    print(f"\n--- {cleaned['name']} ---")
    print(json.dumps(cleaned, indent=2))

print("\nDone.")