"""
cargo_module.py — Space Trader Cargo Module (solution)
"""


class CargoPod:
    def __init__(self, name, category, quantity, unit_weight, destination):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.unit_weight = unit_weight
        self.destination = destination

    def __str__(self):
        return (f"{self.name}: {self.quantity}x {self.category} "
                f"({self.unit_weight} lbs each) -> {self.destination}")


def load_cargo(records):
    pods = []
    for name, category, quantity, unit_weight, destination in records:
        if name and quantity:
            pods.append(CargoPod(name, category, quantity, unit_weight, destination))
    return pods


def classify_cargo(pods):
    results = []
    for pod in pods:
        match pod.category:
            case "weapons":
                instruction = "Restricted - Secure Hold"
            case "food":
                instruction = "Perishable - Cold Storage"
            case "tech":
                instruction = "Fragile - Padded Bay"
            case "minerals":
                instruction = "Heavy - Lower Deck"
            case _:
                instruction = "Standard Storage"
        results.append((pod.name, instruction))
    return results


def scan_for_contraband(pods, banned_items):
    for pod in pods:
        if pod.name in banned_items:
            return (True, f"Contraband detected: {pod.name}")
    else:
        return (False, "Cargo scan clear")


def apply_tariffs(prices, rate):
    for i in range(len(prices)):
        prices[i] = round(prices[i] * (1 + rate), 2)
    return prices


def generate_manifest(names, prices, destinations):
    manifest = []
    for num, (name, price, dest) in enumerate(zip(names, prices, destinations), 1):
        manifest.append((num, name, price, dest))
    return manifest


def filter_cargo_by_destination(pods, destination):
    return [pod for pod in pods if pod.destination == destination]
