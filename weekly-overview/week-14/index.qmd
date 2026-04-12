---
title: "Week 14 Guide"
subtitle: "Chapters 22–25 – Modules and Packages"
format:
  html:
    toc: true
---

You have been using `import` statements since Week 1 and writing modules since Week 8, when `cargo_module.py` became a separate file that `space_trader.py` depended on. This week explains what has been happening underneath that entire time. Chapters 22–25 cover the module system in full: how Python finds a file when you import it, what it does with that file once found, how a module's names are organized into a namespace, and how a module signals which parts of itself are public.

Chapters 22–25 also revisit two patterns that have been present in the course without full explanation. Module namespaces connect directly to the object model from Week 3: every module's names are stored in a plain dictionary called __dict__, so accessing module.name is dictionary lookup. The if __name__ == '__main__': main() line at the bottom of space_trader.py has been in your code since Week 8. This week explains what __name__ contains and why that guard works.

## Week 14 Assignments

- Here is the link to the **[Week 14 Assignments](../../assignments/week-14/index.qmd)** page.

## Chapters 22–25 concepts

### How import works

Every `import` statement triggers three steps in order: Python finds the module file by walking a list of directories called `sys.path`, compiles the source to bytecode if needed, and runs the module's top-level code once. After the first import, Python stores the loaded module object in `sys.modules`. Subsequent imports retrieve that cached object without re-running the file. This is why a module's top-level code, including any `print()` calls or variable assignments, executes exactly once per program run regardless of how many times it is imported.

The demo examples show:

* `sys.path` printed and enumerated, confirming that the current folder appears first and explaining why `week14_module.py` is found without configuration
* the same module imported three different ways (`import`, `import as`, and `from import`), with the module's top-level `print()` appearing exactly once across all three
* `__pycache__` located in the VS Code Explorer panel and its contents listed from code, with an explanation of what the `.pyc` file contains and why Python creates it

### Module namespaces

A module is a namespace: a container that maps names to objects. Every name assigned at the top level of a module file becomes an attribute of the module object, stored in a plain Python dictionary called `__dict__`. This is the same principle from Week 3: objects have attributes, and those attributes are entries in an underlying dictionary. `dir()` lists all names in a module's namespace. `__dict__` exposes the namespace directly as a dictionary whose keys are name strings and whose values are the objects those names refer to. Attribute access and dictionary lookup are the same operation.

The demo examples show:

* `dir()` called on the imported module, listing all names including dunder attributes Python added automatically
* `__dict__` iterated to display the module's user-defined names and their objects
* `id()` used to confirm that `module.greet` and `module.__dict__['greet']` return the same object in memory, connecting back to Week 3's use of `id()` and `is` for identity testing

### Controlling what a module exports

Python modules have no private keyword. Any name defined in a module can be accessed from outside it. Two conventions let a module signal its intent without enforcing it by force. A leading underscore (`_name`) marks a name as internal: the underscore is a message to other programmers, not a lock. Python enforces this convention in one specific place: `from module import *` skips names that begin with `_`. The `__all__` list makes the public interface explicit: when present, only names listed in `__all__` are exported by `from *`. `__all__` also serves as documentation, giving any programmer reading the module an immediate answer to the question of what it is designed to provide.

The demo examples show:

* a public function and a `_`-prefixed private helper called side by side, confirming both are reachable by qualification
* `from module import *` run before and after, confirming the private name is absent from what was imported
* `__all__` printed directly, showing it as a plain list that controls `from *` and declares the public interface

### `__name__` and the guard pattern

Every Python file has a built-in attribute called `__name__`. When a file is run directly using the Run button or `python filename.py`, Python sets `__name__` to the string `'__main__'`. When a file is imported by another script, Python sets `__name__` to the module's name. This difference is the foundation of the `if __name__ == '__main__':` pattern. Code inside that block runs only when the file is executed directly. When the file is imported, `__name__` is not `'__main__'`, the condition is false, and the block is skipped. The pattern allows a single file to serve two roles: importable module and standalone script.

The demo examples show:

* `__name__` printed inside the running script, confirming it is `'__main__'`
* `week14_module.__name__` printed after import, confirming it is `'week14_module'`
* the guard block in `week14_module.py` traced: why it was skipped during import, and how to trigger it by running the module file directly from the terminal
* the connection to `space_trader.py` and `cargo_module.py` from Week 8: the `if __name__ == '__main__': main()` pattern has been in the course since Week 8; this week explains exactly what it does and why

### Additional features in the reading

Chapters 22–25 cover several topics not demonstrated this week. These are worth reading for awareness but are not the focus of the quiz.

The reading covers:

* `reload()`: forces Python to re-run a module's code in a running process, useful in long-running programs and REPL sessions; not relevant to the VS Code run-button workflow
* package-relative imports (`from . import module`): used inside packages to import sibling modules; relevant when writing larger multi-directory projects
* namespace packages: packages without `__init__.py` that can span multiple directories; an advanced import system feature outside the scope of this course

## Reading expectations for Week 14

As you read Chapters 22–25 and work through the demo, check whether you can answer the following in your own words:

1. What are the three steps Python performs when executing an import statement, and in what order?
2. What is `sys.path`, and why does the directory containing the running script appear first?
3. Why does a module's top-level code run only once, even when the module is imported multiple times in the same program?
4. What does `__pycache__` contain, and what triggers Python to create it?
5. How does a name at the top level of a module file become an attribute of the module object?
6. What is `__dict__` on a module object, and what are its keys and values?
7. What does `id()` confirm when comparing `module.name` to `module.__dict__['name']`?
8. What does a leading underscore on a module-level name signal, and what is the one place Python enforces this convention?
9. What does `__all__` control, and what purpose does it serve beyond that?
10. What value does `__name__` hold when a file is run directly, and what value does it hold when a file is imported?
11. What does the `if __name__ == '__main__':` guard prevent, and what dual role does it allow a file to serve?

## Week 14 tasks

1. Read **Learning Python 6e, Chapters 22–25** (complete).
2. Download both demo files from the Week 14 Assignments page and work through **week14_demo.py** in VS Code.
3. Complete the **Week 14 D2L quiz** (Chapters 22–25 concepts, completed directly in D2L; no handout this week).
