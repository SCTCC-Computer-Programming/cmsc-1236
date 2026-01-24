# Week 3 Demo Walkthrough Script

---

Hello everyone, and welcome to the Week 3 demo walkthrough. Today we're going to explore how Python's built-in collection types—lists, dictionaries, sets, and tuples—actually work under the hood. This is a different kind of learning than what we did in CMSC 1203, so let me explain what's changing.

## Understanding the Shift from CMSC 1203

In CMSC 1203, you learned **how to use** Python's collections. You practiced calling `append()` and `pop()`, writing list comprehensions, using dictionary methods like `get()` and `update()`, and reading files with `open()`. You know the syntax, and you can write code that works.

This unit shifts focus to **how Python works internally**. We're going to understand what actually happens when you write `b = a`, why changing one list sometimes affects another variable, and when copying a data structure actually matters. These concepts explain behavior that may have seemed random or confusing in CMSC 1203.

Here's a concrete example of why this matters. Suppose you write code like this: you create a list, assign it to another variable, modify the first variable, and then print the second one. Sometimes the second variable changes. Sometimes it doesn't. Whether it changes depends on *how* you modified the first variable. If you don't understand Python's reference model, this seems unpredictable. Once you understand it, you can predict exactly what will happen every time.

Let's work through the demo.

## Part 1: Names, Objects, and References

The foundation of everything we're covering today is this: in Python, a variable is a **name** that refers to an **object**. When you write `a = [1, 2, 3]`, Python creates a list object in memory, and the name `a` becomes a label pointing to that object. The name and the object are separate things.

This matters because when you write `b = a`, you're not copying the list. You're creating a second name that points to the same object. Now you have two names—`a` and `b`—both referring to the same list in memory. Any change to that list is visible through both names.

Two comparison operators help us distinguish "same object" from "same value." The `is` operator tests **identity**—are these two names pointing to the exact same object in memory? The `==` operator tests **equality**—do these two objects have the same contents? Two different objects can be equal in value but not identical.

**[RUN CELL: Example 1 - Two names referring to the same object]**

Let me run this first cell. We create a list `[1, 2, 3]` and assign it to `a`, then assign `a` to `b`. Look at the output: `a is b` is `True` because both names point to the same object. `a == b` is also `True` because the contents are the same—but that's almost redundant here since it's literally the same object.

**[RUN CELL: Example 2 - Different objects with the same value]**

Now let's see the opposite case. Here we create two separate lists that happen to contain the same values. Look at the output: `x == y` is `True` because the contents match, but `x is y` is `False` because these are two different objects in memory. Python created the list `[1, 2]` twice—once for each assignment.

This distinction becomes critical when you start modifying objects. If two names point to the same object and you modify it, both names see the change. If two names point to different objects that happen to be equal, modifying one doesn't affect the other.

**[RUN CELL: Example 3 - Truth values of objects]**

Before we move on, there's one more foundational concept: every object in Python has a **truth value**. You can use any object directly in an `if` statement, and Python will treat it as either true or false.

The rule is simple: empty things are false, non-empty things are true. Zero is false, non-zero numbers are true. Empty strings, lists, dictionaries, tuples, and sets are all false. `None` is false. Everything else is true.

Look at this example. We have an empty list and a list containing three zeros. The empty list is falsy—even though it exists, it contains nothing. But the list `[0, 0, 0]` is truthy—it contains items, even though those items are zeros. The contents being zero doesn't matter; what matters is that the list is not empty.

This is why Python programmers write `if items:` instead of `if len(items) > 0:`. Both work, but the first is more idiomatic.

## Part 2: Rebinding vs In-Place Mutation

Now we get to the heart of the confusion many students experience. There are two fundamentally different ways to "change" a variable, and they have completely different effects.

**Rebinding** changes which object a name refers to. The original object is unchanged. **Mutation** changes the contents of an existing object. Any name that refers to that object will see the change.

The tricky part is that both can happen after what looks like an assignment statement. `nums = nums + [40]` is rebinding—it creates a new list and makes `nums` point to it. But `nums += [40]` is mutation—it modifies the existing list in place. They look almost identical, but they behave completely differently.

**[RUN CELL: Example 1 - Rebinding creates a new list]**

Let me run this cell. We create a list, create an alias pointing to the same list, then do `nums = nums + [40]`. Look at the output: `nums` has the new item, but `alias` doesn't. And `nums is alias` is `False`—they're no longer the same object.

What happened? The `+` operator created a brand new list containing the old items plus `40`. Then the assignment made `nums` point to this new list. The original list—which `alias` still points to—was never modified.

**[RUN CELL: Example 2 - In-place mutation changes the existing list]**

Now let's see the mutation case. Same setup, but this time we use `nums += [40]`. Look at the output: both `nums` and `alias` show the new item, and `nums is alias` is `True`—they're still the same object.

What happened? The `+=` operator for lists is special—it modifies the existing list in place rather than creating a new one. Since `alias` points to the same object, it sees the change too.

This is one of the most common sources of bugs in Python programs. You think you're working with your own copy of data, but you're actually modifying a shared object. Understanding this distinction helps you predict and prevent these bugs.

## Part 3: Lists—Slice Assignment and Nested Construction

This section covers two list operations that are easy to get wrong if you don't understand the reference model.

First, **slice assignment**. When you assign to a slice like `data[2:5] = ["a", "b"]`, you're modifying the existing list in place. This isn't creating a new list—it's replacing part of the existing one. Any other name referring to that list will see the change.

**[RUN CELL: Example 1 - Slice assignment modifies a list in place]**

Let me run this cell. We start with `[0, 1, 2, 3, 4, 5]` and replace positions 2 through 4 with `["a", "b"]`. Notice the list gets shorter—we replaced three items with two. The key point is that `data` still refers to the same list object; we just changed its contents.

Second, and this is a classic pitfall: **nested list construction with repetition**. When you write `[row] * 3`, you're not creating three separate inner lists. You're creating one outer list containing three references to the same inner list.

**[RUN CELL: Example 2 - Nested lists and repeated references]**

Watch what happens here. We create a row `[0, 0]`, then create a grid by repeating it three times. When we change `grid_bad[0][0]` to 99, look at the output—all three rows changed! This is because all three "rows" are actually the same object. We have one inner list with three references to it.

This is one of those bugs that makes students tear their hair out. They think they created a 3x3 grid, but they actually created one row with three names pointing to it.

**[RUN CELL: Example 3 - Nested lists created as independent inner lists]**

Here's the correct way to do it. Using a list comprehension, `[[0, 0] for _ in range(3)]` creates three separate inner lists. Each iteration of the comprehension creates a new `[0, 0]` object. Now when we change `grid_ok[0][0]`, only the first row changes. The rows are independent objects.

## Part 4: Dictionaries—Insertion Order, Safe Access, and Controlled Updates

Dictionaries have several behaviors that are important to understand for writing predictable code.

**[RUN CELL: Example 1 - Insertion order]**

First, dictionaries preserve insertion order. Since Python 3.7, when you iterate over a dictionary, you get keys in the order they were inserted—not alphabetical order, not sorted order, but insertion order. This cell demonstrates that: we insert `"b"`, then `"a"`, then `"c"`, and that's the order we get back.

**[RUN CELL: Example 2 - Safe access with membership tests and get]**

Second, accessing missing keys. If you try to access a key that doesn't exist with `d["missing"]`, Python raises a KeyError. There are two safe alternatives: check first with `"key" in d`, or use `d.get("key", default)` which returns the default if the key is missing. The `get` method is especially useful when you want to provide a fallback value.

**[RUN CELL: Example 3 - Controlled updates using copy and update]**

Third, controlled updates. When you need to combine two dictionaries without modifying the original, the pattern is: call `copy()` to create a new dictionary, then call `update()` on the copy. Look at the output—`base` is unchanged, but `merged` has the combined result. If we had called `base.update(override)` directly, we would have modified `base`.

**[RUN CELL: Example 4 - Dictionary key views for comparisons]**

Fourth, dictionary key views support set operations. The `keys()` method returns a view that you can use with `&` for intersection and `-` for difference. This is useful when you need to find common keys between dictionaries or keys that exist in one but not the other.

**[RUN CELL: Example 5 - Dictionary comprehensions]**

Finally, dictionary comprehensions. You learned list comprehensions in CMSC 1203—dictionary comprehensions follow the same pattern but produce key-value pairs. This example shows a common use case: combining two parallel lists into a lookup table. Instead of searching through a names list to find a position and then indexing into a scores list, you build a dictionary that maps names directly to scores. One line of code, and now lookups are instant.

## Part 5: Sets—Uniqueness and Hashability

Sets are collections of unique values. When you add duplicate items, they're automatically removed.

**[RUN CELL: Example 1 - De-duplication by constructing a set]**

This cell demonstrates the most common use of sets: removing duplicates. We have a list with repeated items, and converting it to a set gives us just the unique values. This is much simpler than writing a loop to check for duplicates manually.

**[RUN CELL: Example 2 - Hashability requirement]**

But there's a constraint: set elements must be **hashable**. This means their value can't change in a way that affects their hash. Mutable objects like lists can't be set elements because you could add a list to a set, then modify the list, and now the set's internal organization is broken.

This cell tries to create a set containing lists, and Python raises a TypeError. If you need to store list-like data in a set, convert the lists to tuples first—tuples are immutable and therefore hashable.

## Part 6: Tuples—Record-Style Grouping

Tuples are similar to lists—they're ordered sequences you can index into—but with one crucial difference: tuples are **immutable**. Once created, you can't change their contents.

**[RUN CELL: Example 1 - Accessing tuple items by index]**

This cell shows that tuples support the same indexing as lists. You can access items by position, use negative indices to count from the end, and so on.

**[RUN CELL: Example 2 - Tuples do not allow item assignment]**

But this cell shows what happens when you try to modify a tuple: Python raises a TypeError. Tuples don't support item assignment because they're immutable.

Why would you want an immutable sequence? Tuples are useful for grouping related values that shouldn't change—like coordinates, database records, or function return values. The immutability also means tuples can be used as dictionary keys and set elements, which lists cannot.

## Part 7: Copying Nested Collection Objects

When a collection contains other collections, copying gets complicated. A **shallow copy** creates a new outer collection but keeps references to the same inner objects. A **deep copy** recursively copies everything.

**[RUN CELL: Example 1 - Shallow copy shares inner lists]**

Let me run this cell. We create a nested list and make a shallow copy using slice notation `nested[:]`. Then we modify an inner list through the copy. Look at the output—the original `nested` also changed! That's because both `nested[0]` and `shallow[0]` point to the same inner list object. The outer lists are different, but they share the same inner lists.

**[RUN CELL: Example 2 - Deep copy creates independent nested objects]**

Now let's see a deep copy. We use `copy.deepcopy()` which recursively copies everything. When we modify an inner list through the deep copy, the original is unaffected. The identity test confirms that `nested[0]` and `deep[0]` are different objects.

When do you need a deep copy? Whenever you're working with nested structures and need to modify the copy without affecting the original. Configuration objects, game state, undo functionality—anywhere you need a truly independent copy of nested data.

## Part 8: File Access with pathlib

In CMSC 1203, you learned to work with files using `open()` and `with` blocks. That approach is universal and still widely used. This section introduces a modern alternative: the `pathlib` module.

A `Path` object represents a file path as an object rather than a plain string. The methods `read_text()` and `write_text()` handle opening, reading or writing, and closing in a single call. It's more concise for simple operations.

**[RUN CELL: Example 1 - File access with pathlib.Path]**

Let me run this cell. We create a Path object, write some text to the file, read it back, then overwrite with new text and read again. Notice how simple each operation is—one method call instead of a `with` block with `open()`, `read()` or `write()`, and implicit close.

Both approaches are valid. Use `pathlib` when you're doing simple read-entire-file or write-entire-file operations. Use the traditional `open()` approach when you need more control—like reading line by line, appending, or working with binary data.

## What's in the Textbook

This demo focused on the core concepts you need to understand Python's reference model and predict how your code will behave. The textbook—Learning Python Chapters 8 and 9—covers additional topics we didn't demonstrate.

**More list operations**: The full range of list methods like `insert()`, `remove()`, `index()`, and `count()`. You know these from CMSC 1203, but the textbook explains how they work in terms of the reference model.

**Sorting details**: How `sort()` and `sorted()` differ—one mutates in place, one returns a new list. The `key` parameter for custom sorting. Case-insensitive sorting with `str.lower`.

**Dictionary construction alternatives**: Different ways to create dictionaries including `dict()` with keyword arguments, `dict()` with key-value pairs, and `dict.fromkeys()`.

**Traditional file handling**: The textbook presents `open()` with `with` blocks as the standard approach. It covers reading line by line, binary files, and the `pickle` module for storing Python objects.

**Comparisons on nested structures**: How Python recursively compares nested lists and dictionaries. What happens when you compare mixed types.

**Type categories**: The distinction between sequences, mappings, and sets. Mutable versus immutable types. How these categories affect what operations are available.

## Closing

Alright, that wraps up the Week 3 demo walkthrough. You've seen how Python's reference model explains behavior that might have seemed mysterious in CMSC 1203. Variables are names pointing to objects. Assignment creates new references, not copies. Mutation changes objects in place, affecting all references. And when you need independent copies of nested structures, you need to be explicit about it.

Take your time working through the demo code yourself. Run each cell, look at the outputs, and make sure you can predict what will happen before you run it. That's the real test of understanding—not just seeing the output, but knowing in advance what it will be.

The textbook will extend these concepts with more examples and edge cases. Once you understand the reference model, the rest falls into place.

Good luck with the materials, and I'll see you in Week 4.
