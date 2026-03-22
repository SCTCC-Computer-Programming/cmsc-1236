from lastname_wildlife_survey import (
    count_observations,
    find_species,
    flatten_survey,
    apply_formula,
    get_notable_species,
    format_report_lines,
)

# -------------------------------------------------------------------
# Survey data: nested lists representing regions > zones > sub-zones.
# Integers are raw observation counts. Strings are species sightings.
# -------------------------------------------------------------------

SURVEY_DATA = [
    [12, 5, [3, 8, [2, 6]], 4],
    ["Red-tailed Hawk", 9, ["Sandhill Crane", 3, [7, "Red-tailed Hawk"]]],
    [["Bald Eagle", 5, [2, 3]], 11, ["Sandhill Crane", [4, 6, ["Bald Eagle", 1]]]],
]

TEMPERATURE_READINGS = [32.0, 18.5, 25.0, 41.2, 15.8, 30.0]

SPECIES_RECORDS = [
    ("Red-tailed Hawk",  47, "Northern Region"),
    ("Sandhill Crane",   12, "Wetlands Zone"),
    ("Bald Eagle",       31, "River Corridor"),
    ("Great Horned Owl", 8,  "Forest Reserve"),
    ("Peregrine Falcon", 53, "Coastal Strip"),
    ("Osprey",           19, "River Corridor"),
    ("Snowy Owl",        6,  "Northern Region"),
    ("Cooper's Hawk",    28, "Forest Reserve"),
]


# -------------------------------------------------------------------
# Conversion formula (passed to apply_formula as a function argument)
# -------------------------------------------------------------------

def celsius_to_fahrenheit(c):
    return round(c * 9 / 5 + 32, 1)


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


def display_count(total):
    print(f"  Total observations recorded: {total}")
    print()


def display_search_results(target, results):
    print(f"  Search target: {target!r}")
    if results:
        print(f"  Found {len(results)} occurrence(s) across all survey zones.")
    elif results is None:
        print("  (not yet implemented)")
    else:
        print("  No occurrences found.")
    print()


def display_flat_survey(flat):
    if flat is None:
        print("  (not yet implemented)")
        print()
        return
    print(f"  Flattened survey contains {len(flat)} entries:")
    integers = [x for x in flat if isinstance(x, int)]
    strings  = [x for x in flat if isinstance(x, str)]
    print(f"    Observation counts : {integers}")
    print(f"    Species sightings  : {strings}")
    print()


def display_conversions(original, converted):
    if converted is None:
        print("  (not yet implemented)")
        print()
        return
    print(f"  {'Reading (C)':<16} {'Converted (F)'}")
    print(f"  {'-'*30}")
    for c, f in zip(original, converted):
        print(f"  {c:<16} {f}")
    print()


def display_notable(lines, threshold):
    print(f"  Species with more than {threshold} observations:")
    print(f"  {'Species':<22} {'Count':<8} {'Region'}")
    print(f"  {'-'*50}")
    if lines:
        for line in lines:
            print(line)
    else:
        print("  (none)")
    print()


# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

def main():
    display_header("Wildlife Survey Analyzer")

    display_section(1, "TOTAL OBSERVATION COUNT")
    total = count_observations(SURVEY_DATA)
    display_count(total)

    display_section(2, "SPECIES SEARCH")
    target = "Red-tailed Hawk"
    results = find_species(SURVEY_DATA, target)
    display_search_results(target, results)

    target2 = "Bald Eagle"
    results2 = find_species(SURVEY_DATA, target2)
    display_search_results(target2, results2)

    target3 = "Golden Eagle"
    results3 = find_species(SURVEY_DATA, target3)
    display_search_results(target3, results3)

    display_section(3, "FLATTENED SURVEY DATA")
    flat = flatten_survey(SURVEY_DATA)
    display_flat_survey(flat)

    display_section(4, "TEMPERATURE CONVERSION")
    converted = apply_formula(celsius_to_fahrenheit, TEMPERATURE_READINGS)
    display_conversions(TEMPERATURE_READINGS, converted)

    display_section(5, "NOTABLE SPECIES (threshold: 25)")
    threshold = 25
    notable = get_notable_species(SPECIES_RECORDS, threshold)
    lines = format_report_lines(notable)
    display_notable(lines, threshold)

    print("=" * 58)
    print("  SURVEY ANALYSIS COMPLETE")
    print("=" * 58)


if __name__ == "__main__":
    main()
