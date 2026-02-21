# Week 7 Overview Video Script

------

Hello everyone, and welcome to Week 7 of Intermediate Python Programming.

In Weeks 5 and 6, you worked with Python's code structure and assignment features: how programs break down into statements and expressions, extended unpacking with the star operator, the walrus operator, and how augmented assignment interacts with mutable objects.

## What You'll Learn This Week

Chapters 12 and 13 revisit `if` statements, `for` loops, and `while` loops. You already know how to write these from CMSC 1203. What these chapters explain is the design decisions behind them and the features Gaddis didn't cover.

There are two main threads this week. The first is how Python evaluates truth. You're used to comparisons like `x > 5` producing `True` or `False`. What you may not know is that every Python object has its own truth value. Empty collections, zero, and `None` are all false. Everything else is true. On top of that, the Boolean operators `and` and `or` don't return `True` or `False`. They return the actual object that decided the result. This is how experienced Python programmers write patterns like providing default values or guarding against errors in a single expression.

The second thread is how the `for` loop connects to the reference model you studied in Weeks 3 and 4. When a `for` loop runs, it assigns its variable through ordinary assignment on each iteration. That's the same rebinding operation you've already seen. The consequence is that modifying the loop variable does not change the list you're iterating over. This surprises a lot of people, but it's completely consistent with how Python handles names and objects. The demo walks through why this happens and shows you the alternatives that do work.

Along the way, you'll also see the `match/case` statement for clean multi-value selection, the loop `else` clause and the search problem it solves, and the built-in functions `zip` and `enumerate` that make `for` loops more powerful without adding complexity.

## Your Week 7 Tasks

You have three things to do this week.

First, read Chapters 12 and 13 of Learning Python. These chapters cover a lot of ground, but focus your attention on truth value testing, how `and` and `or` actually work, and the `for` loop mechanics sections. The textbook also covers advanced `match/case` patterns and dictionary-based branching, which are worth reading for awareness but won't be on the quiz.

Second, work through the Week 7 demo. There's no walkthrough video this week, so run each cell yourself, read the explanations, and check whether you can predict the output before you see it. The demo has five parts: truth values and Boolean operators, basic `match/case`, the loop `else` clause, `for` loop mechanics with the reference model, and `zip`/`enumerate` techniques. The centerpiece is Part 4, where you'll see exactly why modifying a loop variable doesn't change the list and what to do instead.

Third, complete the Week 7 D2L quiz using the quiz handout. Download the handout from the assignment page, work through the 30 multiple-choice questions, and submit your answers in D2L. The questions ask you to predict output, trace behavior, and explain why Python does what it does.

Alright, that's it for the Week 7 overview. Go ahead and start the reading and demo, and I'll see you next week.

------
