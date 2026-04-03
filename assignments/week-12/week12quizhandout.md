# CMSC 1236 - Week 12 Quiz
## Chapter 20: Comprehensions and Generators

*Instructions: For each question, select the best answer. Record your answers (A, B, C, or D) in the D2L quiz.*

---
### Part 1: List Comprehensions

**1.** What does [x ** 2 for x in range(5) if x % 2 == 0] return?

- A) [4, 16]
- B) [0, 1, 4, 9, 16]
- C) [1, 9, 25]
- D) [0, 4, 16]

**2.** In a list comprehension with an `if` clause, when is the `if` condition evaluated?

- A) Before the expression on the left is evaluated
- B) Only on the first iteration
- C) After all items have been collected
- D) After the expression on the left is evaluated

**3.** Which of the following list comprehensions is equivalent to list(filter(lambda x: x > 3, [1,2,3,4,5]))?

- A) [x for x in [1,2,3,4,5] if x < 3]
- B) [x for x in [1,2,3,4,5] if x == 3]
- C) [x for x in [1,2,3,4,5] if x > 3]
- D) [x + 3 for x in [1,2,3,4,5]]

**4.** What does [(x, y) for x in [1, 2] for y in ['a', 'b']] return?

- A) [(1, 'b'), (2, 'a')]
- B) [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
- C) [(1, 'a'), (2, 'b')]
- D) [(1, 2), ('a', 'b')]

**5.** How many items does [(x, y) for x in range(3) for y in range(2)] contain?

- A) 5
- B) 3
- C) 2
- D) 6

**6.** Which comprehension combines the effect of both map() and filter() in a single expression?

- A) [x for x in data if test(x)]
- B) [f(x) for x in data]
- C) [f(x) for x in data if test(x)]
- D) [x for x in data]

**7.** What does [item for row in [[1,2],[3,4],[5,6]] for item in row] return?

- A) [2, 4, 6]
- B) [1, 2, 3, 4, 5, 6]
- C) [1, 3, 5]
- D) [[1,2],[3,4],[5,6]]

---
### Part 2: Set and Dictionary Comprehensions

**8.** What does {len(w) for w in ['hi', 'hello', 'hi', 'bye']} return?

- A) {4}
- B) ['hi', 'hello', 'bye']
- C) {2, 2, 5, 3}
- D) {2, 5, 3}

**9.** What type does a set comprehension enclosed in {} return?

- A) set
- B) list
- C) dict
- D) tuple

**10.** What does {k: v for k, v in [('a', 1), ('b', 2)]} return?

- A) [('a', 1), ('b', 2)]
- B) ('a', 'b')
- C) {'a', 'b'}
- D) {'a': 1, 'b': 2}

**11.** Which expression correctly inverts a dictionary d = {'x': 1, 'y': 2}?

- A) {v: k for k, v in d.items()}
- B) {v for v in d.values()}
- C) {k for k in d.keys()}
- D) {k: v for k, v in d.items()}

**12.** What is the key syntactic difference between a list comprehension and a set comprehension?

- A) Set comprehensions cannot use for loops
- B) Set comprehensions use () instead of []
- C) Set comprehensions use {} instead of []
- D) Set comprehensions require an if clause

---
### Part 3: Generator Functions

**13.** What does a generator function use instead of return to produce values?

- A) produce
- B) yield
- C) next
- D) send

**14.** What does calling a generator function return?

- A) The first value in the series
- B) None
- C) A generator object
- D) A list of all values

**15.** What happens to a generator function's local variables when it yields a value?

- A) They are copied to the caller
- B) They are reset to their initial values
- C) They are deleted
- D) They are retained until the next call

**16.** Given: def gen(): yield 1; yield 2; yield 3 — what does next(gen()) return?

- A) 2
- B) A list [1, 2, 3]
- C) 3
- D) 1

**17.** What exception is raised when a generator has no more values to produce?

- A) GeneratorExit
- B) IndexError
- C) StopIteration
- D) ValueError

**18.** Which statement best explains why map() returns a map object rather than a list?

- A) map() is implemented as a generator, producing values on demand
- B) map() has a bug that was never fixed
- C) map() returns a map object only when given a lambda
- D) map() requires list() to sort its results

**19.** After calling next() twice on a generator that yields 5 values, how many values remain?

- A) 3
- B) 5
- C) 2
- D) 0

---
### Part 4: Generator Expressions

**20.** What does (x ** 2 for x in range(5)) return?

- A) A tuple
- B) [0, 1, 4, 9, 16]
- C) A generator object
- D) (0, 1, 4, 9, 16)

**21.** What is the syntactic difference between a list comprehension and a generator expression?

- A) Generator expressions use () instead of []
- B) Generator expressions require yield
- C) Generator expressions cannot include if clauses
- D) Generator expressions use {} instead of []

**22.** Why do generator expressions use less memory than equivalent list comprehensions?

- A) Generator expressions skip duplicate values
- B) Generator expressions produce values one at a time without building a list
- C) Generator expressions automatically delete used values
- D) Generator expressions store values in compressed form

**23.** Which of the following produces the same result as (x * 2 for x in data if x > 0)?

- A) map(lambda x: x * 2, data)
- B) [x * 2 for x in data]
- C) filter(lambda x: x > 0, data)
- D) map(lambda x: x * 2, filter(lambda x: x > 0, data))

---
### Part 5: Generator Odds and Ends

**24.** What does list(gen) return if gen is a generator that has already been fully iterated?

- A) []
- B) The original values again
- C) None
- D) A StopIteration error

**25.** Which of the following supports multiple iterations without creating a new object?

- A) A generator function result
- B) A map object
- C) A generator expression
- D) A list

**26.** After for x in range(5): pass, what is the value of x?

- A) 0
- B) 5
- C) 4
- D) undefined

**27.** Given x = 99; result = [x for x in range(3)], what is x after the comprehension runs?

- A) 0
- B) 99
- C) 3
- D) 2

**28.** Why is a generator described as a single-pass iterable?

- A) It can only yield one value
- B) It produces each value exactly once and cannot restart
- C) It only works inside for loops
- D) It can only be created once

**29.** What does list(map(lambda x: x + 1, [1, 2, 3])) return?

- A) (2, 3, 4)
- B) [1, 2, 3]
- C) [2, 3, 4]
- D) A map object

**30.** A student assigns gen = (x**2 for x in range(4)) and calls list(gen) twice. What does the second call return?

- A) [0, 1, 4, 9]
- B) []
- C) [1, 4, 9, 16]
- D) A StopIteration error
