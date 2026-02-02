"""
===============================================================================
PET SHELTER ADOPTION TRACKER - INSTRUCTOR VERSION
===============================================================================

This file contains 5 embedded bugs related to Chapters 8-9 concepts.
Each bug is marked with:
    - BUG #N marker
    - Concept violated
    - Why it's wrong
    - The fix

BUGS OVERVIEW:
    Bug 1: copy_available_pets()      - Aliasing (= doesn't copy)
    Bug 2: create_feeding_schedule()  - Nested list with * repetition
    Bug 3: backup_pet_profile()       - Shallow copy vs deep copy
    Bug 4: register_adoption()        - Mutable default argument
    Bug 5: find_duplicate_profiles()  - is vs == (identity vs equality)

===============================================================================
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


# ==============================================================================
# BUG 1: ALIASING
# ==============================================================================
# Concept: Assignment (=) does not copy a list; it creates an alias (two names
#          referring to the same object).
#
# What's wrong: event_pets = shelter_pets makes both names point to the SAME
#               list object. Any modification to one affects the other.
#
# Symptom: When Charlie is added to event_pets, he also appears in shelter_pets.
#
# Diagnostic clue: Both lists have the same id().
# ==============================================================================

def copy_available_pets(shelter_pets):
    # ----- BUGGY CODE -----
    event_pets = shelter_pets           # <-- BUG: Creates alias, not a copy
    return event_pets
    
    # ----- FIXED CODE -----
    # event_pets = shelter_pets.copy()  # Creates a new list (shallow copy)
    # return event_pets
    #
    # Alternative fixes:
    # event_pets = list(shelter_pets)   # Also creates a new list
    # event_pets = shelter_pets[:]      # Slice creates a new list


# ==============================================================================
# BUG 2: NESTED LIST WITH * REPETITION
# ==============================================================================
# Concept: Using * to repeat a list containing a mutable object creates multiple
#          references to the SAME inner object, not independent copies.
#
# What's wrong: [daily_schedule] * 7 creates a list with 7 references to the
#               SAME daily_schedule list. Changing one "day" changes all days.
#
# Symptom: Updating schedule[2][2] (Wednesday evening) changes the evening
#          slot for ALL days.
#
# Diagnostic clue: All rows have the same id().
# ==============================================================================

def create_feeding_schedule(num_pets):
    portions_per_slot = num_pets
    
    # ----- BUGGY CODE -----
    daily_schedule = [portions_per_slot] * len(FEEDING_TIMES)
    weekly_schedule = [daily_schedule] * len(DAYS_OF_WEEK)  # <-- BUG: Repeats same list reference
    return weekly_schedule
    
    # ----- FIXED CODE -----
    # Use a list comprehension to create independent inner lists:
    # weekly_schedule = [[portions_per_slot] * len(FEEDING_TIMES) for _ in range(len(DAYS_OF_WEEK))]
    # return weekly_schedule
    #
    # Why this works: The comprehension creates a NEW [portions_per_slot, ...]
    # list on each iteration, so each day has its own independent list.


# ==============================================================================
# BUG 3: SHALLOW COPY VS DEEP COPY
# ==============================================================================
# Concept: copy.copy() creates a shallow copy - a new outer object, but nested
#          mutable objects (like lists) are still shared references.
#
# What's wrong: copy.copy(pet) creates a new Pet object, but the new Pet's
#               medical_history attribute points to the SAME list as the original.
#
# Symptom: Adding a medical record to the backup also adds it to the original.
#
# Diagnostic clue: Both pets' medical_history have the same id().
# ==============================================================================

def backup_pet_profile(pet):
    # ----- BUGGY CODE -----
    backup = copy.copy(pet)             # <-- BUG: Shallow copy shares nested lists
    return backup
    
    # ----- FIXED CODE -----
    # backup = copy.deepcopy(pet)       # Deep copy creates independent nested objects
    # return backup
    #
    # Why this works: deepcopy() recursively copies all nested objects,
    # so medical_history becomes a completely independent list.


# ==============================================================================
# BUG 4: MUTABLE DEFAULT ARGUMENT
# ==============================================================================
# Concept: Default argument values are evaluated ONCE at function definition
#          time, not each time the function is called. If the default is a
#          mutable object (like a list), it's shared across all calls.
#
# What's wrong: notes=[] creates ONE list when the function is defined. Every
#               call that doesn't provide notes appends to that SAME list.
#
# Symptom: Each adoption record accumulates notes from ALL previous adoptions.
#          By the third adoption, the notes list has 6 items instead of 2.
#
# Diagnostic clue: All records' notes have the same id().
# ==============================================================================

def register_adoption(pet_name, adopter_name, notes=[]):  # <-- BUG: Mutable default
    notes.append(f"Adopted by: {adopter_name}")
    notes.append(f"Date: 2024-04-01")
    
    record = {
        "pet": pet_name,
        "adopter": adopter_name,
        "notes": notes
    }
    return record

    # ----- FIXED CODE -----
    # def register_adoption(pet_name, adopter_name, notes=None):
    #     if notes is None:
    #         notes = []                # Create a NEW list each time
    #     notes.append(f"Adopted by: {adopter_name}")
    #     notes.append(f"Date: 2024-04-01")
    #     
    #     record = {
    #         "pet": pet_name,
    #         "adopter": adopter_name,
    #         "notes": notes
    #     }
    #     return record
    #
    # Why this works: Using None as the default and creating a new list inside
    # the function ensures each call gets its own independent list.


# ==============================================================================
# BUG 5: IDENTITY VS EQUALITY (is vs ==)
# ==============================================================================
# Concept: 'is' tests identity (same object in memory), while '==' tests
#          equality (same value/contents).
#
# What's wrong: Two Pet objects with identical attributes are EQUAL (==) but
#               not IDENTICAL (is). Using 'is' to find duplicates will always
#               return False unless they're literally the same object.
#
# Symptom: Two pets with the same name, species, and age are reported as
#          "NOT A DUPLICATE" even though they should be flagged.
#
# Note: For this to work properly with ==, the Pet class would need an __eq__
#       method. A simpler fix is to compare the relevant attributes directly.
# ==============================================================================

def find_duplicate_profiles(pet_a, pet_b):
    # ----- BUGGY CODE -----
    if pet_a is pet_b:                  # <-- BUG: Tests identity, not equality
        return True
    return False
    
    # ----- FIXED CODE (Option 1: Compare attributes) -----
    # if pet_a.name == pet_b.name and pet_a.species == pet_b.species and pet_a.age == pet_b.age:
    #     return True
    # return False
    #
    # ----- FIXED CODE (Option 2: Add __eq__ to Pet class, then use ==) -----
    # In Pet class, add:
    #     def __eq__(self, other):
    #         if not isinstance(other, Pet):
    #             return False
    #         return (self.name == other.name and 
    #                 self.species == other.species and 
    #                 self.age == other.age)
    #
    # Then in this function:
    #     if pet_a == pet_b:
    #         return True
    #     return False


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


def run_diagnostics(data):
    print("\n" + "=" * 50)
    print("DIAGNOSTIC INFORMATION")
    print("=" * 50)
    
    if "shelter_pets" in data and "event_pets" in data:
        print("\n[Copy Available Pets Check]")
        print(f"  shelter_pets id: {id(data['shelter_pets'])}")
        print(f"  event_pets id:   {id(data['event_pets'])}")
        same = "YES" if data['shelter_pets'] is data['event_pets'] else "NO"
        print(f"  Same object?     {same}")
    
    if "schedule" in data:
        print("\n[Feeding Schedule Check]")
        print(f"  Monday id:    {id(data['schedule'][0])}")
        print(f"  Tuesday id:   {id(data['schedule'][1])}")
        print(f"  Wednesday id: {id(data['schedule'][2])}")
        same = "YES" if data['schedule'][0] is data['schedule'][1] else "NO"
        print(f"  Mon/Tue same object? {same}")
    
    if "original_pet" in data and "backup_pet" in data:
        print("\n[Backup Pet Profile Check]")
        print(f"  original medical_history id: {id(data['original_pet'].medical_history)}")
        print(f"  backup medical_history id:   {id(data['backup_pet'].medical_history)}")
        same = "YES" if data['original_pet'].medical_history is data['backup_pet'].medical_history else "NO"
        print(f"  Same history list? {same}")
    
    if "adoption_records" in data:
        print("\n[Adoption Records Check]")
        for i, record in enumerate(data['adoption_records']):
            print(f"  Record {i+1} notes id: {id(record['notes'])}")
            print(f"  Record {i+1} notes: {record['notes']}")


def main():
    display_banner()
    diagnostic_data = {}
    
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
    
    diagnostic_data["shelter_pets"] = shelter_pets
    diagnostic_data["event_pets"] = event_pets
    
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
    
    diagnostic_data["schedule"] = schedule
    
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
    
    diagnostic_data["original_pet"] = original_pet
    diagnostic_data["backup_pet"] = backup_pet
    
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
    
    diagnostic_data["adoption_records"] = adoption_records
    
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
    
    run_diagnostics(diagnostic_data)
    
    print("\n" + "=" * 50)
    print("END OF DAILY OPERATIONS REPORT")
    print("=" * 50)


if __name__ == "__main__":
    main()


"""
===============================================================================
GRADING RUBRIC SUGGESTION
===============================================================================

For each bug (5 bugs total), evaluate:

1. IDENTIFICATION (Did they find it?)
   - Correctly identified the function name
   - Correctly identified the buggy line(s)

2. EXPLANATION (Do they understand WHY?)
   - Used correct terminology (aliasing, shallow copy, mutable default, etc.)
   - Explained what happens in memory / with object references
   - Connected to Chapter 8-9 concepts

3. FIX (Can they solve it?)
   - Provided working corrected code
   - Fix actually addresses the root cause (not a workaround)

4. DEMONSTRATION (Video)
   - Showed buggy output before fix
   - Showed correct output after fix
   - Verbal explanation was clear

===============================================================================
EXPECTED OUTPUT COMPARISON
===============================================================================

BUGGY OUTPUT:
-------------
[2] Shelter roster: 6 pets (includes Charlie - WRONG)
    Event roster: 6 pets

[3] Wednesday evening = 10, but ALL days' evening = 10 (WRONG)

[4] Original has 3 medical records after backup modification (WRONG)
    Should have 2

[5] All adoption notes show 6 items (WRONG)
    Each should have 2

[6] Reports "NOT A DUPLICATE" for identical pets (WRONG)


CORRECT OUTPUT (after fixes):
-----------------------------
[2] Shelter roster: 5 pets
    Event roster: 6 pets (only event has Charlie)

[3] Only Wednesday evening = 10
    All other days' evening = 6

[4] Original has 2 medical records
    Backup has 3 medical records

[5] Each adoption record has exactly 2 notes

[6] Reports "DUPLICATE FOUND" for identical pets

===============================================================================
"""
