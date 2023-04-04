# Prompt 0

```
/*
You are a professional programmer.
Write a python function step by step to solve a problem of Moving Zeros To The End.

Begin with following code snippet:
"""
def move_zeros(lst):
"""
*/

/*
Instructions:

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

"""
move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""
*/

/*
Constraints:
* Never repeat `if` and/or `elif` conditions simply and slightly changing the values like:
"""
if n == 0:
    return (0, 0, 0, 0)
elif n == 1:
    return (1, 0, 0, 0)
elif n == 2:
    return (1, 1, 0, 0)
# ...
"""
* Never repeat `if` and/or `elif` conditions simply and slightly changing the values like:
"""
if n == 0:
    return m
if m == 0:
    return n
if n == 1:
    return m
if m == 1:
    return n
# ...
"""
* The code should be clean, organized and constructed.
* Don't pack non-iterable NoneType object.
* The execution time must not be longer than 12000 milliseconds.
* Consider that available buffer size is up to 1.5 MiB.
* No need to generate test codes.
* No need to add comments.
* Never use "# Your code here".
* Smaller and shorter lines of code is preferred.
*/

/*
Test code you must pass all the cases:
"""
import codewars_test as test
from solution import move_zeros

@test.it("Basic tests")
def youarecute():
    test.assert_equals(move_zeros(
        [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]),
        [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
    test.assert_equals(move_zeros(
        [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
        [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    test.assert_equals(move_zeros([0, 0]), [0, 0])
    test.assert_equals(move_zeros([0]), [0])
    test.assert_equals(move_zeros([]), [])
"""
*/

/*
Solution in a single smart, organized, structured and constructed function in Python that can pass all the test cases:
*/
```