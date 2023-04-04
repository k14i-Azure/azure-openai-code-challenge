# Prompt 0

```
/*
You are a professional programmer.
Write a python function step by step to solve a problem of Array with distance of N.

Begin with following code snippet:
"""
def generate(num):
"""
*/

/*
Instructions:
## Task
Your task is to write a function that accept a single parameter - a whole number N and generates an array with following properties.

There are exactly 2 * N + 1 elements in this array
There is only one 0 (zero) in array
Other elements are pairs of natural numbers from 1 to N
Number of elements between a pair of numbers is equal to the number itself
For example, the number of elements between pair of 2s should be exactly 2, for 3s - three and so on.

## Examples of arrays
[1, 0, 1]      # Exactly one element between 1s
[1, 2, 1, 0 2] # Exactly one element between 1s and exactly two elements between 2s

## Example usage
generate(4) 
[1, 3, 1, 4, 2, 3, 0, 2, 4]
Notice that there may be multiple solutions for each number. For example, for number 3 both arrays are valid:

[2, 3, 1, 2, 1, 3, 0]
[1, 3, 1, 2, 0, 3, 2]
Notice that a reverse of a correct solution is a correct solution as well.

## Tests
The solution will be tested for N < 1024
*/

/*
Test code you must pass all the cases:
"""
from solution import generate
import codewars_test as test

check_condition = lambda el, arr: el == 0 or len(arr) - 1 - arr[::-1].index(el) - arr.index(el) == el + 1
check_array = lambda num, arr: all([check_condition(el, arr) for el in arr]) and arr.count(0) == 1 and len(arr) == 2 * num + 1

@test.describe("should fit requirements")
def tests():
    # Use "it" to identify the conditions you are testing for
    @test.it("should work for input")
    def test_second_oldest_first():
        test.expect(check_array(2, generate(2)))
        test.expect(check_array(3, generate(3)))
        
        test.expect(check_array(5, generate(5)))
        
        test.expect(check_array(7, generate(7)))
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
*/

/*
Wrong solution 1:
"""
def generate(num):
    return [0] + [x for x in range(1, num + 1) for _ in range(x)] + [x for x in range(num, 0, -1) for _ in range(x)]
"""
In this case, it fails on all the test cases.
*/

/*
Wrong solution 2:
"""
def generate(num):
    arr = [0]
    for i in range(1, num + 1):
        arr += [j for j in range(i, 0, -1)] + [j for j in range(1, i + 1)]
    return arr
"""
In this case, it fails on all the test cases.
*/

/*
Wrong solution 3:
"""
def generate(num):
    res = [0]
    for i in range(1, num + 1):
        res += list(range(i, 0, -1)) + list(range(1, i + 1))
    return res
"""
In this case, it fails on all the test cases.
*/

/*
Wrong solution 4:
"""
def generate(num):
    res = [0]
    for i in range(1, num + 1):
        res += [i] * i + [i] * i
    return res
"""
In this case, it fails on all the test cases.
*/

/*
Wrong solution 5:
"""
def generate(num):
    res = [0]
    for i in range(1, num + 1):
        res += [i] + [i] * (i - 1) + [i]
    return res
"""
In this case, it fails on all the test cases.
*/

/*
Wrong solution 6:
"""
def generate(num):
    res = [0]
    for i in range(1, num + 1):
        res += [i] + [i] * (i - 1) + [i]
    return res[:2 * num + 1]
"""
In this case, it fails on all the test cases.
*/

/*
Wrong solution 7:
"""
def generate(num):
    res = [0]
    for i in range(1, num + 1):
        res += [i] * i + [i] * i
    return res[:2 * num + 1]
"""
In this case, it fails on all the test cases.
*/

/*
Wrong solution that you must not output #8:
"""
def generate(num):
    res = [0]
    for i in range(1, num + 1):
        res += [i] + [i] * (i - 1) + [i]
    return res[:2 * num + 1]
"""
In this case, it fails on all the test cases. Never output the solution.
*/

/*
Again, here is the test code you must pass all the cases:
"""
from solution import generate
import codewars_test as test

check_condition = lambda el, arr: el == 0 or len(arr) - 1 - arr[::-1].index(el) - arr.index(el) == el + 1
check_array = lambda num, arr: all([check_condition(el, arr) for el in arr]) and arr.count(0) == 1 and len(arr) == 2 * num + 1

@test.describe("should fit requirements")
def tests():
    # Use "it" to identify the conditions you are testing for
    @test.it("should work for input")
    def test_second_oldest_first():
        test.expect(check_array(2, generate(2)))
        test.expect(check_array(3, generate(3)))
        
        test.expect(check_array(5, generate(5)))
        
        test.expect(check_array(7, generate(7)))
"""
*/

/*
Solution in a single smart, organized, structured and constructed function in Python that can pass all the test cases:
*/
```
