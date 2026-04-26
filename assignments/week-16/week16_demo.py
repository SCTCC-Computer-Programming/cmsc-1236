# ============================================================
# week16_demo.py
# Week 16 Demo: Chapter 30, Operator Overloading
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
#      python week16_demo.py in the VS Code terminal.
#
#   4. Work through the file with two views open at once:
#      the source code in the editor and the terminal output
#      below it. The comments in the source explain what you
#      are seeing in the terminal.
#
# ============================================================
#
# WHAT THIS DEMO COVERS
# ============================================================
#
# Chapter 30 covers operator overloading: the set of
# specially named methods that allow a class to intercept
# built-in operations. When Python evaluates an expression
# like len(p) or p1 + p2, it looks for a method with a
# predefined name (__len__ or __add__) in the class tree
# and calls it automatically.
#
# After working through these examples you should be able to:
#
#   - Explain the difference between __repr__ and __str__
#     and describe when Python calls each one
#   - Define __len__ and __bool__ in a class and explain
#     how Python uses them for truth testing
#   - Define __add__ to support the + operator on instances
#   - Explain what happens when += is used without __iadd__
#   - Define __eq__ to support value equality with ==
#   - Define __contains__ to support the in operator
#   - Explain how operator overloading methods are inherited
#
# ============================================================


# ============================================================
# PART 1: __repr__ AND __str__ -- TWO DISPLAY METHODS
# ============================================================
#
# Chapter 30 introduces two display methods: __repr__ and
# __str__. Both allow a class to control how its instances
# appear as strings, but Python calls them in different
# contexts. This part shows what each one does, when Python
# calls each one, and what happens when one or both are defined.


# ------------------------------------------------------------
# Example 1: The default display without either method
# ------------------------------------------------------------
#
# Without __repr__ or __str__, Python uses the default
# inherited from object: a string showing the class name
# and the object's memory address. This is technically
# informative but not useful for reading or debugging.

class PlaylistV1:
    """A playlist without any display methods."""

    def __init__(self, name, tracks):
        self.name   = name
        self.tracks = list(tracks)

print("=" * 60)
print("PART 1: __repr__ AND __str__ -- TWO DISPLAY METHODS")
print("=" * 60)

print("\n--- Example 1: default display without __repr__ or __str__ ---\n")

p = PlaylistV1("Morning Mix", ["Blue Skies", "Easy", "Float"])

print(f"  print(p):   ", end="")
print(p)
print(f"  repr(p):    {repr(p)}")
print(f"  str(p):     {str(p)}")

# The output is the same in all three cases: class name and
# memory address. The address changes every run. There is no
# way to tell what tracks are in the playlist from this output.


# ------------------------------------------------------------
# Example 2: Adding __repr__
# ------------------------------------------------------------
#
# __repr__ is the general-purpose display method. Python calls
# it in all contexts where a display is needed and no __str__
# is defined: when Python displays a value in the REPL, the
# repr() built-in, objects nested inside other objects, and
# print() itself.
#
# The convention for __repr__ is to return a string that
# looks like a Python expression that could recreate the
# object. Not all classes follow this strictly, but it is
# the intent.

class PlaylistV2:
    """A playlist with __repr__ only."""

    def __init__(self, name, tracks):
        self.name   = name
        self.tracks = list(tracks)

    def __repr__(self):
        return f"Playlist({self.name!r}, {self.tracks!r})"

print("\n--- Example 2: adding __repr__ ---\n")

p = PlaylistV2("Morning Mix", ["Blue Skies", "Easy", "Float"])

print(f"  repr(p):  {repr(p)}")
print(f"  str(p):   {str(p)}")
print(f"  print(p): ", end="")
print(p)
print()

# When only __repr__ is defined, Python uses it everywhere:
# for repr(), for str(), and for print(). All three produce
# the same output. __repr__ is the fallback for everything.

print("  Nested in a list:")
print(f"  {[p]}")

# When an object appears inside a list, Python uses __repr__
# for the nested display -- not __str__. This is true even
# when the list itself is printed.


# ------------------------------------------------------------
# Example 3: Adding __str__ alongside __repr__
# ------------------------------------------------------------
#
# __str__ is called by print() and str() when it is defined.
# Its intended purpose is a user-friendly display: readable
# output rather than an as-code representation.
#
# If __str__ is defined, Python uses it for print() and str().
# For all other contexts -- repr(), REPL display, and
# nested appearances -- Python still uses __repr__.
#
# The split: __str__ for users, __repr__ for developers.

class Playlist:
    """A playlist with both __repr__ and __str__."""

    def __init__(self, name, tracks):
        self.name   = name
        self.tracks = list(tracks)

    def __repr__(self):
        return f"Playlist({self.name!r}, {self.tracks!r})"

    def __str__(self):
        track_list = "\n".join(f"    {i+1}. {t}"
                               for i, t in enumerate(self.tracks))
        return f"  Playlist: {self.name}\n{track_list}"

print("\n--- Example 3: __repr__ and __str__ together ---\n")

p = Playlist("Morning Mix", ["Blue Skies", "Easy", "Float"])

print("  repr(p):")
print(f"    {repr(p)}")
print()
print("  print(p) uses __str__:")
print(p)
print()
print("  Nested in a list uses __repr__:")
print(f"  {[p]}")

# print(p) calls __str__ and produces the readable track list.
# repr(p) calls __repr__ and produces the as-code string.
# The nested appearance in [p] uses __repr__ regardless.
#
# From Week 6: __str__ was defined in the Character class.
# From Week 8: __str__ was defined in CargoPod.
# Both produced readable output for print(). __repr__ was
# not defined, so repr() fell back to the object default.
# This week makes the distinction between the two explicit.


# ============================================================
# PART 2: __len__ AND __bool__
# ============================================================
#
# Python uses two methods to determine the truth value of
# an object: __bool__ and __len__. When a class defines
# these methods, instances can be used in if statements,
# while loops, and any other Boolean context.

print("\n" + "=" * 60)
print("PART 2: __len__ AND __bool__")
print("=" * 60)


# ------------------------------------------------------------
# Example 4: __len__
# ------------------------------------------------------------
#
# __len__ is called when len() is applied to an instance.
# It must return a non-negative integer. For a playlist,
# the natural length is the number of tracks.

class Playlist:
    """Playlist with __repr__, __str__, and __len__."""

    def __init__(self, name, tracks):
        self.name   = name
        self.tracks = list(tracks)

    def __repr__(self):
        return f"Playlist({self.name!r}, {self.tracks!r})"

    def __str__(self):
        track_list = "\n".join(f"    {i+1}. {t}"
                               for i, t in enumerate(self.tracks))
        return f"  Playlist: {self.name}\n{track_list}"

    def __len__(self):
        return len(self.tracks)

print("\n--- Example 4: __len__ ---\n")

morning = Playlist("Morning Mix", ["Blue Skies", "Easy", "Float"])
empty   = Playlist("Empty Queue", [])

print(f"  len(morning): {len(morning)}")
print(f"  len(empty):   {len(empty)}")

# len(morning) calls morning.__len__(), which returns the
# length of the internal tracks list. The same len() built-in
# that works on lists and strings now works on Playlist.


# ------------------------------------------------------------
# Example 5: __bool__ via __len__ fallback
# ------------------------------------------------------------
#
# When a class defines __len__ but not __bool__, Python infers
# the truth value from the length: zero means false, non-zero
# means true. This is the same rule used for lists, strings,
# and other built-in collections.

print("\n--- Example 5: __bool__ via __len__ fallback ---\n")

print(f"  bool(morning): {bool(morning)}")
print(f"  bool(empty):   {bool(empty)}")
print()

if morning:
    print("  morning is truthy -- has tracks")
if not empty:
    print("  empty is falsy  -- no tracks")

# __bool__ is not defined here. Python falls back to __len__:
# morning has 3 tracks, so bool(morning) is True.
# empty has 0 tracks, so bool(empty) is False.
# This mirrors how bool([1, 2, 3]) is True and bool([]) is False.


# ------------------------------------------------------------
# Example 6: Explicit __bool__
# ------------------------------------------------------------
#
# When __bool__ is defined directly, Python uses it instead
# of falling back to __len__. A class can define its own
# truth condition independently of its length. Here a length
# of 1 is truthy by the __len__ rule, but __bool__ returns
# False for it -- showing that the two methods can differ.

class PlaylistBool:
    """Playlist where truth requires more than one track."""

    def __init__(self, name, tracks):
        self.name   = name
        self.tracks = list(tracks)

    def __len__(self):
        return len(self.tracks)

    def __bool__(self):
        return len(self.tracks) > 1   # truthy only if more than one track

print("\n--- Example 6: explicit __bool__ ---\n")

one_track = PlaylistBool("Single", ["Float"])
two_track = PlaylistBool("Pair",   ["Float", "Easy"])

print(f"  len(one_track):  {len(one_track)}")
print(f"  bool(one_track): {bool(one_track)}")
print()
print(f"  len(two_track):  {len(two_track)}")
print(f"  bool(two_track): {bool(two_track)}")
print()
print("  Python prefers __bool__ over __len__ for truth tests.")
print("  __len__ still works for len() even when __bool__ is defined.")

# Both methods coexist. __len__ returns a count for len().
# __bool__ returns the truth value for Boolean contexts.
# Python checks for __bool__ first and only falls back to
# __len__ if __bool__ is absent.


# ============================================================
# PART 3: __add__ -- OPERATOR OVERLOADING FOR +
# ============================================================
#
# The + operator is not defined for custom classes by default.
# Defining __add__ allows instances to appear in + expressions.
# Python calls __add__ with the right operand as its argument
# and uses the return value as the result of the expression.

print("\n" + "=" * 60)
print("PART 3: __add__ -- OPERATOR OVERLOADING FOR +")
print("=" * 60)


# ------------------------------------------------------------
# Example 7: Without __add__
# ------------------------------------------------------------
#
# Without __add__, using + on two Playlist instances raises
# a TypeError. Python has no way to know what combining two
# playlists should mean.

print("\n--- Example 7: without __add__ ---\n")

class PlaylistNoAdd:
    def __init__(self, name, tracks):
        self.name   = name
        self.tracks = list(tracks)

p1 = PlaylistNoAdd("Morning Mix", ["Blue Skies", "Easy"])
p2 = PlaylistNoAdd("Evening Mix", ["Neon", "Fade"])

print("  Attempting p1 + p2 without __add__:")
try:
    result = p1 + p2
except TypeError as e:
    print(f"  TypeError: {e}")

# Python found no addition method on either operand and
# raised TypeError.


# ------------------------------------------------------------
# Example 8: Adding __add__
# ------------------------------------------------------------
#
# __add__ receives self (the left operand) and other (the
# right operand). For a playlist, combining two playlists
# produces a new playlist whose tracks are the tracks of
# both originals in order.

class Playlist:
    """Playlist with __repr__, __str__, __len__, and __add__."""

    def __init__(self, name, tracks):
        self.name   = name
        self.tracks = list(tracks)

    def __repr__(self):
        return f"Playlist({self.name!r}, {self.tracks!r})"

    def __str__(self):
        track_list = "\n".join(f"    {i+1}. {t}"
                               for i, t in enumerate(self.tracks))
        return f"  Playlist: {self.name}\n{track_list}"

    def __len__(self):
        return len(self.tracks)

    def __add__(self, other):
        combined_name   = f"{self.name} + {other.name}"
        combined_tracks = self.tracks + other.tracks
        return Playlist(combined_name, combined_tracks)

print("\n--- Example 8: adding __add__ ---\n")

morning = Playlist("Morning Mix", ["Blue Skies", "Easy", "Float"])
evening = Playlist("Evening Mix", ["Neon", "Fade", "Still"])

combined = morning + evening

print("  morning + evening:")
print(combined)
print()
print(f"  type(combined): {type(combined)}")
print(f"  len(combined):  {len(combined)}")

# morning + evening calls morning.__add__(evening).
# __add__ builds a new Playlist from both track lists and
# returns it. The result is a full Playlist instance with
# its own name, tracks, and all inherited methods.


# ------------------------------------------------------------
# Example 9: += without __iadd__
# ------------------------------------------------------------
#
# Python supports augmented assignment (+=) through a
# separate method called __iadd__. If __iadd__ is not defined,
# Python falls back to __add__ and reassigns the result to the
# variable. The behavior is correct but creates a new object
# rather than modifying the existing one in place.

print("\n--- Example 9: += without __iadd__ ---\n")

p = Playlist("Work Mix", ["Steady", "Drive"])
print(f"  id(p) before +=: {id(p)}")

p += Playlist("Bonus", ["One More"])
print(f"  id(p) after +=:  {id(p)}")
print()
print("  The ids are different.")
print("  Python called __add__ and assigned the new object to p.")
print("  The original object was replaced, not modified.")
print()
print(f"  p after +=:")
print(p)

# id() returns the memory address of an object.
# From Week 3: if two ids differ, the two variables refer
# to different objects. Here, p points to a new Playlist
# after +=, because __add__ always creates a new one.
# __iadd__ can be defined when in-place modification is
# preferred, but __add__ as a fallback is sufficient.


# ============================================================
# PART 4: __eq__ AND __contains__
# ============================================================
#
# Parts 1-3 covered display, length, truth, and arithmetic.
# This part adds the two remaining methods in the demo:
# __eq__ for the == operator and __contains__ for the in
# operator. Together with the methods already defined, these
# give Playlist a complete set of the most commonly used
# behaviors.

print("\n" + "=" * 60)
print("PART 4: __eq__ AND __contains__")
print("=" * 60)


# ------------------------------------------------------------
# Example 10: Default == without __eq__
# ------------------------------------------------------------
#
# Without __eq__, the == operator tests identity: two objects
# are equal only if they are the same object in memory. This
# is the default inherited from object. Two Playlist instances
# with identical names and tracks are not equal by default.
#
# From Week 3: == tests equality and is tests identity.
# For built-in types, == compares by value. For custom
# classes without __eq__, == falls back to identity -- the
# same behavior as is.

print("\n--- Example 10: default == without __eq__ ---\n")

class PlaylistNoEq:
    def __init__(self, name, tracks):
        self.name   = name
        self.tracks = list(tracks)

a = PlaylistNoEq("Morning Mix", ["Blue Skies", "Easy", "Float"])
b = PlaylistNoEq("Morning Mix", ["Blue Skies", "Easy", "Float"])

print(f"  a and b have identical names and tracks.")
print(f"  a is b:  {a is b}")
print(f"  a == b:  {a == b}")
print()
print("  Without __eq__, == tests identity -- same as 'is'.")
print("  a and b are different objects, so both return False.")

# This is the same behavior seen in Week 3 when comparing
# two lists created separately: [] == [] is True because
# list defines __eq__ by value. Custom classes don't get
# that for free -- it must be defined.


# ------------------------------------------------------------
# Example 11: Adding __eq__
# ------------------------------------------------------------
#
# __eq__ receives self and other and should return True if
# the two objects are considered equal in value. For a
# playlist, two playlists with the same name and the same
# tracks in the same order are considered equal.

class Playlist:
    """Playlist with all methods including __eq__."""

    def __init__(self, name, tracks):
        self.name   = name
        self.tracks = list(tracks)

    def __repr__(self):
        return f"Playlist({self.name!r}, {self.tracks!r})"

    def __str__(self):
        track_list = "\n".join(f"    {i+1}. {t}"
                               for i, t in enumerate(self.tracks))
        return f"  Playlist: {self.name}\n{track_list}"

    def __len__(self):
        return len(self.tracks)

    def __add__(self, other):
        return Playlist(
            f"{self.name} + {other.name}",
            self.tracks + other.tracks
        )

    def __eq__(self, other):
        return self.name == other.name and self.tracks == other.tracks

    def __contains__(self, track):
        return track in self.tracks

print("\n--- Example 11: adding __eq__ ---\n")

a = Playlist("Morning Mix", ["Blue Skies", "Easy", "Float"])
b = Playlist("Morning Mix", ["Blue Skies", "Easy", "Float"])
c = Playlist("Morning Mix", ["Blue Skies", "Float", "Easy"])

print(f"  a and b: same name, same tracks in same order")
print(f"  a == b:  {a == b}")
print()
print(f"  a and c: same name, same tracks in different order")
print(f"  a == c:  {a == c}")
print()
print(f"  a is b:  {a is b}")
print("  a == b is True but a is b is False.")
print("  __eq__ compares by value. 'is' still tests identity.")

# a == b calls a.__eq__(b). The method compares names and
# track lists by value. a and c have the same tracks but
# in a different order, so they are not equal.
# 'is' is unchanged -- a and b are still different objects.


# ------------------------------------------------------------
# Example 12: __contains__
# ------------------------------------------------------------
#
# __contains__ is called when the in operator is used:
# track in playlist. It receives the item being tested
# and should return True or False.
#
# Without __contains__, Python falls back to iteration
# (calling __iter__ or __getitem__ to scan the object).
# Defining __contains__ directly allows for a clean and
# potentially more efficient membership test.

print("\n--- Example 12: __contains__ ---\n")

morning = Playlist("Morning Mix", ["Blue Skies", "Easy", "Float"])

print(f"  'Easy' in morning:       {'Easy' in morning}")
print(f"  'Neon' in morning:       {'Neon' in morning}")
print(f"  'Blue Skies' in morning: {'Blue Skies' in morning}")

# Each 'in' expression calls morning.__contains__(track).
# The method delegates to 'in' on the internal list,
# which Python already knows how to search.


# ------------------------------------------------------------
# Example 13: Connecting back to Week 15
# ------------------------------------------------------------
#
# Operator overloading methods are inherited exactly like
# regular methods. A subclass that inherits from Playlist
# gets all the overloaded operators without defining any of
# them. If the subclass needs different behavior, it can
# override individual methods.

class Album(Playlist):
    """A subclass of Playlist representing a released album."""

    def __init__(self, name, artist, tracks):
        super().__init__(name, tracks)   # Playlist.__init__
        self.artist = artist

    def __repr__(self):
        return f"Album({self.name!r}, {self.artist!r}, {self.tracks!r})"

    def __str__(self):
        track_list = "\n".join(f"    {i+1}. {t}"
                               for i, t in enumerate(self.tracks))
        return f"  Album: {self.name} by {self.artist}\n{track_list}"

print("\n--- Example 13: connecting back to Week 15 ---\n")

album = Album("Kind of Blue", "Miles Davis",
              ["So What", "Freddie Freeloader", "Blue in Green"])

print("  Album inherits __len__, __add__, __eq__, __contains__")
print("  from Playlist without redefining them.\n")
print(f"  len(album):                    {len(album)}")
print(f"  'So What' in album:            {'So What' in album}")
print(f"  'Coltrane' in album:           {'Coltrane' in album}")
print()

# __add__ with a Playlist and an Album:
extra = Playlist("Bonus Tracks", ["Flamenco Sketches"])
combined = album + extra

print(f"  album + extra:")
print(combined)
print()

# __eq__ inherited from Playlist:
a1 = Album("Kind of Blue", "Miles Davis",
           ["So What", "Freddie Freeloader", "Blue in Green"])
a2 = Album("Kind of Blue", "Miles Davis",
           ["So What", "Freddie Freeloader", "Blue in Green"])

print(f"  a1 == a2 (same content): {a1 == a2}")
print()
print("  Album.__mro__:")
for cls in Album.__mro__:
    print(f"    {cls}")

# Album.__eq__ is not defined. Python walks the MRO:
# Album -> Playlist -> object. It finds __eq__ in Playlist
# and calls it. The operator methods are found and used
# exactly like any other inherited method.
#
# From Week 15: the MRO determines lookup order. Operator
# overloading methods follow the same search as everything else.
#
# Note: album + extra returns a Playlist, not an Album,
# because Playlist.__add__ creates and returns a Playlist.
# The output shows "Playlist:" for that reason. A subclass
# that needed + to return an Album would override __add__.


# ============================================================
# CONCLUSION
# ============================================================

print("\n" + "=" * 60)
print("CONCLUSION")
print("=" * 60)

print("""
What you have learned this week:

__repr__ AND __str__
  __repr__ is the general display method. Python calls it
  when Python displays a value in the REPL, for repr(), and
  for nested appearances. __str__ is called by print() and str() when defined.
  If only __repr__ is defined, it serves as the fallback
  for everything. If both are defined, __str__ applies to
  print() and str(); __repr__ applies everywhere else.
  Defining __repr__ alone is sufficient if one display
  covers all contexts. Defining both supports separate
  user-facing and developer-facing formats.

__len__ AND __bool__
  __len__ makes len() work on instances. Python also uses
  __len__ to infer truth: zero length means false, non-zero
  means true. __bool__ defines truth directly and takes
  precedence over __len__ when both are present. If neither
  is defined, instances are always truthy.

__add__
  __add__ intercepts the + operator. It receives the right
  operand as other and returns the result. If __iadd__ is
  not defined, += falls back to __add__ and reassigns the
  result. Every binary operator has a corresponding method
  (__sub__, __mul__, etc.) that works the same way.

__eq__
  __eq__ intercepts ==. Without it, == tests identity --
  the same behavior as is. With it, == tests whatever the
  method defines as equal. The is operator always tests
  identity regardless of __eq__.

__contains__
  __contains__ intercepts the in operator. Without it,
  Python falls back to iteration. Defining __contains__
  directly provides a clean, explicit membership test.

INHERITANCE
  Operator overloading methods are inherited exactly like
  regular methods. A subclass gets all parent overloads
  automatically and can override individual ones as needed.

What the reading covers in more depth:

  __radd__ and __iadd__: right-side and in-place variants
  of __add__. __radd__ handles cases where the instance is
  on the right side of +. __iadd__ enables true in-place
  modification for +=.

  __getitem__ and __setitem__: intercept indexing (obj[i])
  and slice expressions. Also serve as a fallback for
  iteration if __iter__ is absent.

  __call__: makes an instance callable like a function.
  Useful for stateful callbacks and function-like objects.

  __getattr__ and __setattr__: intercept attribute access
  and assignment. Used for delegation, validation, and
  proxy patterns.

  Comparison suite: __lt__, __gt__, __le__, __ge__, __ne__
  cover the full set of comparison operators. __lt__ is
  also used by sorted() and list.sort().

  __del__: called when an instance is garbage-collected.
  Rarely used in practice.
""")
