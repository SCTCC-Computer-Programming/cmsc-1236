"""
Realm of Pytha — Party Management Module
CMSC 1236 — Week 6 Assignment
"""


CHARACTER_RECORDS = [
    ("Aldric", "Warrior", 12, "Slash", "Shield Bash", "War Cry", 340),
    ("Lyra", "Mage", 10, "Fireball", "Ice Shard", "Teleport", "Mana Shield", 180),
    ("Finn", "Rogue", 8, "Backstab", "Stealth", 210),
    ("Sera", "Cleric", 11, "Heal", "Smite", "Resurrect", 250),
    ("Kael", "Ranger", 9, "Arrow Shot", "Trap", "Eagle Eye", "Camouflage", "Volley", 220),
]

LOOT_DROPS = [
    ("Shadow Dagger", "Rare", 450, "Enchanted", "Lifesteal"),
    ("Iron Helm", "Common", 80),
    ("Phoenix Staff", "Legendary", 1200, "Fire Damage", "Self-Repair", "Soulbound"),
    ("Leather Boots", "Common", 45),
    ("Emerald Amulet", "Rare", 600, "Poison Resist"),
    ("Obsidian Shield", "Epic", 870, "Thorns"),
]

INVENTORY_WEIGHTS = {
    "Shadow Dagger": 3.2,
    "Iron Helm": 8.5,
    "Phoenix Staff": 6.1,
    "Leather Boots": 2.4,
    "Emerald Amulet": 0.8,
    "Obsidian Shield": 14.7,
    "Health Potion": 1.0,
    "Mana Potion": 1.0,
    "Iron Sword": 7.3,
    "Travel Rations": 4.5,
}

WEIGHT_LIMIT = 5.0

ALDRIC_INVENTORY = ["Iron Sword", "Health Potion", "Iron Helm", "Travel Rations"]
LYRA_INVENTORY = ["Phoenix Staff", "Mana Potion", "Emerald Amulet"]


class Character:
    """An RPG character with a name, class, level, skills, and health."""
    pass


def parse_characters(records):
    """Create Character instances from variable-length record tuples."""
    pass


def parse_loot_drops(drops):
    """Parse loot drop tuples into structured dictionaries."""
    pass


def find_heavy_items(weights, limit):
    """Find items that exceed the weight limit and compute the excess."""
    pass


def combine_inventories(inv_a, inv_b):
    """Return a combined inventory without modifying the originals."""
    pass


def display_party(party):
    """Display all characters in the party."""
    print(f"\n  {'Name':<12}{'Class':<12}{'Level':<8}{'Health':<10}{'Skills'}")
    print("  " + "-" * 60)
    for c in party:
        skills = ", ".join(c.skills)
        print(f"  {c.name:<12}{c.char_class:<12}{c.level:<8}{c.health:<10}{skills}")
    print()


def display_loot(loot):
    """Display parsed loot drops in a formatted table."""
    print(f"\n  {'Item':<20}{'Rarity':<14}{'Value':<10}{'Tags'}")
    print("  " + "-" * 56)
    for item in loot:
        tags = ", ".join(item["tags"]) if item["tags"] else "(none)"
        print(f"  {item['name']:<20}{item['rarity']:<14}{item['value']:<10}{tags}")
    print()


def display_heavy_items(items):
    """Display items that exceed the weight limit."""
    if not items:
        print("  No items exceed the weight limit.")
    else:
        print(f"\n  {'Item':<20}{'Weight':<12}{'Excess'}")
        print("  " + "-" * 40)
        for name, weight, excess in items:
            print(f"  {name:<20}{weight:<12.1f}{excess:.1f}")
    print()


def display_inventory(label, inventory):
    """Display an inventory list with a label."""
    print(f"  {label}:")
    for i, item in enumerate(inventory, 1):
        print(f"    {i}. {item}")
    print()


def main():
    print("=" * 58)
    print(f"{'Realm of Pytha — Party Management Module':^58}")
    print("=" * 58)

    print(f"\n[1] ASSEMBLING THE PARTY")
    print("-" * 58)
    try:
        party = parse_characters(CHARACTER_RECORDS)
        if party:
            print(f"  Recruited {len(party)} characters.")
            display_party(party)
            for c in party:
                print(f"  {c}")
        else:
            print("  No characters created.")
    except Exception as e:
        print(f"  ERROR: {type(e).__name__}: {e}")
        party = None

    print(f"\n[2] SORTING LOOT DROPS")
    print("-" * 58)
    try:
        loot = parse_loot_drops(LOOT_DROPS)
        if loot:
            print(f"  Found {len(loot)} items.")
            display_loot(loot)
        else:
            print("  No loot parsed.")
    except Exception as e:
        print(f"  ERROR: {type(e).__name__}: {e}")

    print(f"\n[3] CHECKING ENCUMBRANCE")
    print("-" * 58)
    try:
        heavy = find_heavy_items(INVENTORY_WEIGHTS, WEIGHT_LIMIT)
        if heavy is not None:
            print(f"  Weight limit: {WEIGHT_LIMIT} lbs")
            display_heavy_items(heavy)
        else:
            print("  No results returned.")
    except Exception as e:
        print(f"  ERROR: {type(e).__name__}: {e}")

    print(f"\n[4] COMBINING PARTY INVENTORY")
    print("-" * 58)
    try:
        print(f"  Aldric's inventory before combining:")
        display_inventory("Aldric", ALDRIC_INVENTORY)
        print(f"  Lyra's inventory before combining:")
        display_inventory("Lyra", LYRA_INVENTORY)

        combined = combine_inventories(ALDRIC_INVENTORY, LYRA_INVENTORY)

        if combined:
            display_inventory("Combined party inventory", combined)
            print(f"  Aldric's inventory after combining:")
            display_inventory("Aldric", ALDRIC_INVENTORY)
        else:
            print("  No combined inventory returned.")
    except Exception as e:
        print(f"  ERROR: {type(e).__name__}: {e}")

    print("=" * 58)
    print("PARTY MANAGEMENT COMPLETE")
    print("=" * 58)


if __name__ == "__main__":
    main()
