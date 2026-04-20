import json

INPUT_FILE = "AtomicCards.json"
OUTPUT_FILE = "cleaned_cards.json"

BATCH_SIZE = 100


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


print("Loading source JSON (read-only)...")

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    raw = json.load(f)

data = raw["data"]

print(f"Total cards in dataset: {len(data)}")

# Open output file safely
with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
    out.write("[\n")  # start JSON array

    first = True
    count = 0

    for name, versions in data.items():
        if not versions:
            continue

        c = versions[0]
        cleaned = normalize_card(c)

        # Write JSON safely with commas
        if not first:
            out.write(",\n")
        else:
            first = False

        json.dump(cleaned, out, ensure_ascii=False)

        count += 1

        # Progress checkpoint every 100 cards
        if count % BATCH_SIZE == 0:
            print(f"Processed {count} cards...")

    out.write("\n]")  # close JSON array

print(f"\nDone. Total cleaned cards: {count}")