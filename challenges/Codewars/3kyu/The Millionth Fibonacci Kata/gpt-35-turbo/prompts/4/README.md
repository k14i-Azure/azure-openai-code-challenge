# Prompt 4

```
/*
You are a professional programmer.
Write a python function step by step to solve a problem of Moving Zeros To The End.

Begin with following code snippet:
"""
def fib(n):
"""
*/

/*
Instructions:

The year is 1214. One night, Pope Innocent III awakens to find the the archangel Gabriel floating before him. Gabriel thunders to the pope:

> Gather all of the learned men in Pisa, especially Leonardo Fibonacci. In order for the crusades in the holy lands to be successful, these men must calculate the millionth number in Fibonacci's recurrence. Fail to do this, and your armies will never reclaim the holy land. It is His will.

The angel then vanishes in an explosion of white light.

Pope Innocent III sits in his bed in awe. How much is a million? he thinks to himself. He never was very good at math.

He tries writing the number down, but because everyone in Europe is still using Roman numerals at this moment in history, he cannot represent this number. If he only knew about the invention of zero, it might make this sort of thing easier.

He decides to go back to bed. He consoles himself, The Lord would never challenge me thus; this must have been some deceit by the devil. A pretty horrendous nightmare, to be sure.

Pope Innocent III's armies would go on to conquer Constantinople (now Istanbul), but they would never reclaim the holy land as he desired.
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
* Use List Comprehensions instead of `for` or `while` loop to improve performance if possible.
* Do not use `for` or `while` loop for performance if possible.
* Handle exceptions like IndexError.
*/

/*
Test code you must pass all the cases:
"""
test.assert_equals(fib(0),0)
test.assert_equals(fib(1),1)
test.assert_equals(fib(2),1)
test.assert_equals(fib(3),2)
test.assert_equals(fib(4),3)
test.assert_equals(fib(5),5)
test.assert_equals(fib(1000),43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875)
"""
*/

/*
Wrong solution example #1:
Never output solutions as follows:
"""
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
"""
It causes an exception of `RecursionError: maximum recursion depth exceeded`. The traceback is as follows:
"""
Traceback (most recent call last):
  File "/workspace/default/tests.py", line 9, in <module>
    test.assert_equals(fib(1000),43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875)
                       ^^^^^^^^^
  File "/workspace/default/solution.py", line 7, in fib
    return fib(n-1) + fib(n-2)
           ^^^^^^^^
  File "/workspace/default/solution.py", line 7, in fib
    return fib(n-1) + fib(n-2)
           ^^^^^^^^
  File "/workspace/default/solution.py", line 7, in fib
    return fib(n-1) + fib(n-2)
           ^^^^^^^^
  [Previous line repeated 996 more times]
RecursionError: maximum recursion depth exceeded
"""
*/

/*
Wrong solution example #2:
Never output solutions as follows:
"""
def fib(n):
    return (lambda x: (x[0], x[1], x[2], x[3]))(lambda x: (x[1], x[0]+x[1], x[2]+1, x[3]+x[0]) if x[2] < n else x)((0, 1, 0, 0))
"""
It causes an exception of `TypeError: 'function' object is not subscriptable`. The traceback is as follows:
"""
Traceback (most recent call last):
  File "/workspace/default/tests.py", line 3, in <module>
    test.assert_equals(fib(0),0)
                       ^^^^^^
  File "/workspace/default/solution.py", line 2, in fib
    return (lambda x: (x[0], x[1], x[2], x[3]))(lambda x: (x[1], x[0]+x[1], x[2]+1, x[3]+x[0]) if x[2] < n else x)((0, 1, 0, 0))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/workspace/default/solution.py", line 2, in <lambda>
    return (lambda x: (x[0], x[1], x[2], x[3]))(lambda x: (x[1], x[0]+x[1], x[2]+1, x[3]+x[0]) if x[2] < n else x)((0, 1, 0, 0))
                       ~^^^
TypeError: 'function' object is not subscriptable
"""
*/

/*
Wrong solution example #3:
Never output solutions as follows:
"""
def fib(n):
    return fib(n-1) + fib(n-2) if n > 1 else n
"""
It causes an exception of `RecursionError: maximum recursion depth exceeded`. The traceback is as follows:
"""
Traceback (most recent call last):
  File "/workspace/default/tests.py", line 9, in <module>
    test.assert_equals(fib(1000),43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875)
                       ^^^^^^^^^
  File "/workspace/default/solution.py", line 10, in fib
    return fib(n-1) + fib(n-2) if n > 1 else n
           ^^^^^^^^
  File "/workspace/default/solution.py", line 10, in fib
    return fib(n-1) + fib(n-2) if n > 1 else n
           ^^^^^^^^
  File "/workspace/default/solution.py", line 10, in fib
    return fib(n-1) + fib(n-2) if n > 1 else n
           ^^^^^^^^
  [Previous line repeated 996 more times]
RecursionError: maximum recursion depth exceeded
"""
*/

/*
Solution in a single smart, organized, structured and constructed function in Python that can pass all the test cases:
*/
```