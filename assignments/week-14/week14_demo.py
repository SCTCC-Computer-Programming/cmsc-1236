# ============================================================
# week14_demo.py
# Week 14 Demo: Chapters 22-25, Modules and Packages
# ============================================================
#
# BEFORE YOU BEGIN
# ============================================================
#
# This demo uses two files that must be in the same folder:
#
#   week14_demo.py       <-- this file (run this one)
#   week14_module.py     <-- the module this file imports
#
# Setup steps:
#
#   1. Save both files in the same folder on your computer.
#
#   2. Open that folder in VS Code using File > Open Folder.
#      Do not just open the file. Open the whole folder in VS Code.
#      You should see both .py files listed in the Explorer
#      panel on the left.
#
#   3. Run this file using the Run button or by typing
#      python week14_demo.py in the VS Code terminal.
#
#   4. Work through the file with two views open at once:
#      the source code in the editor and the terminal output
#      below it. The comments in the source explain what you
#      are seeing in the terminal. Reading one without the
#      other will leave gaps.
#
#   5. After the first run, look at the Explorer panel again.
#      A new folder named __pycache__ will have appeared.
#      Part 1 explains what it is and why Python created it.
#
#   6. Do not modify week14_module.py unless an example
#      specifically asks you to.
#
# ============================================================
#
# WHAT THIS DEMO COVERS
# ============================================================
#
# You have been using import statements since Week 1 and
# writing modules since Week 8 (cargo_module.py). This demo
# explains what has been happening underneath that entire time.
#
# After working through these examples you should be able to:
#
#   - Explain the three steps Python takes every time it
#     executes an import statement
#   - Describe what sys.path is and why the current directory
#     appears first
#   - Explain why a module's top-level code runs once and
#     does not run again on repeated imports
#   - Explain what __pycache__ is and why Python creates it
#   - Inspect a module's namespace using dir() and __dict__
#   - Explain the relationship between module attributes and
#     the underlying __dict__ dictionary
#   - Use _X naming and __all__ to control what a module
#     exposes and to signal intent to other programmers
#   - Explain what __name__ contains and why its value
#     depends on how the file is being used
#   - Read and write the if __name__ == '__main__' pattern
#     with full understanding of what it does and why
#
# ============================================================


# ============================================================
# PART 1: HOW IMPORT WORKS
# ============================================================
#
# When Python executes an import statement it performs three
# steps in order:
#
#   1. FIND   — locate the module file on the file system
#   2. COMPILE — translate the source to bytecode (if needed)
#   3. RUN    — execute the module's top-level code once
#
# The rest of Part 1 makes each of these steps visible.


# ------------------------------------------------------------
# Example 1: The module search path
# ------------------------------------------------------------
#
# The first step of every import is a search. Python walks
# through a list of directories looking for a file whose name
# matches the module being imported. That list is stored in
# sys.path, a plain Python list you can inspect and print.

import sys

print("=" * 60)
print("PART 1: HOW IMPORT WORKS")
print("=" * 60)

print("\n--- Example 1: sys.path ---\n")
print("Python searches these directories, in order:")
for i, path in enumerate(sys.path):
    label = " (current folder)" if i == 0 else ""
    print(f"  [{i}] {path!r}{label}")

# The first entry is always the directory containing the
# script being run, which in this case is the folder where
# you saved these two files. This is why week14_module.py was found
# without any special configuration: it sits in the same
# folder as this script, and that folder is always first.
#
# From Week 8: cargo_module.py worked for the same reason.
# You saved it in the same folder as space_trader.py, which
# meant it was always at position [0] in sys.path.


# ------------------------------------------------------------
# Example 2: Modules run once
# ------------------------------------------------------------
#
# When Python imports a module for the first time, it runs
# all of the module's top-level statements from top to bottom.
# This is how the module's functions and variables get defined.
#
# After that first import, Python stores the loaded module in
# an internal table called sys.modules. Every subsequent
# import statement for the same module retrieves the already-
# loaded object from that table without re-running the file.
#
# week14_module.py has a print() call at its top level that
# reads: [week14_module] module loaded
#
# Watch for that line in the output below. It will appear
# exactly once no matter how many times the module is imported.

print("\n--- Example 2: one-time execution ---\n")

print("First import:")
import week14_module          # top-level print fires here

print("\nSecond import (same module, different alias):")
import week14_module as wm    # already loaded, no print

print("\nThird import (from form):")
from week14_module import greet   # still already loaded, no print

print("\nAll three import statements completed.")
print("The [week14_module] message appeared exactly once.")

# The module object is the same object in memory across all
# three imports. Python never loaded the file a second time.


# ------------------------------------------------------------
# Example 3: __pycache__ and bytecode compilation
# ------------------------------------------------------------
#
# The second step of the import process is compilation.
# Python translates the module's source code into bytecode,
# a lower-level representation that the Python interpreter
# can execute more efficiently than raw source text.
#
# Python saves that bytecode to disk so it does not have to
# recompile the file on every run. The saved file lives in
# the __pycache__ folder that appeared in your VS Code
# Explorer panel after the first run.
#
# The file inside __pycache__ has a name like:
#   week14_module.cpython-312.pyc
#
# The .pyc extension marks it as compiled bytecode. The
# cpython-312 part records which Python version created it,
# so Python will recompile if you switch versions.
#
# On future runs, if the source file has not changed,
# Python skips the compilation step and loads the .pyc file
# directly. This is purely a performance optimization with
# no effect on what your code does.

print("\n--- Example 3: __pycache__ ---\n")
print("Look at the VS Code Explorer panel now.")
print("You should see a __pycache__ folder next to your .py files.")
print()

import os
cache_dir = os.path.join(os.path.dirname(__file__), '__pycache__')
if os.path.exists(cache_dir):
    pyc_files = [f for f in os.listdir(cache_dir) if f.endswith('.pyc')]
    print("Contents of __pycache__:")
    for f in pyc_files:
        print(f"  {f}")
else:
    print("  __pycache__ not found. Try running the script once more.")

print()
print("Python created this file the first time week14_module was")
print("imported. It is bytecode: a compiled version of the source.")
print("You never need to create or edit .pyc files yourself.")


# ============================================================
# PART 2: MODULE NAMESPACES
# ============================================================
#
# Every module is a namespace: a container that maps names
# to objects. When Python runs a module file, every name
# assigned at the top level becomes an attribute of the
# module object. That is how greet, shout, and word_count
# became accessible as week14_module.greet and so on.
#
# Python stores a module's namespace in a plain dictionary
# called __dict__. This part makes that structure visible.

print("\n" + "=" * 60)
print("PART 2: MODULE NAMESPACES")
print("=" * 60)


# ------------------------------------------------------------
# Example 4: Inspecting a module with dir()
# ------------------------------------------------------------
#
# dir() called on a module returns a sorted list of all the
# names defined in that module. This includes the functions
# you wrote, any variables assigned at the top level, and
# a set of names Python adds automatically, such as
# __name__, __file__, __doc__, and __all__.

print("\n--- Example 4: dir() ---\n")
print("Names defined in week14_module:")
names = dir(week14_module)
for name in names:
    print(f"  {name}")

# You will see greet, shout, word_count, and _format_header
# listed alongside the automatic dunder names. dir() shows
# everything, including names that start with an underscore.
# The _ convention signals intent, not access restriction.


# ------------------------------------------------------------
# Example 5: The namespace as a dictionary
# ------------------------------------------------------------
#
# The names you just saw with dir() live in a plain Python
# dictionary stored as the module's __dict__ attribute.
# The keys are name strings; the values are the objects
# those names refer to.
#
# This is the same object model from Week 3. Modules, like
# everything else in Python, are objects, and their
# attributes are stored in a dictionary underneath.

print("\n--- Example 5: __dict__ ---\n")
print("week14_module.__dict__ (user-defined names only):\n")

for key, value in week14_module.__dict__.items():
    # Show user-defined names and __all__; skip other dunders
    if not key.startswith('__') or key == '__all__':
        print(f"  {key!r:20} → {value}")


# ------------------------------------------------------------
# Example 6: attribute access and dictionary lookup are
#            the same operation
# ------------------------------------------------------------
#
# Accessing week14_module.greet and looking up
# week14_module.__dict__['greet'] return the exact same
# object. Attribute access is dictionary lookup with
# dot-notation syntax. This is the same principle that
# Week 3 demonstrated with object identity and attributes.
#
# id() returns the memory address of an object. If two
# expressions return the same id, they refer to the same
# object in memory.

print("\n--- Example 6: attribute access vs dictionary lookup ---\n")

via_dot    = week14_module.greet
via_dict   = week14_module.__dict__['greet']

print(f"  week14_module.greet          id = {id(via_dot)}")
print(f"  week14_module.__dict__[...] id = {id(via_dict)}")
print(f"  Same object? {via_dot is via_dict}")

# From Week 3: is tests identity, not equality. Two expressions
# that return True from is refer to the exact same object,
# not a copy, not an equal value, the same thing in memory.
#
# The attribute and the dictionary entry are not two copies
# of the function. They are two names pointing at one object.


# ============================================================
# PART 3: CONTROLLING WHAT A MODULE EXPORTS
# ============================================================
#
# Python modules have no private keyword. Any name defined
# in a module can be accessed from outside it. But there are
# two tools that let a module signal its intent: the _X
# naming convention and the __all__ list. Together they
# define a module's public interface without restricting
# access by force.

print("\n" + "=" * 60)
print("PART 3: CONTROLLING WHAT A MODULE EXPORTS")
print("=" * 60)


# ------------------------------------------------------------
# Example 7: The _X naming convention
# ------------------------------------------------------------
#
# A name that begins with a single underscore is a signal:
# "this is for internal use, not part of the public interface."
# Python does not enforce this. You can still access
# _format_header by qualifying it through the module name.
# The underscore is a convention between programmers, not a
# lock.

print("\n--- Example 7: _X convention ---\n")

# Both calls work. The underscore makes no technical difference.
# It signals intent, not access control.
public_result  = week14_module.greet("Ada")
private_result = week14_module._format_header("Week 14 Demo")

print(f"  week14_module.greet('Ada')           → {public_result!r}")
print(f"  week14_module._format_header(...)    → reachable, but signaled as internal")
print(private_result)
print()
print("Both names are accessible by qualification.")
print("The underscore on _format_header is a signal, not a lock.")
print("It tells other programmers: this is an internal helper,")
print("not a tool this module is designed to provide to you.")


# ------------------------------------------------------------
# Example 8: from module import * and the _X convention
# ------------------------------------------------------------
#
# The from * form imports every name from a module into the
# current namespace. There are two reasons to be careful
# with it:
#
#   1. It can silently overwrite names that already exist
#      in your namespace.
#   2. It obscures where names came from. Reading the code
#      later, you cannot tell which module provided them.
#
# The one thing from * does respect is the underscore
# convention: names beginning with _ are not exported.
#
# The names available before and after the import are
# compared below to make the effect visible.

print("\n--- Example 8: from * and the _X convention ---\n")

before = set()
after  = set()

before = set(dir())
from week14_module import *
after  = set(dir())

imported = sorted(after - before)
print("Names brought in by 'from week14_module import *':")
for name in imported:
    print(f"  {name}")

# greet was already imported earlier in this script
# (Example 2: from week14_module import greet), so it does
# not appear as a new name here; it was already present in
# the baseline. shout and word_count are new.
print()
print("Note: greet was already imported earlier in this script,")
print("so it does not appear as a new name here.")
print()
print("Notice: _format_header is NOT in this list.")
print("The underscore convention protected it from from *.")


# ------------------------------------------------------------
# Example 9: __all__ and the public interface
# ------------------------------------------------------------
#
# __all__ is a list of name strings defined at the top level
# of a module. When present, it tells Python exactly which
# names to export for from * imports. Names absent from
# __all__ are not exported, even if they don't start with _.
#
# __all__ also serves as documentation. A programmer reading
# week14_module.py can find __all__ near the top and
# immediately know what the module is intended to provide.
# It is a design statement, not just a technical filter.

print("\n--- Example 9: __all__ ---\n")
print(f"week14_module.__all__ = {week14_module.__all__}")
print()
print("This list controls what 'from week14_module import *' exports.")
print("It also documents the module's intended public interface.")
print()
print("_format_header is excluded from __all__ for the same reason")
print("it starts with _: it is an internal helper, not a public tool.")


# ============================================================
# PART 4: __name__ == '__main__'
# ============================================================
#
# Every Python file has a built-in attribute called __name__.
# Python sets its value automatically depending on how the
# file is being used:
#
#   - If the file is run directly (python week14_demo.py),
#     Python sets __name__ to the string '__main__'.
#
#   - If the file is imported by another file,
#     Python sets __name__ to the module's name as a string.
#
# This single difference is the foundation of one of the most
# common patterns in Python code.

print("\n" + "=" * 60)
print("PART 4: __name__ == '__main__'")
print("=" * 60)


# ------------------------------------------------------------
# Example 10: __name__ in the running script
# ------------------------------------------------------------
#
# This file is being run directly. Print its __name__ and
# see what Python set it to.

print("\n--- Example 10: __name__ in the running script ---\n")
print(f"  __name__ in week14_demo.py = {__name__!r}")
print()
print("Because this file was launched directly with the Run button")
print("or 'python week14_demo.py', Python set __name__ to '__main__'.")


# ------------------------------------------------------------
# Example 11: __name__ in an imported module
# ------------------------------------------------------------
#
# The same attribute exists on every module object.
# For an imported module, __name__ holds the module's name
# as a string, not '__main__'.

print("\n--- Example 11: __name__ in an imported module ---\n")
print(f"  week14_module.__name__ = {week14_module.__name__!r}")
print()
print("Because week14_module was imported rather than run directly,")
print("Python set its __name__ to 'week14_module'.")


# ------------------------------------------------------------
# Example 12: the if __name__ == '__main__' pattern
# ------------------------------------------------------------
#
# Because __name__ has different values depending on how the
# file is used, a file can test its own __name__ to decide
# whether to run a block of code.
#
# The pattern looks like this:
#
#   if __name__ == '__main__':
#       # this block runs only when the file is executed
#       # directly. It does not run when the file is imported.
#
# Open week14_module.py and find the block at the bottom.
# It contains self-test code for the module's functions.
# When week14_demo.py imported week14_module, that block
# did not run. The module was loaded and its functions were
# defined. The test code was skipped.
#
# To see the self-test block run:
#   1. Open a terminal in VS Code (Terminal > New Terminal)
#   2. Run: python week14_module.py
#   3. Compare that output to what you have seen here.

print("\n--- Example 12: the pattern ---\n")
print("Open week14_module.py in the VS Code editor now.")
print("Scroll to the bottom of the file.")
print("You will find the if __name__ == '__main__': block there.")
print()
print("That block contains self-test code for the module's functions.")
print("When week14_demo.py imported week14_module, that block")
print("did not run. Here is why:")
print()
print(f"  week14_module.__name__ is {week14_module.__name__!r}")
print(f"  The condition  '__main__' == 'week14_module'  is False.")
print(f"  Python skipped the entire block.")
print()
print("To see the block run, open a terminal in VS Code and type:")
print("  python week14_module.py")
print()
print("When you run it directly, __name__ is '__main__'.")
print("The condition is True, and the self-test code executes.")


# ------------------------------------------------------------
# Example 13: Connecting back to Week 8
# ------------------------------------------------------------
#
# You have seen this pattern before.
#
# At the bottom of space_trader.py from Week 8:
#
#   if __name__ == '__main__':
#       main()
#
# That line has been sitting in your code since Week 8.
# Now you know exactly what it means.
#
# space_trader.py was always run directly, never imported.
# So __name__ was always '__main__', and main() always ran.
#
# But the pattern matters for files that play both roles.
# cargo_module.py was imported by space_trader.py. If
# cargo_module.py had test code at the bottom without the
# __name__ guard, that test code would have run every time
# space_trader.py imported it, not just when you were
# testing the module directly.
#
# The guard prevents this. Code inside the block runs only
# when the file is executed directly, not when it is imported
# by another script.

print("\n--- Example 13: Week 8 connection ---\n")
print("From Week 8: bottom of space_trader.py:")
print()
print("  if __name__ == '__main__':")
print("      main()")
print()
print("space_trader.py was always run directly.")
print("__name__ was always '__main__', so main() always ran.")
print()
print("cargo_module.py was always imported.")
print("Its __name__ was 'cargo_module', never '__main__'.")
print("Any self-test code under the guard would have been skipped")
print("automatically during normal program use.")
print()
print("This is the pattern. You have been using it since Week 8.")


# ============================================================
# CONCLUSION
# ============================================================

print("\n" + "=" * 60)
print("CONCLUSION")
print("=" * 60)

print("""
What you have learned this week:

HOW IMPORT WORKS
  Python finds a module by walking sys.path, starting with
  the current directory. It compiles the source to bytecode
  and saves the result in __pycache__. It runs the module's
  top-level code exactly once. Repeated imports retrieve the
  already-loaded module from sys.modules without re-running
  the file.

MODULE NAMESPACES
  Every module is a namespace. Its names are stored in a
  plain dictionary called __dict__. Attribute access with
  dot notation (module.name) is dictionary lookup. The module
  object, like everything in Python, follows the object model
  from Week 3: attributes are entries in an underlying dict.

CONTROLLING EXPORTS
  A leading underscore (_name) signals that a name is internal.
  Python respects this convention in from * imports; names
  beginning with _ are not exported. __all__ makes the public
  interface explicit: only names listed in __all__ are exported
  by from *. Both tools communicate intent rather than enforce
  restriction.

__name__ == '__main__'
  __name__ is set to '__main__' when a file is run directly,
  and to the module's name string when it is imported. The
  if __name__ == '__main__': guard lets a single file serve
  two roles: importable module and standalone script. You have
  been looking at this pattern since Week 8. This week explains why it works.

What the textbook covers in more depth:

  reload(): forces Python to re-run a module's code in a
  running process. Useful in long-running programs and REPL
  sessions. Not relevant to VS Code's run-button workflow.

  Package-relative imports (from . import module): used
  inside packages to import sibling modules. Relevant when
  writing larger multi-directory projects.

  Namespace packages: packages without __init__.py that can
  span multiple directories. An advanced import system feature
  outside the scope of this course.
""")
