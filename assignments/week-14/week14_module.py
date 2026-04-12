# ============================================================
# week14_module.py
# Week 14 Demo Module: Chapters 22-25, Modules and Packages
# ============================================================
#
# This file is a module. You do not run it directly.
# It is imported by week14_demo.py.
#
# It is intentionally simple. The functions here matter less
# than how the file is structured. As you work through
# week14_demo.py, you will return to this file several times
# to see how its pieces connect to the concepts in the demo.
#
# ============================================================

# This print statement runs exactly once, on the first import
# of this module. If the module is imported again in the
# same program run, this line does not run again. You will see
# this behavior demonstrated in Part 1 of the demo.

print("  [week14_module] module loaded")


# ============================================================
# Private helper: _format_header
# ============================================================
#
# The leading underscore is a convention that signals: this
# name is intended for internal use only. Python does not
# enforce this. You can still access it from outside the
# module by qualification, but the underscore is a clear
# message to anyone reading the code: this is not part of
# the public interface.

def _format_header(text):
    width = len(text) + 4
    return f"\n  {'=' * width}\n  | {text} |\n  {'=' * width}"


# ============================================================
# __all__: the module's declared public interface
# ============================================================
#
# This list tells Python which names to export when a client
# runs: from week14_module import *
#
# Names not in this list are not exported by that statement.
# Notice that _format_header is absent. It is an internal
# helper, not part of the public interface.

__all__ = ['greet', 'shout', 'word_count']


# ============================================================
# Public functions
# ============================================================

def greet(name):
    """Return a greeting string for the given name."""
    return f"Hello, {name}!"


def shout(text):
    """Return text uppercased with an exclamation mark."""
    return text.upper() + "!"


def word_count(text):
    """Return the number of words in a string."""
    return len(text.split())


# ============================================================
# __name__ == '__main__' self-test block
# ============================================================
#
# This block runs only when this file is executed directly
# (e.g. python week14_module.py). It does not run when the
# module is imported. This is explained fully in Part 4 of
# the demo.
#
# To see this block run:
#   1. Open a terminal in VS Code
#   2. Run: python week14_module.py
#   3. Compare the output to what you see when week14_demo.py
#      imports this module instead.

if __name__ == '__main__':
    print(_format_header("Self-Test: week14_module"))
    print(f"  greet:      {greet('Ada')}")
    print(f"  shout:      {shout('hello world')}")
    print(f"  word_count: {word_count('the quick brown fox')}")
    print()
