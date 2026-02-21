# Week 6 Quiz — Answer Key

**Distribution: A=4, B=4, C=4, D=3**

| # | Answer | Concept | Explanation |
|---|--------|---------|-------------|
| 1 | C | Program hierarchy | Programs → Modules → Statements → Expressions (→ Objects) |
| 2 | A | Statement vs expression | `len("hello")` produces a value; the others perform actions |
| 3 | B | Extended unpacking `first, *rest` | `first` gets the single element `10`, `*rest` collects into a list |
| 4 | D | Extended unpacking `first, *middle, last` | `*scores` collects middle elements into a list; `final` gets `72` |
| 5 | A | Starred name can be empty | With exactly 2 elements, `first=1`, `last=2`, `*middle=[]` |
| 6 | D | Extended unpacking from tuple | `*` always collects into a list, even when unpacking a tuple |
| 7 | B | Walrus operator in loop | doubled values: 30,16,44,6,34 — those >20 are 30,44,34 |
| 8 | C | Walrus precedence (no parens) | Without parens: `x := (len("hello") > 3)` → `x := True` |
| 9 | C | Walrus precedence (with parens) | `(n := 4) > 2` → n is 4, condition True, prints 4 |
| 10 | A | Multi-target assignment + mutation | `a = b = [1,2,3]` shares one list; `.append(4)` mutates it |
| 11 | B | Multi-target assignment + rebinding | `a = b = 0` shares ref; `a = a + 5` rebinds `a`, `b` unchanged |
| 12 | D | Augmented `+=` mutates lists | `x += [40]` calls `__iadd__`, mutates in place; `y` sees change |
| 13 | A | `+` creates new list | `x = x + [40]` rebinds `x` to new list; `y` still refers to original |
| 14 | C | Print `sep` and `end` | `end="!"` replaces newline, so next print continues on same line |
| 15 | B | Walrus operator definition | `:=` assigns and returns the value as part of the expression |
