# ============================================================
# week15_demo.py
# Week 15 Demo: Chapters 26-27, Classes and Inheritance
# ============================================================
#
# BEFORE YOU BEGIN
# ============================================================
#
# This demo is a single Python file. No companion module is
# required this week.
#
# Setup steps:
#
#   1. Save this file in your course folder in VS Code.
#
#   2. Open that folder in VS Code using File > Open Folder.
#
#   3. Run this file using the Run button or by typing
#      python week15_demo.py in the VS Code terminal.
#
#   4. Work through the file with two views open at once:
#      the source code in the editor and the terminal output
#      below it. The comments in the source explain what you
#      are seeing in the terminal. Reading one without the
#      other will leave gaps.
#
# ============================================================
#
# WHAT THIS DEMO COVERS
# ============================================================
#
# Chapters 26-27 cover the class tree model and inheritance.
# In Python, classes and instances are namespace objects
# connected by links, and attribute lookup walks those links
# from the instance upward through the class hierarchy. This
# model explains how inheritance, method overriding, self,
# and super() work.
#
# After working through these examples you should be able to:
#
#   - Explain what a class object is and how it differs from
#     an instance object
#   - Describe how Python searches a class tree when looking
#     up an attribute
#   - Explain what self is and why it is always the first
#     argument in a method
#   - Write a subclass that inherits from a parent class
#   - Override a method in a subclass
#   - Use super() to extend a parent method rather than
#     replace it entirely
#   - Read the __mro__ of a class and explain what it means
#
# ============================================================


# ============================================================
# PART 1: THE CLASS TREE AND HOW INHERITANCE WORKS
# ============================================================
#
# Before writing any subclasses, it helps to understand what
# Python is actually doing when you define a class and create
# instances from it. The class model is simpler than it looks:
# it is a tree of objects connected by links, and Python walks
# that tree whenever you access an attribute.


# ------------------------------------------------------------
# Example 1: A class is an object
# ------------------------------------------------------------
#
# A class statement creates a class object and assigns it to
# a name. The class object exists before any instances are
# created. Like everything else in Python, it has a type, an
# identity in memory, and attributes stored in a dictionary.
#
# This connects directly to Week 14: module namespaces are
# plain __dict__ dictionaries, and so are class namespaces.

class Animal:
    species = "unknown"

    def speak(self):
        return "..."

print("=" * 60)
print("PART 1: THE CLASS TREE AND HOW INHERITANCE WORKS")
print("=" * 60)

print("\n--- Example 1: a class is an object ---\n")
print(f"  type(Animal)  = {type(Animal)}")
print(f"  id(Animal)    = {id(Animal)}")
print()
print("  Animal.__dict__ (class-level names):")
for key, value in Animal.__dict__.items():
    if not key.startswith('__'):
        print(f"    {key!r:15} -> {value}")

# From Week 14: __dict__ is the namespace dictionary for any
# object in Python. Modules have one. Classes have one too.
# The names assigned at the top level of a class body become
# entries in that dictionary, exactly like module attributes.


# ------------------------------------------------------------
# Example 2: Instances are linked to their class
# ------------------------------------------------------------
#
# Calling a class creates a new instance object. Each instance
# is a separate namespace but holds a reference back to the
# class it came from. Two instances of the same class are
# independent objects with independent data, but they share
# the methods defined in the class.

print("\n--- Example 2: instances are linked to their class ---\n")

a1 = Animal()
a1.name = "Rex"

a2 = Animal()
a2.name = "Luna"

print(f"  a1 is a2:          {a1 is a2}")
print(f"  type(a1) is Animal: {type(a1) is Animal}")
print()
print(f"  a1.__dict__: {a1.__dict__}")
print(f"  a2.__dict__: {a2.__dict__}")

# The instances have different __dict__ dictionaries because
# their data (name) is stored on the instance, not the class.
# The method speak is not in either instance's __dict__. It
# lives in the class, and both instances find it there.
# Example 3 makes this explicit.


# ------------------------------------------------------------
# Example 3: The namespace underneath
# ------------------------------------------------------------
#
# An instance's __dict__ contains only the names assigned
# directly to that instance. The class's __dict__ contains
# the names defined in the class body. When Python looks up
# an attribute, it checks the instance first, then the class.
#
# This is the same lookup model from Week 3 (identity and
# attributes) and Week 14 (module namespaces). OOP in Python
# is the same mechanism applied to a tree of linked objects.

print("\n--- Example 3: the namespace underneath ---\n")
print("  a1.__dict__ (instance namespace):")
print(f"    {a1.__dict__}")
print()
print("  Animal.__dict__ (class namespace, user-defined names only):")
for key, value in Animal.__dict__.items():
    if not key.startswith('__'):
        print(f"    {key!r:15} -> {value}")
print()
print("  'name' is in a1.__dict__:", 'name' in a1.__dict__)
print("  'speak' is in a1.__dict__:", 'speak' in a1.__dict__)
print("  'speak' is in Animal.__dict__:", 'speak' in Animal.__dict__)

# Python checks the instance first. If the name is not found
# there, it moves up to the class. If still not found, it
# continues up to the class's superclass, and so on. This
# chain of linked namespaces is the class tree.


# ------------------------------------------------------------
# Example 4: Attribute lookup walks up the tree
# ------------------------------------------------------------
#
# The lookup chain is not just one level deep. Every class
# in Python implicitly inherits from a built-in class called
# object. This is the root of every class tree and provides
# default behaviors that all classes inherit automatically.

print("\n--- Example 4: attribute lookup walks up the tree ---\n")
print("  Animal.__mro__:")
for cls in Animal.__mro__:
    print(f"    {cls}")
print()
print("  'speak' found at:", end=" ")
for cls in Animal.__mro__:
    if 'speak' in cls.__dict__:
        print(cls)
        break
print()
print("  '__repr__' found at:", end=" ")
for cls in Animal.__mro__:
    if '__repr__' in cls.__dict__:
        print(cls)
        break

# __mro__ is the Method Resolution Order: the exact sequence
# Python follows when searching for a name. For Animal, it is
# [Animal, object]. For a subclass, the subclass appears first
# so its definitions take precedence over the parent's.
#
# '__repr__' is not defined in Animal, so Python finds it in
# object. This is why every Python object has a default string
# representation even if you never define one.


# ============================================================
# PART 2: WRITING A BASE CLASS
# ============================================================
#
# Now that the class tree model is visible, this part builds
# a proper base class and examines what each piece does.
# The Animal class is rebuilt here with a full __init__ and
# __str__ so the examples in Parts 3 and 4 have something
# real to work with.

print("\n" + "=" * 60)
print("PART 2: WRITING A BASE CLASS")
print("=" * 60)


# Animal is redefined here with a full __init__, __str__,
# and methods. The minimal version in Part 1 served to show
# the class tree before any instance data was involved.
# This version is what Parts 3 and 4 build on.
class Animal:
    """A shelter animal with a name, species, and age."""

    def __init__(self, name, species, age):
        self.name    = name
        self.species = species
        self.age     = age

    def __str__(self):
        return f"{self.name} ({self.species}, {self.age} yrs)"

    def speak(self):
        return f"{self.name} makes a sound."

    def description(self):
        return (f"  Name:    {self.name}\n"
                f"  Species: {self.species}\n"
                f"  Age:     {self.age} years")


# ------------------------------------------------------------
# Example 5: The Animal class
# ------------------------------------------------------------
#
# The three methods above do three different things. __init__
# runs automatically when an instance is created and stores
# data on self. __str__ runs automatically when an instance
# is passed to print() or str(). speak() and description()
# are regular methods called explicitly by name.
#
# This is the same structure used in Weeks 2, 6, and 8.

print("\n--- Example 5: the Animal class ---\n")
print("  Animal.__dict__ (methods and class-level names):")
show = {'__init__', '__str__'}
for key, value in Animal.__dict__.items():
    if not key.startswith('__') or key in show:
        print(f"    {key!r:15} -> {value}")


# ------------------------------------------------------------
# Example 6: Creating instances and calling methods
# ------------------------------------------------------------

print("\n--- Example 6: creating instances and calling methods ---\n")

cat = Animal("Whiskers", "Cat", 4)
rabbit = Animal("Biscuit", "Rabbit", 2)

print(f"  str(cat):    {str(cat)}")
print(f"  str(rabbit): {str(rabbit)}")
print()
print(f"  cat.speak():    {cat.speak()}")
print(f"  rabbit.speak(): {rabbit.speak()}")
print()
print("  cat.description():")
print(cat.description())

# description() returns a multi-line string with leading
# spaces built into the f-string. The indentation is part
# of the return value, not added by print().

# Notice that str(cat) and str(rabbit) produce different
# output even though the same __str__ method is called for
# both. The difference is self: each call receives a different
# instance object, so self.name resolves to a different value.


# ------------------------------------------------------------
# Example 7: What self is
# ------------------------------------------------------------
#
# self is not a keyword. It is simply the name given by
# convention to the first argument of every method. Python
# fills it in automatically with the instance that the method
# is called on. Demonstrating this with id() makes it concrete.

# Animal is redefined here to add show_self_id(). The class
# is otherwise identical to the Part 2 version. Instances
# created before this point (cat, rabbit) belong to the
# prior definition and will not have show_self_id().
class Animal:
    """A shelter animal with a name, species, and age."""

    def __init__(self, name, species, age):
        self.name    = name
        self.species = species
        self.age     = age

    def __str__(self):
        return f"{self.name} ({self.species}, {self.age} yrs)"

    def speak(self):
        return f"{self.name} makes a sound."

    def description(self):
        return (f"  Name:    {self.name}\n"
                f"  Species: {self.species}\n"
                f"  Age:     {self.age} years")

    def show_self_id(self):
        print(f"  id(self) inside the method  = {id(self)}")

print("\n--- Example 7: what self is ---\n")

dog = Animal("Rex", "Dog", 3)
print(f"  id(dog) outside the method  = {id(dog)}")
dog.show_self_id()
print()
print("  Both ids are identical.")
print("  self IS the instance. Python passes it automatically.")

# From Week 10: functions are first-class objects in Python.
# A method is a function stored as a class attribute. When
# called through an instance, Python prepends the instance
# as the first argument. dog.show_self_id() is equivalent
# to Animal.show_self_id(dog).


# ============================================================
# PART 3: WRITING A SUBCLASS AND OVERRIDING METHODS
# ============================================================
#
# Inheritance means that a subclass automatically receives
# all of the attributes defined in its parent class. When a
# subclass defines a method with the same name as one in the
# parent, the subclass version takes precedence because Python
# finds it first during the tree search.

print("\n" + "=" * 60)
print("PART 3: WRITING A SUBCLASS AND OVERRIDING METHODS")
print("=" * 60)


class Dog(Animal):
    """A dog in the shelter. Inherits from Animal."""

    def speak(self):
        return f"{self.name} barks."

    def fetch(self, item):
        return f"{self.name} fetches the {item}!"


# ------------------------------------------------------------
# Example 8: The Dog subclass
# ------------------------------------------------------------
#
# Dog lists Animal in its header: class Dog(Animal).
# This creates a link in the class tree from Dog up to Animal.
# Dog defines speak() and fetch(). It does not define
# __init__, __str__, or description() -- those are inherited
# from Animal and work without any additional code in Dog.

print("\n--- Example 8: the Dog subclass ---\n")
print("  Dog.__mro__:")
for cls in Dog.__mro__:
    print(f"    {cls}")
print()
print("  Names defined directly in Dog (not inherited):")
for key in Dog.__dict__:
    if not key.startswith('__'):
        print(f"    {key}")


# ------------------------------------------------------------
# Example 9: Inheritance in action
# ------------------------------------------------------------
#
# A Dog instance calls speak() and gets the Dog version.
# A Dog instance calls __str__() and gets the Animal version
# because Dog does not define its own. The tree search stops
# at the first match found walking upward from the instance.

print("\n--- Example 9: inheritance in action ---\n")

buddy = Dog("Buddy", "Dog", 5)

print(f"  str(buddy):       {str(buddy)}")
print(f"  buddy.speak():    {buddy.speak()}")
print(f"  buddy.fetch('ball'): {buddy.fetch('ball')}")
print()
print("  Where does Python find each method?")

for method_name in ('speak', '__str__', 'description', 'fetch'):
    for cls in Dog.__mro__:
        if method_name in cls.__dict__:
            print(f"    {method_name!r:15} found in {cls.__name__}")
            break

# __str__ and description are found in Animal because Dog
# does not define them. speak and fetch are found in Dog.
# This is the inheritance search in action: instance first,
# then Dog, then Animal, then object.


# ------------------------------------------------------------
# Example 10: Polymorphism
# ------------------------------------------------------------
#
# When different classes define the same method name,
# the same call produces different behavior depending on
# which object it is called on. This is polymorphism: one
# interface, multiple implementations.
#
# The loop below calls speak() on every animal in the list
# without knowing or caring which class each object belongs to.

print("\n--- Example 10: polymorphism ---\n")

shelter = [
    Animal("Mittens", "Cat",    2),
    Dog("Rex",     "Dog",    4),
    Animal("Nibbles", "Rabbit", 1),
    Dog("Sadie",   "Dog",    6),
]

print("  Morning roll call:")
for animal in shelter:
    print(f"    {animal.speak()}")

# The loop is identical for every animal. Python selects the
# correct speak() based on the actual type of each object at
# runtime. Animal instances use Animal.speak(); Dog instances
# use Dog.speak(). No if/elif needed -- the class tree handles
# the dispatch automatically.


# ============================================================
# PART 4: super() -- EXTENDING RATHER THAN REPLACING
# ============================================================
#
# When a subclass needs to add to a parent method rather than
# replace it entirely, super() provides a way to call the
# parent's version of the method from inside the subclass.
# This is most commonly needed in __init__, where the parent
# sets up shared attributes and the subclass adds its own.

print("\n" + "=" * 60)
print("PART 4: super() -- EXTENDING RATHER THAN REPLACING")
print("=" * 60)


# ------------------------------------------------------------
# Example 11: The problem -- rewriting __init__ from scratch
# ------------------------------------------------------------
#
# A ServiceDog needs everything a Dog needs plus a task.
# One approach is to rewrite __init__ from scratch.
# This works, but it duplicates every line from Animal.__init__
# and creates a maintenance problem: if Animal.__init__ ever
# changes, ServiceDog must be updated separately.

class ServiceDogWithoutSuper(Dog):
    """Demonstrates the wrong approach: duplicating __init__."""

    def __init__(self, name, species, age, task):
        # Duplicating Animal.__init__ -- every attribute
        # must be written again by hand:
        self.name    = name
        self.species = species
        self.age     = age
        # Then add what is new:
        self.task    = task

    def __str__(self):
        return f"{self.name} ({self.species}, {self.age} yrs) [Service: {self.task}]"

print("\n--- Example 11: the problem (duplication) ---\n")
guide = ServiceDogWithoutSuper("Guide", "Dog", 4, "vision assistance")
print(f"  {guide}")
print()
print("  ServiceDogWithoutSuper.__init__ duplicates all of")
print("  Animal.__init__ just to add one new attribute.")
print("  If Animal ever adds a new attribute, this class breaks.")


# ------------------------------------------------------------
# Example 12: The solution -- super()
# ------------------------------------------------------------
#
# super() returns an object that routes attribute lookups
# to the next class in the MRO. Inside __init__,
# super().__init__(...) calls the parent's constructor with
# the shared arguments, then the subclass adds only what
# is new. No duplication.

class ServiceDog(Dog):
    """A service dog with a specific task. Extends Dog with super()."""

    def __init__(self, name, species, age, task):
        super().__init__(name, species, age)  # next in MRO: Dog -> Animal
        self.task = task                       # new attribute

    def __str__(self):
        base = super().__str__()               # next in MRO: Dog -> Animal
        return f"{base} [Service: {self.task}]"

    def speak(self):
        return f"{self.name} is focused on duty."

print("\n--- Example 12: the solution (super()) ---\n")

apollo = ServiceDog("Apollo", "Dog", 3, "mobility assistance")
print(f"  str(apollo):    {apollo}")
print(f"  apollo.speak(): {apollo.speak()}")
print(f"  apollo.fetch(): {apollo.fetch('harness')}")
print()
print("  ServiceDog.__init__ adds only self.task.")
print("  Everything else comes from Animal.__init__ via super().")

# super() follows the MRO: ServiceDog -> Dog -> Animal.
# Dog defines no __init__ or __str__, so super() passes
# through to Animal for both. fetch() is not defined in
# ServiceDog at all -- it is inherited from Dog.


# ------------------------------------------------------------
# Example 13: Connecting back to prior weeks
# ------------------------------------------------------------
#
# Every class the course has written -- Pet, Character,
# CargoPod -- was already a subclass. They inherited from
# object implicitly. object is the built-in root class that
# sits at the top of every class tree in Python. It provides
# the default __repr__, __eq__, and other behaviors that all
# classes share unless they override them.
#
# The __mro__ of ServiceDog shows the full chain:
# ServiceDog -> Dog -> Animal -> object

print("\n--- Example 13: connecting back to prior weeks ---\n")
print("  ServiceDog.__mro__:")
for cls in ServiceDog.__mro__:
    print(f"    {cls}")
print()
print("  Every class in Python implicitly inherits from object.")
print("  This includes every class written in this course.")
print()
print("  The classes defined in this demo confirm the pattern:")
for cls in (Animal, Dog, ServiceDog):
    root = cls.__mro__[-1]
    print(f"    {cls.__name__:15} -> root is {root}")
print()
print("  Pet, Character, and CargoPod from earlier weeks have")
print("  the same root. object provides __repr__, __eq__, and")
print("  other defaults. When you wrote __str__ in CargoPod,")
print("  you were overriding the version inherited from object.")


# ============================================================
# CONCLUSION
# ============================================================

print("\n" + "=" * 60)
print("CONCLUSION")
print("=" * 60)

print("""
What you have learned this week:

THE CLASS TREE
  A class is an object. Instances are linked to the class
  that created them. Attribute lookup walks up the tree:
  Python checks the instance first, then the class, then
  each superclass in MRO order, stopping at the first match.
  Module namespaces and class namespaces are both plain
  dictionaries (__dict__) connected by links.

SELF
  self is the first argument of every method. Python fills
  it in automatically with the instance the method is called
  on. Calling dog.speak() is equivalent to Animal.speak(dog).
  The name self is a convention, not a keyword. Its position
  in the method header is what matters.

SUBCLASSES AND METHOD OVERRIDING
  A subclass lists its parent in parentheses: class Dog(Animal).
  This places Dog below Animal in the tree. Any method defined
  in Dog overrides the same-named method in Animal for Dog
  instances, because the tree search finds Dog's version first.
  Methods not defined in Dog are inherited from Animal without
  any additional code.

super()
  super() calls the next class in the MRO. In __init__, it
  allows a subclass to extend the parent constructor rather
  than rewrite it. This avoids duplication and keeps the
  subclass synchronized with the parent automatically.

OBJECT
  Every class in Python inherits from object. Pet, Character,
  CargoPod, Animal, Dog, and ServiceDog all have object at
  the top of their tree. The __repr__, __eq__, and other
  default behaviors you get without defining them come from
  object.

What the reading covers in more depth:

  Multiple inheritance: a class can list more than one
  superclass in its header. Python uses MRO to determine
  the lookup order. This is covered in Chapter 31.

  Operator overloading: classes can intercept expressions
  like +, len(), and == by defining __add__, __len__, and
  __eq__. This is the subject of Week 16.

  Abstract superclasses: a class that defines a method
  that subclasses are required to override. Python provides
  the abc module for enforcing this pattern.
""")
