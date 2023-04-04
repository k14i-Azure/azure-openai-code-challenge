# Prompt 0

```
/*
You are a professional programmer.
Write a python function step by step to solve a problem of Evaluate mathematical expression.

Begin with following code snippet:
"""
def calc(expression):
"""
*/

/*
Instructions:

## Instructions
Given a mathematical expression as a string you must return the result as a number.

## Numbers
Number may be both whole numbers and/or decimal numbers. The same goes for the returned result.

## Operators
You need to support the following mathematical operators:

* Multiplication `*`
* Division `/` (as floating point division)
* Addition `+`
* Subtraction `-`

Operators are always evaluated from left-to-right, and `*` and `/` must be evaluated before `+` and `-`.

## Parentheses
You need to support multiple levels of nested parentheses, ex. `(2 / (2 + 3.33) * 4) - -6`

## Whitespace
There may or may not be whitespace between numbers and operators.

An addition to this rule is that the minus sign (`-`) used for negating numbers and parentheses will never be separated by whitespace. I.e all of the following are valid expressions.

1-1    // 0
1 -1   // 0
1- 1   // 0
1 - 1  // 0
1- -1  // 2
1 - -1 // 2
1--1   // 2

6 + -(4)   // 2
6 + -( -4) // 10

And the following are invalid expressions

1 - - 1    // Invalid
1- - 1     // Invalid
6 + - (4)  // Invalid
6 + -(- 4) // Invalid

## Validation
You do not need to worry about validation - you will only receive valid mathematical expressions following the above rules.

## Restricted APIs
NOTE: `eval` and `exec` are disallowed in your solution.
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
* As mentioned in the instructions, you cannot use both `eval` and `exec` in your solution.
*/

/*
Test code you must pass all the cases:
"""
from solution import calc
import codewars_test as test

@test.describe("Sample tests")
def _():
    @test.it("Tests")
    def __():
        cases = (
            ("1 + 1", 2),
            ("8/16", 0.5),
            ("3 -(-1)", 4),
            ("2 + -2", 0),
            ("10- 2- -5", 13),
            ("(((10)))", 10),
            ("3 * 5", 15),
            ("-7 * -(6 / 3)", 14)
        )

        for x, y in cases:
            test.assert_equals(calc(x), y)
"""
*/

/*
Wrong solution example #1:
Never output a code as follows:
"""
def calc(expression):
    # Strip whitespace
    expression = expression.replace(" ", "")

    # Handle parentheses
    while "(" in expression:
        start = expression.index("(")
        end = start + expression[start:].index(")")
        result = calc(expression[start + 1:end])
        expression = expression[:start] + str(result) + expression[end + 1:]

    # Handle multiplication and division
    while "*" in expression or "/" in expression:
        if "*" in expression:
            op = "*"
            index = expression.index("*")
        else:
            op = "/"
            index = expression.index("/")
        num1 = float(expression[:index])
        num2 = float(expression[index + 1:expression.index(" ", index)])
        if op == "*":
            result = num1 * num2
        else:
            result = num1 / num2
        expression = expression[:expression.index(op)] + str(result) + expression[expression.index(" ", index) + 1:]

    # Handle addition and subtraction
    while "+" in expression or "-" in expression:
        if "+" in expression:
            op = "+"
            index = expression.index("+")
        else:
            op = "-"
            index = expression.index("-")
        num1 = float(expression[:index])
        num2 = float(expression[index + 1:expression.index(" ", index)])
        if op == "+":
            result = num1 + num2
        else:
            result = num1 - num2
        expression = expression[:expression.index(op)] + str(result) + expression[expression.index(" ", index) + 1:]

    return float(expression)
"""
It causes an exception of `ValueError: substring not found`. The traceback is as follows:
"""
Traceback (most recent call last):
  File "/workspace/default/.venv/lib/python3.11/site-packages/codewars_test/test_framework.py", line 112, in wrapper
    func()
  File "/workspace/default/tests.py", line 20, in __
    test.assert_equals(calc(x), y)
                       ^^^^^^^
  File "/workspace/default/solution.py", line 38, in calc
    num2 = float(expression[index + 1:expression.index(" ", index)])
                                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: substring not found
"""
*/

/*
Wrong solution example #2:
Never output a code as follows:
"""
def calc(expression):
    # Strip whitespace
    expression = expression.replace(" ", "")

    # Handle parentheses
    while "(" in expression:
        start = expression.index("(")
        end = start + expression[start:].index(")")
        result = calc(expression[start + 1:end])
        expression = expression[:start] + str(result) + expression[end + 1:]

    # Handle multiplication and division
    ops = ["*", "/"]
    while any(op in expression for op in ops):
        for op in ops:
            if op in expression:
                index = expression.index(op)
                num1 = float(expression[:index])
                num2 = float(expression[index + 1:expression.index(" ", index)])
                if op == "*":
                    result = num1 * num2
                else:
                    result = num1 / num2
                expression = expression[:expression.index(op)] + str(result) + expression[expression.index(" ", index) + 1:]

    # Handle addition and subtraction
    ops = ["+", "-"]
    while any(op in expression for op in ops):
        for op in ops:
            if op in expression:
                index = expression.index(op)
                num1 = float(expression[:index])
                num2 = float(expression[index + 1:expression.index(" ", index)])
                if op == "+":
                    result = num1 + num2
                else:
                    result = num1 - num2
                expression = expression[:expression.index(op)] + str(result) + expression[expression.index(" ", index) + 1:]

    return float(expression)
"""
It causes an exception of `ValueError: substring not found`. The traceback is as follows:
"""
Traceback (most recent call last):
  File "/workspace/default/.venv/lib/python3.11/site-packages/codewars_test/test_framework.py", line 112, in wrapper
    func()
  File "/workspace/default/tests.py", line 20, in __
    test.assert_equals(calc(x), y)
                       ^^^^^^^
  File "/workspace/default/solution.py", line 34, in calc
    num2 = float(expression[index + 1:expression.index(" ", index)])
                                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: substring not found
"""
*/

/*
Wrong solution example #3:
Never output a code as follows:
"""
def calc(expression):
    # Strip whitespace
    expression = expression.replace(" ", "")

    # Handle parentheses
    while "(" in expression:
        start = expression.index("(")
        end = start + expression[start:].index(")")
        result = calc(expression[start + 1:end])
        expression = expression[:start] + str(result) + expression[end + 1:]

    # Handle multiplication and division
    while "*" in expression or "/" in expression:
        if "*" in expression:
            op = "*"
            index = expression.index("*")
        else:
            op = "/"
            index = expression.index("/")
        num1 = float(expression[:index])
        num2 = float(expression[index + 1:expression.index(op) + 1])
        if op == "*":
            result = num1 * num2
        else:
            result = num1 / num2
        expression = expression[:expression.index(op)] + str(result) + expression[expression.index(op) + 1:]

    # Handle addition and subtraction
    while "+" in expression or "-" in expression:
        if "+" in expression:
            op = "+"
            index = expression.index("+")
        else:
            op = "-"
            index = expression.index("-")
        num1 = float(expression[:index])
        num2 = float(expression[index + 1:expression.index(op) + 1])
        if op == "+":
            result = num1 + num2
        else:
            result = num1 - num2
        expression = expression[:expression.index(op)] + str(result) + expression[expression.index(op) + 1:]

    return float(expression)
"""
It causes an exception of `ValueError: could not convert string to float: ''`. The traceback is as follows:
"""
Traceback (most recent call last):
  File "/workspace/default/.venv/lib/python3.11/site-packages/codewars_test/test_framework.py", line 112, in wrapper
    func()
  File "/workspace/default/tests.py", line 20, in __
    test.assert_equals(calc(x), y)
                       ^^^^^^^
  File "/workspace/default/solution.py", line 38, in calc
    num2 = float(expression[index + 1:expression.index(op) + 1])
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: could not convert string to float: ''
"""
*/

/*
Wrong solution example #4:
Never output a code as follows:
"""
def calc(expression):
    # Strip whitespace
    expression = expression.replace(" ", "")

    # Handle parentheses
    while "(" in expression:
        start = expression.index("(")
        end = start + expression[start:].rindex(")")
        result = calc(expression[start + 1:end])
        expression = expression[:start] + str(result) + expression[end + 1:]

    # Handle multiplication and division
    ops = ["*", "/"]
    while any(op in expression for op in ops):
        for op in ops:
            if op in expression:
                index = expression.index(op)
                num1 = float(expression[:index])
                num2 = float(expression[index + 1:expression.index(" ", index) if " " in expression[index + 1:] else None])
                if op == "*":
                    result = num1 * num2
                else:
                    result = num1 / num2
                expression = expression[:expression.index(op)] + str(result) + expression[expression.index(" ", index) + 1 if " " in expression[index + 1:] else len(expression):]

    # Handle addition and subtraction
    ops = ["+", "-"]
    while any(op in expression for op in ops):
        for op in ops:
            if op in expression:
                index = expression.index(op)
                num1 = float(expression[:index])
                num2 = float(expression[index + 1:expression.index(" ", index) if " " in expression[index + 1:] else None])
                if op == "+":
                    result = num1 + num2
                else:
                    result = num1 - num2
                expression = expression[:expression.index(op)] + str(result) + expression[expression.index(" ", index) + 1 if " " in expression[index + 1:] else len(expression):]

    return float(expression)
"""
It causes an exception of `ValueError: could not convert string to float: ''`. The traceback is as follows:
"""
Traceback (most recent call last):
  File "/workspace/default/.venv/lib/python3.11/site-packages/codewars_test/test_framework.py", line 112, in wrapper
    func()
  File "/workspace/default/tests.py", line 20, in __
    test.assert_equals(calc(x), y)
                       ^^^^^^^
  File "/workspace/default/solution.py", line 10, in calc
    result = calc(expression[start + 1:end])
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/workspace/default/solution.py", line 33, in calc
    num1 = float(expression[:index])
           ^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: could not convert string to float: ''
"""
*/

/*
Solution in a single smart, organized, structured and constructed function in Python that can pass all the test cases:
*/
```