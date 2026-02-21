# Week 4 Overview Video Script

------

Hello everyone, and welcome to Week 4 of Intermediate Python Programming.

Last week, you dove into Chapters 8–9 and explored Python's object model—how names refer to objects, how aliasing works, and why mutation and rebinding behave differently. You worked through the demo examples and completed the quiz, building a mental model of what's happening behind the scenes when Python handles lists, dictionaries, and nested structures.

This week, we're putting that knowledge to work. Week 4 is a **reflection and consolidation week**. There's no new reading. Instead, you'll demonstrate your understanding by finding and fixing bugs in real code—bugs that are caused by exactly the concepts you studied last week.

## What You'll Learn This Week

The core skill this week is **debugging code you didn't write**. In the real world, you won't always be working with code you created from scratch. You'll inherit programs from other developers, or you'll return to your own code months later and wonder what you were thinking. The ability to read unfamiliar code, trace its behavior, and identify where things go wrong is essential.

The bugs you'll encounter this week aren't syntax errors—the program runs just fine. They're **semantic bugs**: the code does something, just not what it's supposed to do. These are harder to find because Python won't tell you anything is wrong. You have to notice that the output doesn't match what you expected, then trace backward to figure out why.

Every bug in this week's exercise is caused by one of the Chapter 8–9 concepts: aliasing when you meant to copy, shallow copy when you needed deep copy, mutable default arguments accumulating across function calls, or using identity when you meant equality. You've seen these patterns in isolation in the demo. Now you'll see them hiding in a larger program, causing the kind of subtle, confusing behavior that frustrates real developers every day.

## Your Week 4 Tasks

Let me walk you through what you need to do this week.

**First**, download the assignment files from the Week 4 Assignments page. You'll get two files: a Python program called `lastname-pet-shelter.py` and a PDF quiz handout. Rename the Python file with your last name before you start working.

**Second**, complete the D2L Quiz. The quiz handout contains 15 multiple-choice questions with properly formatted code examples. Work through the questions using the handout, then submit your answers (A, B, C, or D) in D2L. These questions are similar to the Week 3 quiz but focused on predicting buggy behavior and identifying fixes. Think of it as a warm-up for the debugging exercise.

**Third**, debug the Pet Shelter program. This is the main assignment. The program simulates daily operations at an animal shelter—tracking pets, managing feeding schedules, creating backups, recording adoptions, and checking for duplicates. When you run it, you'll see output for each of these operations. The problem is, the output is wrong in five different places.

Your job is to find the five bugs. Each bug lives in its own short function—I've told you which five functions to focus on. Read the program's output, compare it to what the employees expect (described in the assignment), and figure out which Chapter 8–9 concept is being violated. Then fix the code. Each fix is only one or two lines.

**Fourth**, record your video explanation. This is where you demonstrate not just that you fixed the bugs, but that you understand *why* they were bugs in the first place. For each bug, show the incorrect output, identify the function and line where the bug lives, explain the concept being violated using Chapter 8–9 terminology, show your fix, and prove it works.

After you've covered all five bugs, run your corrected program and compare the output to the expected output provided at the end of the assignment page. Walk through each section verbally and confirm the results are now correct.

Finally, discuss your lessons learned: which bug was hardest to find and why, what surprised you about Python's behavior, and whether any of these bugs could have appeared in your Virtual Pet project.

**Fifth**, submit your work. Upload your corrected Python file to the D2L Dropbox, and upload your video to Kaltura with the naming convention `lastname_Week4_Debugging`.

## Key Concepts You're Applying

As you work through the debugging exercise, you're applying the same concepts from last week—but now you have to recognize them in context, not in isolation.

**Aliasing** happens when you assign one variable to another and think you have two independent copies. You don't. You have two names for the same object. When code creates a "separate" list but both lists change together, aliasing is the culprit.

**Nested structure bugs** happen when you use the `*` operator to create what looks like a grid or table. Instead of independent rows, you get multiple references to the same row. When changing one cell affects an entire column, this is why.

**Shallow versus deep copy** matters when your objects contain other objects. A shallow copy gives you a new outer container, but the inner objects are still shared. When a "backup" isn't truly independent, shallow copy is usually the problem.

**Mutable default arguments** are a classic Python gotcha. When a function uses `[]` or `{}` as a default parameter value, that object is created once and reused across all calls. Data accumulates in ways that make no sense until you understand what's happening.

**Identity versus equality** trips people up when they use `is` to compare values instead of `==`. Two objects can have the same data and still be different objects. Using `is` when you mean `==` causes comparisons to fail unexpectedly.

The debugging exercise has one bug demonstrating each of these concepts. Your job is to match the symptoms to the cause.

## A Note About This Week

This is a different kind of assignment than you've done so far. You're not building something from scratch—you're fixing something that's broken. The program is longer than what you've written, and it uses a few Python features we haven't covered yet. That's intentional.

Don't let the unfamiliar parts distract you. The bugs are all in five short functions, each only a few lines long, using concepts you studied last week. The rest of the code—the display functions, the sample data setup, the automation in `main()`—just works. You don't need to understand every line to complete the assignment.

Focus on the output. When you see something wrong, trace it back to the responsible function. Look at that function with Chapter 8–9 concepts in mind. The bug will reveal itself.

And remember: your fixes should only change code inside those five functions. Don't add new functions, don't restructure the program, don't modify the automation. Each bug can be fixed with one or two lines of code in the right place.

## Wrapping Up

So to summarize: Download the assignment files and complete the D2L Quiz using the handout. Debug the Pet Shelter program by finding the five bugs—one in each of the identified functions—and fix them using what you learned in Chapters 8–9. Record your video explanation, demonstrating each bug and fix, comparing your output to the expected results, and reflecting on what you learned. Then submit your corrected code and video to D2L.

This week is about making the transition from understanding concepts in isolation to recognizing them in practice. The bugs you'll find are exactly the kind of bugs that appear in real programs. Once you've debugged them yourself, you'll be much more likely to avoid them in your own code—and much faster at finding them when they do slip through.

Alright, that's it for the Week 4 overview. Download the files, dig into the code, and I'll see you in your video submissions.

------
