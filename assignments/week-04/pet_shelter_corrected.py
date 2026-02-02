"""
Pet Shelter Adoption Tracker - CORRECTED VERSION
All 5 bugs have been fixed.
"""

import copy
import random


SHELTER_NAME = "Sunshine Animal Shelter"
DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
FEEDING_TIMES = ["Morning", "Midday", "Evening"]
SPECIES_TYPES = ["Dog", "Cat", "Rabbit"]


class Pet:
    
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        self.medical_history = []
        self.traits = {"vaccinated": False, "neutered": False, "microchipped": False}
    
    def summary(self):
        return f"{self.name} ({self.species}, {self.age} yrs)"
    
    def add_medical_record(self, record):
        self.medical_history.append(record)
    
    def update_trait(self, trait, value):
        if trait in self.traits:
            self.traits[trait] = value


def display_banner():
    width = 50
    print("=" * width)
    print(f"{SHELTER_NAME:^{width}}")
    print("=" * width)
    print()


def format_pet_list(pets):
    if not pets:
        return "  (no pets)"
    lines = []
    for i, pet in enumerate(pets, 1):
        lines.append(f"  {i}. {pet.summary()}")
    return "\n".join(lines)


def calculate_food_cost(num_pets, cost_per_pet=3.50):
    return num_pets * cost_per_pet


def get_random_trait_status():
    return random.choice([True, False])


def validate_pet_data(pet):
    if not pet.name or len(pet.name) < 1:
        return False
    if pet.species not in SPECIES_TYPES:
        return False
    if pet.age < 0:
        return False
    return True


def create_sample_pets():
    pets = [
        Pet("Buddy", "Dog", 3),
        Pet("Whiskers", "Cat", 5),
        Pet("Hoppy", "Rabbit", 2),
        Pet("Luna", "Cat", 4),
        Pet("Max", "Dog", 6)
    ]
    
    pets[0].add_medical_record("Checkup: 2024-01-15 - Healthy")
    pets[0].update_trait("vaccinated", True)
    pets[0].update_trait("neutered", True)
    
    pets[1].add_medical_record("Checkup: 2024-02-20 - Healthy")
    pets[1].add_medical_record("Dental: 2024-03-10 - Cleaning performed")
    pets[1].update_trait("vaccinated", True)
    
    pets[2].add_medical_record("Checkup: 2024-01-05 - Healthy")
    
    pets[3].add_medical_record("Checkup: 2024-03-01 - Minor ear infection")
    pets[3].add_medical_record("Follow-up: 2024-03-15 - Recovered")
    pets[3].update_trait("vaccinated", True)
    pets[3].update_trait("microchipped", True)
    
    pets[4].add_medical_record("Checkup: 2024-02-28 - Healthy")
    pets[4].update_trait("vaccinated", True)
    pets[4].update_trait("neutered", True)
    pets[4].update_trait("microchipped", True)
    
    return pets


# FIX 1: Use .copy() to create independent list
def copy_available_pets(shelter_pets):
    event_pets = shelter_pets.copy()
    return event_pets


# FIX 2: Use list comprehension to create independent inner lists
def create_feeding_schedule(num_pets):
    portions_per_slot = num_pets
    weekly_schedule = [[portions_per_slot] * len(FEEDING_TIMES) for _ in range(len(DAYS_OF_WEEK))]
    return weekly_schedule


# FIX 3: Use deepcopy to copy nested mutable objects
def backup_pet_profile(pet):
    backup = copy.deepcopy(pet)
    return backup


# FIX 4: Use None as default, create new list inside function
def register_adoption(pet_name, adopter_name, notes=None):
    if notes is None:
        notes = []
    notes.append(f"Adopted by: {adopter_name}")
    notes.append(f"Date: 2024-04-01")
    
    record = {
        "pet": pet_name,
        "adopter": adopter_name,
        "notes": notes
    }
    return record


# FIX 5: Compare attributes with == instead of using 'is'
def find_duplicate_profiles(pet_a, pet_b):
    if pet_a.name == pet_b.name and pet_a.species == pet_b.species and pet_a.age == pet_b.age:
        return True
    return False


def print_feeding_schedule(schedule):
    print(f"\n{'WEEKLY FEEDING SCHEDULE':^50}")
    print("-" * 50)
    
    header = f"{'Day':<12}"
    for time in FEEDING_TIMES:
        header += f"{time:^12}"
    print(header)
    print("-" * 50)
    
    for i, day in enumerate(DAYS_OF_WEEK):
        row = f"{day:<12}"
        for portions in schedule[i]:
            row += f"{portions:^12}"
        print(row)


def print_pet_details(pet):
    print(f"\n  Name: {pet.name}")
    print(f"  Species: {pet.species}")
    print(f"  Age: {pet.age} years")
    print(f"  Traits: {pet.traits}")
    print(f"  Medical History ({len(pet.medical_history)} records):")
    if pet.medical_history:
        for record in pet.medical_history:
            print(f"    - {record}")
    else:
        print("    (no records)")


def main():
    display_banner()
    
    print("[1] INITIALIZING SHELTER")
    print("-" * 50)
    shelter_pets = create_sample_pets()
    print(f"Loaded {len(shelter_pets)} pets into the system.\n")
    
    print("[2] PREPARING ADOPTION EVENT")
    print("-" * 50)
    print("Creating pet list for weekend adoption event...")
    event_pets = copy_available_pets(shelter_pets)
    print(f"Event coordinator received {len(event_pets)} pets.\n")
    
    new_pet = Pet("Charlie", "Dog", 2)
    new_pet.add_medical_record("Intake exam: 2024-04-01 - Healthy")
    event_pets.append(new_pet)
    print(f"Event coordinator added new pet: {new_pet.summary()}")
    
    print(f"\nShelter roster ({len(shelter_pets)} pets):")
    print(format_pet_list(shelter_pets))
    print(f"\nEvent roster ({len(event_pets)} pets):")
    print(format_pet_list(event_pets))
    
    print("\n[3] CREATING FEEDING SCHEDULE")
    print("-" * 50)
    num_current_pets = len(shelter_pets)
    schedule = create_feeding_schedule(num_current_pets)
    print(f"Created feeding schedule for {num_current_pets} pets.")
    print_feeding_schedule(schedule)
    
    print("\n\nUpdating Wednesday evening for special dietary needs...")
    schedule[2][2] = 10
    print("Set Wednesday evening portions to 10.")
    print_feeding_schedule(schedule)
    
    print("\n[4] BACKING UP PET PROFILE")
    print("-" * 50)
    original_pet = shelter_pets[1]
    print(f"Creating backup of {original_pet.name}'s profile before transfer...")
    backup_pet = backup_pet_profile(original_pet)
    print("Backup created successfully.")
    
    print("\nOriginal profile:")
    print_pet_details(original_pet)
    print("\nBackup profile:")
    print_pet_details(backup_pet)
    
    print("\n\nAdding new medical record to BACKUP only...")
    backup_pet.add_medical_record("Transfer exam: 2024-04-02 - Cleared for transfer")
    
    print("\nOriginal profile after backup modification:")
    print_pet_details(original_pet)
    print("\nBackup profile after backup modification:")
    print_pet_details(backup_pet)
    
    print("\n[5] RECORDING ADOPTIONS")
    print("-" * 50)
    adoption_records = []
    
    print("Recording adoption for Hoppy...")
    record1 = register_adoption("Hoppy", "Sarah Johnson")
    adoption_records.append(record1)
    print(f"  Record created: {record1}")
    
    print("\nRecording adoption for Max...")
    record2 = register_adoption("Max", "Mike Chen")
    adoption_records.append(record2)
    print(f"  Record created: {record2}")
    
    print("\nRecording adoption for Luna...")
    record3 = register_adoption("Luna", "Emily Davis")
    adoption_records.append(record3)
    print(f"  Record created: {record3}")
    
    print("\n\nFinal adoption records:")
    for i, record in enumerate(adoption_records, 1):
        print(f"\n  Adoption #{i}:")
        print(f"    Pet: {record['pet']}")
        print(f"    Adopter: {record['adopter']}")
        print(f"    Notes: {record['notes']}")
    
    print("\n[6] CHECKING FOR DUPLICATE PROFILES")
    print("-" * 50)
    
    pet_x = Pet("Bella", "Dog", 3)
    pet_x.add_medical_record("Checkup: 2024-01-01")
    pet_x.update_trait("vaccinated", True)
    
    pet_y = Pet("Bella", "Dog", 3)
    pet_y.add_medical_record("Checkup: 2024-01-01")
    pet_y.update_trait("vaccinated", True)
    
    print(f"Pet X: {pet_x.summary()}")
    print(f"Pet Y: {pet_y.summary()}")
    print(f"Same name? {pet_x.name == pet_y.name}")
    print(f"Same species? {pet_x.species == pet_y.species}")
    print(f"Same age? {pet_x.age == pet_y.age}")
    
    is_duplicate = find_duplicate_profiles(pet_x, pet_y)
    
    if is_duplicate:
        print("\nResult: DUPLICATE FOUND - Profiles should be merged.")
    else:
        print("\nResult: NOT A DUPLICATE - Profiles are different pets.")
    
    print("\n" + "=" * 50)
    print("END OF DAILY OPERATIONS REPORT")
    print("=" * 50)


if __name__ == "__main__":
    main()
