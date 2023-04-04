# Prompt 1

```
/*
You are a professional programmer.
Write a python function step by step to solve a problem of Expressions Matter.

Begin with following code snippet:
"""
def expression_matter(a, b, c):
"""
*/

/*
Instructions:

## Task
Given three integers a ,b ,c, return the largest number obtained after inserting the following operators and brackets: +, *, ()
In other words , try every combination of a,b,c with [*+()] , and return the Maximum Obtained (Read the notes for more detail about it)

## Example
With the numbers are 1, 2 and 3 , here are some ways of placing signs and brackets:

1 * (2 + 3) = 5
1 * 2 * 3 = 6
1 + 2 * 3 = 7
(1 + 2) * 3 = 9
So the maximum value that you can obtain is 9.

## Notes
The numbers are always positive.
The numbers are in the range (1  ≤  a, b, c  ≤  10).
You can use the same operation more than once.
It's not necessary to place all the signs and brackets.
Repetition in numbers may occur .
You cannot swap the operands. For instance, in the given example you cannot get expression (1 + 3) * 2 = 8.

## Input >> Output Examples:
expressionsMatter(1,2,3)  ==>  return 9

### Explanation:
After placing signs and brackets, the Maximum value obtained from the expression (1+2) * 3 = 9.

expressionsMatter(1,1,1)  ==>  return 3

### Explanation:
After placing signs, the Maximum value obtained from the expression is 1 + 1 + 1 = 3.

expressionsMatter(9,1,1)  ==>  return 18

### Explanation:
After placing signs and brackets, the Maximum value obtained from the expression is 9 * (1+1) = 18. ___# Task

Given three integers a ,b ,c, return the largest number obtained after inserting the following operators and brackets: +, *, ()
In other words , try every combination of a,b,c with [*+()] , and return the Maximum Obtained

## Example
With the numbers are 1, 2 and 3 , here are some ways of placing signs and brackets:

1 * (2 + 3) = 5
1 * 2 * 3 = 6
1 + 2 * 3 = 7
(1 + 2) * 3 = 9
So the maximum value that you can obtain is 9.

## Notes
The numbers are always positive.
The numbers are in the range (1  ≤  a, b, c  ≤  10).
You can use the same operation more than once.
It's not necessary to place all the signs and brackets.
Repetition in numbers may occur .
You cannot swap the operands. For instance, in the given example you cannot get expression (1 + 3) * 2 = 8.

## Input >> Output Examples:
expressionsMatter(1,2,3)  ==>  return 9

### Explanation:
After placing signs and brackets, the Maximum value obtained from the expression (1+2) * 3 = 9.

expressionsMatter(1,1,1)  ==>  return 3
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
*/

/*
Wrong solution that you must not output #1:
"""
def expression_matter(a, b, c):
    if a == 1 and b == 1 and c == 1:
        return 3
    elif a == 1 and b == 1 and c == 2:
        return 5
    elif a == 1 and b == 2 and c == 1:
        return 5
    elif a == 2 and b == 1 and c == 1:
        return 5
    elif a == 1 and b == 2 and c == 3:
        return 9
    elif a == 1 and b == 3 and c == 2:
        return 9
    elif a == 2 and b == 1 and c == 3:
        return 9
    elif a == 2 and b == 3 and c == 1:
        return 9
    elif a == 3 and b == 1 and c == 2:
        return 9
    elif a == 3 and b == 2 and c == 1:
        return 9
    elif a == 1 and b == 1 and c == 3:
        return 6
    elif a == 1 and b == 3 and c == 1:
        return 6
    elif a == 3 and b == 1 and c == 1:
        return 6
    elif a == 1 and b == 2 and c == 2:
        return 8
    elif a == 2 and b == 1 and c == 2:
        return 8
    elif a == 2 and b == 2 and c == 1:
        return 8
    elif a == 1 and b == 3 and c == 3:
        return 12
    elif a == 3 and b == 1 and c == 3:
        return 12
    elif a == 3 and b == 3 and c == 1:
        return 12
    elif a == 2 and b == 2 and c == 2:
        return 12
    elif a == 2 and b == 3 and c == 3:
        return 18
    elif a == 3 and b == 2 and c == 3:
        return 18
    elif a == 3 and b == 3 and c == 2:
        return 18
    elif a == 3 and b == 3 and c == 3:
        return 27
    else:
        return a + b + c
"""
In this case, it passes only on 5 test cases and fails on 16 test cases. Never output the solution.
*/

/*
Wrong solution that you must not output #2:
"""
def expression_matter(a, b, c):
    # Find the maximum of the three numbers
    max_num = max(a, b, c)
    
    # If the maximum number is a, return the result of (a + b) * c
    if max_num == a:
        return (a + b) * c
    # If the maximum number is b, return the result of a * (b + c)
    elif max_num == b:
        return a * (b + c)
    # If the maximum number is c, return the result of a + b * c
    else:
        return a + b * c
"""
In this case, it passes only on 5 test cases and fails on 16 test cases. Never output the solution.
*/

/*
Solution in a single smart, organized, structured and constructed function in Python that can pass all the test cases:
*/
```
