# Prompt 1

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
* Use List Comprehensions instead of `for` or `while` loop to improve performance.
* Use one-liner code if possible.
* Do not use `for` or `while` loop for performance.
* Never use `for` or `while` loop for performance!!!!!
* Handle exceptions like IndexError.
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
Wrong solution #1:
Never output solutions as follows:
"""
def move_zeros(lst):
    zeros = []
    for i in range(len(lst)):
        if lst[i] == 0:
            zeros.append(lst.pop(i))
            i -= 1
    return lst + zeros
"""
In this case, it fails due to unexpected exception of IndexError: list index out of range. The traceback is as follows:
"""
Traceback (most recent call last):
  File "/workspace/default/.venv/lib/python3.11/site-packages/codewars_test/test_framework.py", line 112, in wrapper
    func()
  File "/workspace/default/tests.py", line 6, in youarecute
    test.assert_equals(move_zeros(
                       ^^^^^^^^^^^
  File "/workspace/default/solution.py", line 4, in move_zeros
    if lst[i] == 0:
       ~~~^^^
IndexError: list index out of range
"""
*/

/*
Wrong solution #2:
Never output solutions as follows:
"""
def move_zeros(lst):
    if not lst:
        return lst
    zeros = []
    for i in range(len(lst)):
        if lst[i] == 0:
            zeros.append(lst.pop(i))
            i -= 1
    return lst + zeros
"""
In this case, it fails due to unexpected exception of IndexError: list index out of range. The traceback is as follows:
"""
Traceback (most recent call last):
  File "/workspace/default/.venv/lib/python3.11/site-packages/codewars_test/test_framework.py", line 112, in wrapper
    func()
  File "/workspace/default/tests.py", line 6, in youarecute
    test.assert_equals(move_zeros(
                       ^^^^^^^^^^^
  File "/workspace/default/solution.py", line 6, in move_zeros
    if lst[i] == 0:
       ~~~^^^
IndexError: list index out of range
"""
*/

/*
Wrong solution #3:
Never output solutions as follows:
"""
def move_zeros(lst):
    if not lst:
        return lst
    i = 0
    while i < len(lst):
        if lst[i] == 0:
            lst.append(lst.pop(i))
        else:
            i += 1
    return lst
"""
In this case, it fails due to Execution Timed Out (12000 ms).
*/

/*
Wrong solution #4:
Never output solutions as follows:
"""
def move_zeros(lst):
    if not lst:
        return lst
    i = 0
    while i < len(lst):
        if lst[i] == 0:
            lst.append(lst.pop(i))
        else:
            i += 1
    return lst
"""
In this case, it fails due to Execution Timed Out (12000 ms).
*/

/*
Solution in a single smart, organized, structured and constructed function in Python that can pass all the test cases:
*/
```