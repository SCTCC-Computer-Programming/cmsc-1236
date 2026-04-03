# Week 13 Solution - Instructor Reference Only

# -------------------------------------------------------------------
# Sample data for testing
# -------------------------------------------------------------------

ROSTER = [
    {"name": "Plague Doctor", "stress": 45, "affliction": "None",       "skills": ["Battlefield Medicine", "Blinding Gas", "Disorienting Blast"]},
    {"name": "Highwayman",    "stress": 72, "affliction": "Masochistic", "skills": ["Pistol Shot", "Duelist's Advance", "Open Vein"]},
    {"name": "Crusader",      "stress": 30, "affliction": "None",        "skills": ["Smite", "Stunning Blow", "Inspiring Cry"]},
    {"name": "Vestal",        "stress": 85, "affliction": "Paranoid",    "skills": ["Divine Grace", "Judgment", "Hand of Light"]},
    {"name": "Grave Robber",  "stress": 55, "affliction": "None",        "skills": ["Lunge", "Shadow Fade", "Thrown Dagger"]},
    {"name": "Hellion",       "stress": 20, "affliction": "Hopeless",    "skills": ["If It Bleeds", "Iron Swan", "Barbaric YAWP!"]},
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
    ("Gold Coins", 150),
    ("", 0),           # corrupted entry - skip
    ("Ancestral Portrait", 300),
    ("Medical Supplies", 0),  # zero value - skip  
    ("Crimson Court Invitation", 500),
    ("Bust", 200),
    (None, 0),         # corrupted entry - skip
]

GOLD_THRESHOLD = 100


# -------------------------------------------------------------------
# Student functions
# -------------------------------------------------------------------

def get_hero_skills(roster, max_stress):
    """
    Return a flat list of all skills belonging to heroes whose stress
    is at or below max_stress.

    Requires a list comprehension with a nested for clause and an if filter.
    The outer loop iterates over heroes, the if clause filters by stress,
    and the inner loop collects each skill from the qualifying hero's skill list.
    """
    return [skill for hero in roster if hero["stress"] <= max_stress
            for skill in hero["skills"]]


def get_unique_afflictions(roster):
    """
    Return a set of all unique afflictions present in the roster.
    Heroes with no affliction will have the string "None".
    """
    return {hero["affliction"] for hero in roster}


def build_hero_profiles(roster):
    """
    Return a dictionary mapping each hero's name to a tuple of
    (stress, affliction).
    """
    return {hero["name"]: (hero["stress"], hero["affliction"])
            for hero in roster}


def search_dungeon(area, target):
    """
    Recursively search a nested dungeon structure for all occurrences
    of target. Returns a flat list of matches found at any depth.

    area is a list that may contain strings or nested lists.
    Uses isinstance() to determine whether each item needs further searching.
    """
    results = []
    for item in area:
        if isinstance(item, list):
            results.extend(search_dungeon(item, target))
        elif item == target:
            results.append(item)
    return results


def generate_drops(chest_contents):
    """
    Yield loot drop names one at a time from chest_contents.
    Each entry is a (name, gold_value) tuple.
    Skip entries where the name is falsy (empty string or None).
    """
    for name, value in chest_contents:
        if name:
            yield name


def format_drop_display(drops_gen, gold_threshold):
    """
    Return a generator expression that formats drop entries for display,
    keeping only drops whose gold value exceeds gold_threshold.

    drops_gen yields (name, value) tuples.
    Format each as: "  {name:<30} {value} gp"
    """
    return (f"  {name:<30} {value} gp"
            for name, value in drops_gen
            if value > gold_threshold)


# -------------------------------------------------------------------
# Quick test
# -------------------------------------------------------------------

if __name__ == "__main__":
    print("=== get_hero_skills (max_stress=55) ===")
    skills = get_hero_skills(ROSTER, 55)
    for s in skills:
        print(f"  {s}")

    print("\n=== get_unique_afflictions ===")
    print(f"  {get_unique_afflictions(ROSTER)}")

    print("\n=== build_hero_profiles ===")
    for name, profile in build_hero_profiles(ROSTER).items():
        print(f"  {name}: stress={profile[0]}, affliction={profile[1]}")

    print("\n=== search_dungeon (target='Gold Coins') ===")
    print(f"  Found: {search_dungeon(DUNGEON, 'Gold Coins')}")

    print("\n=== generate_drops ===")
    for drop in generate_drops(CHEST_CONTENTS):
        print(f"  {drop}")

    print("\n=== format_drop_display (threshold=100) ===")
    display = format_drop_display(iter(CHEST_CONTENTS), GOLD_THRESHOLD)
    for line in display:
        print(line)
