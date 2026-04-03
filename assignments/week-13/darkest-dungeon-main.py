from darkest_dungeon_solution import (
    get_hero_skills,
    get_unique_afflictions,
    build_hero_profiles,
    search_dungeon,
    generate_drops,
    format_drop_display,
)

# -------------------------------------------------------------------
# Game data
# -------------------------------------------------------------------

ROSTER = [
    {"name": "Plague Doctor", "stress": 45, "affliction": "None",        "skills": ["Battlefield Medicine", "Blinding Gas", "Disorienting Blast"]},
    {"name": "Highwayman",    "stress": 72, "affliction": "Masochistic",  "skills": ["Pistol Shot", "Duelist's Advance", "Open Vein"]},
    {"name": "Crusader",      "stress": 30, "affliction": "None",         "skills": ["Smite", "Stunning Blow", "Inspiring Cry"]},
    {"name": "Vestal",        "stress": 85, "affliction": "Paranoid",     "skills": ["Divine Grace", "Judgment", "Hand of Light"]},
    {"name": "Grave Robber",  "stress": 55, "affliction": "None",         "skills": ["Lunge", "Shadow Fade", "Thrown Dagger"]},
    {"name": "Hellion",       "stress": 20, "affliction": "Hopeless",     "skills": ["If It Bleeds", "Iron Swan", "Barbaric YAWP!"]},
]

DUNGEON = [
    "Gold Coins",
    ["Antique Chest", ["Bust", "Crimson Court Invitation"]],
    "Torch",
    ["Curio", "Old Rune"],
    "Warrens Map",
    ["Hidden Alcove", ["Ancestor's Memento", ["Gold Coins", "Medical Supplies"]]],
]

CHEST_CONTENTS = [
    ("Gold Coins",               150),
    ("",                           0),
    ("Ancestral Portrait",       300),
    ("Medical Supplies",           0),
    ("Crimson Court Invitation", 500),
    ("Bust",                     200),
    (None,                         0),
]

STRESS_THRESHOLD = 55
GOLD_THRESHOLD   = 100


# -------------------------------------------------------------------
# Display functions (do not modify)
# -------------------------------------------------------------------

def display_header(title):
    print("=" * 58)
    print(f"  {title}")
    print("=" * 58)
    print()


def display_section(number, title):
    print(f"[{number}] {title}")
    print("-" * 58)


def display_skills(skills):
    if skills is None:
        print("  (not yet implemented)")
        print()
        return
    print(f"  {len(skills)} available skill(s):")
    for skill in skills:
        print(f"    - {skill}")
    print()


def display_afflictions(afflictions):
    if afflictions is None:
        print("  (not yet implemented)")
        print()
        return
    print(f"  Active afflictions across the party:")
    for a in sorted(afflictions):
        print(f"    {a}")
    print()


def display_profiles(profiles):
    if profiles is None:
        print("  (not yet implemented)")
        print()
        return
    print(f"  {'Hero':<22} {'Stress':<10} {'Affliction'}")
    print(f"  {'-'*50}")
    for name, (stress, affliction) in profiles.items():
        print(f"  {name:<22} {stress:<10} {affliction}")
    print()


def display_search(target, results):
    if results is None:
        print("  (not yet implemented)")
        print()
        return
    print(f"  Searching for: {target!r}")
    if results:
        print(f"  Found {len(results)} occurrence(s).")
    else:
        print("  Not found.")
    print()


def display_drops(drops):
    if drops is None:
        print("  (not yet implemented)")
        print()
        return
    drop_list = list(drops)
    if not drop_list:
        print("  (chest is empty or not yet implemented)")
        print()
        return
    print(f"  {len(drop_list)} item(s) collected:")
    for item in drop_list:
        print(f"    {item}")
    print()


def display_formatted_drops(lines):
    if lines is None:
        print("  (not yet implemented)")
        print()
        return
    line_list = list(lines)
    if not line_list:
        print("  (no items above threshold or not yet implemented)")
        print()
        return
    print(f"  {'Item':<30} {'Value'}")
    print(f"  {'-'*42}")
    for line in line_list:
        print(line)
    print()


# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

def main():
    display_header("Darkest Dungeon — Guild Management")

    display_section(1, f"AVAILABLE SKILLS (stress <= {STRESS_THRESHOLD})")
    skills = get_hero_skills(ROSTER, STRESS_THRESHOLD)
    display_skills(skills)

    display_section(2, "PARTY AFFLICTIONS")
    afflictions = get_unique_afflictions(ROSTER)
    display_afflictions(afflictions)

    display_section(3, "HERO PROFILES")
    profiles = build_hero_profiles(ROSTER)
    display_profiles(profiles)

    display_section(4, "DUNGEON SEARCH")
    target = "Gold Coins"
    results = search_dungeon(DUNGEON, target)
    display_search(target, results)

    target2 = "Ancestor's Memento"
    results2 = search_dungeon(DUNGEON, target2)
    display_search(target2, results2)

    target3 = "Holy Water"
    results3 = search_dungeon(DUNGEON, target3)
    display_search(target3, results3)

    display_section(5, "CHEST DROPS")
    drops = generate_drops(CHEST_CONTENTS)
    display_drops(drops)

    display_section(6, f"VALUABLE LOOT (gold > {GOLD_THRESHOLD})")
    formatted = format_drop_display(CHEST_CONTENTS, GOLD_THRESHOLD)
    display_formatted_drops(formatted)

    print("=" * 58)
    print("  EXPEDITION COMPLETE")
    print("=" * 58)


if __name__ == "__main__":
    main()
