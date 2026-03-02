"""
Space Trader — Docking Sequence
Main program — DO NOT MODIFY

This program runs an automated docking sequence at Nexus Station.
It imports the cargo module and calls each function to process
incoming cargo shipments.
"""

from cargo_module import (
    CargoPod,
    load_cargo,
    classify_cargo,
    scan_for_contraband,
    apply_tariffs,
    generate_manifest,
    filter_cargo_by_destination,
)

# ============================================================
#  CARGO DATA
# ============================================================

CARGO_RECORDS = [
    ("Plasma Coils", "tech", 4, 2.5, "Nexus Station", "fragile", "high-value"),
    ("", "food", 10, 1.0, "Outpost Zeta"),
    ("Iron Ore", "minerals", 20, 8.0, "Forge World", "bulk"),
    ("Dried Rations", "food", 15, 0.5, "Nexus Station"),
    ("Blaster Rifles", "weapons", 6, 3.5, "Nexus Station", "restricted"),
    ("Crystal Shards", "luxury", 8, 0.3, "Velaris Hub", "fragile", "rare", "insured"),
    ("Med Kits", "tech", 0, 1.5, "Outpost Zeta", "urgent"),
    ("Titanium Plates", "minerals", 12, 6.0, "Forge World", "bulk", "heavy"),
    ("Freeze-Dried Fruit", "food", 25, 0.4, "Velaris Hub"),
]

BANNED_ITEMS = ["Nerve Gas Canisters", "Blaster Rifles", "Dark Matter Vials"]

CARGO_PRICES = [120.00, 480.00, 45.50, 288.00, 36.00, 432.00, 75.00]

TARIFF_RATE = 0.15
TARIFF_THRESHOLD = 50.00


# ============================================================
#  DISPLAY FUNCTIONS
# ============================================================

def print_header():
    print("=" * 58)
    print(f"{'Space Trader — Docking Sequence':^58}")
    print("=" * 58)


def print_section(number, title):
    print(f"\n[{number}] {title}")
    print("-" * 58)


def display_cargo(pods):
    print(f"  Loaded {len(pods)} cargo pods.\n")
    print(f"  {'Name':<22}{'Category':<12}{'Qty':<6}{'Weight':<10}{'Destination'}")
    print(f"  {'-' * 66}")
    for pod in pods:
        print(f"  {pod.name:<22}{pod.category:<12}{pod.quantity:<6}"
              f"{pod.unit_weight:<10}{pod.destination}")
    print()
    print("  Cargo flags:")
    for pod in pods:
        tag_str = ", ".join(pod.tags) if pod.tags else "(none)"
        print(f"    {pod.name}: {tag_str}")
    print()
    print("  Cargo log:")
    for pod in pods:
        print(f"    {pod}")


def display_classifications(classifications):
    print(f"\n  {'Cargo':<22}{'Handling Instructions'}")
    print(f"  {'-' * 50}")
    for name, instruction in classifications:
        print(f"  {name:<22}{instruction}")


def display_scan_result(result):
    found, message = result
    if found:
        print(f"  WARNING: {message}")
    else:
        print(f"  OK: {message}")


def display_prices(label, prices):
    print(f"\n  {label}:")
    for i, price in enumerate(prices, 1):
        print(f"    {i}. ${price:.2f}")


def display_manifest(manifest):
    print(f"\n  {'#':<4}{'Item':<22}{'Price':<12}{'Destination'}")
    print(f"  {'-' * 54}")
    for num, name, price, dest in manifest:
        print(f"  {num:<4}{name:<22}${price:<11.2f}{dest}")


def display_filtered(pods, destination):
    print(f"\n  Cargo bound for {destination} ({len(pods)} pods):")
    if pods:
        for pod in pods:
            print(f"    - {pod.name} ({pod.quantity}x {pod.category}, "
                  f"{pod.total_weight()} lbs total)")
    else:
        print("    (none)")


def print_footer():
    print("\n" + "=" * 58)
    print("DOCKING SEQUENCE COMPLETE")
    print("=" * 58)


# ============================================================
#  MAIN DOCKING SEQUENCE
# ============================================================

def main():
    print_header()

    # --- Section 1: Load cargo ---
    print_section(1, "LOADING CARGO")
    pods = load_cargo(CARGO_RECORDS)
    display_cargo(pods)

    # --- Section 2: Classify cargo ---
    print_section(2, "CLASSIFYING CARGO")
    classifications = classify_cargo(pods)
    display_classifications(classifications)

    # --- Section 3: Contraband scan ---
    print_section(3, "CONTRABAND SCAN")
    result = scan_for_contraband(pods, BANNED_ITEMS)
    display_scan_result(result)

    # --- Section 4: Apply tariffs ---
    print_section(4, "APPLYING STATION TARIFFS")
    prices = CARGO_PRICES.copy()
    print(f"  Tariff rate: {TARIFF_RATE:.0%}")
    print(f"  Threshold: ${TARIFF_THRESHOLD:.2f} (items at or below are exempt)")
    display_prices("Prices before tariff", prices)
    apply_tariffs(prices, TARIFF_RATE, TARIFF_THRESHOLD)
    display_prices("Prices after tariff", prices)

    # --- Section 5: Generate docking manifest ---
    print_section(5, "GENERATING DOCKING MANIFEST")
    names = [pod.name for pod in pods]
    destinations = [pod.destination for pod in pods]
    manifest = generate_manifest(names, prices, destinations)
    display_manifest(manifest)

    # --- Section 6: Priority unloading ---
    print_section(6, "PRIORITY UNLOADING")
    nexus_pods = filter_cargo_by_destination(pods, "Nexus Station")
    display_filtered(nexus_pods, "Nexus Station")
    forge_pods = filter_cargo_by_destination(pods, "Forge World")
    display_filtered(forge_pods, "Forge World")

    print_footer()


if __name__ == "__main__":
    main()
