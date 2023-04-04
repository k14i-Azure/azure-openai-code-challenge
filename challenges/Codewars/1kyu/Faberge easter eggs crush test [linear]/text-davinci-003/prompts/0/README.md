# Prompt 0

```
# Write a python function step by step to solve Expressing number as sum of four squares.

# Begin with following code snippet:
# """
MOD = 998244353

def height(n, m):
"""

# Instructions:
# This is the SUPER performance version of This kata.
# 
# You task is exactly the same as that kata. But this time, you should output result % 998244353, or otherwise the result would be too large.
# 
# Data range
# sometimes
#   n <= 80000
#   m <= 100000
# while sometimes
#   n <= 3000
#   m <= 2^200
# There are 150 random tests. You will need more than just a naive linear algorithm for this task :D

# Test code to pass:
# """
from solution import height
import codewars_test as test

@test.describe('Example tests')
def desc1():
    @test.it("should work for some basic tests")
    def it1():
        test.assert_equals(height(1,51),51)
        test.assert_equals(height(2,1),1)
        test.assert_equals(height(4,17),3213)
        test.assert_equals(height(16,19),524096)
        test.assert_equals(height(23,19),524287)
    @test.it("should work for some advanced tests")
    def it2():
        test.assert_equals(height(13,550),621773656)
        test.assert_equals(height(531,550),424414512)
    @test.it("should work for some serious tests :)")
    def it3():
        test.assert_equals(height(10 ** 4, 10 ** 5),132362171)
        test.assert_equals(height(8*10 ** 4, 10 ** 5),805097588)
        test.assert_equals(height(3000,2 ** 200),141903106)
        test.assert_equals(height(8*10 ** 4, 4*10 **4 ),616494770)
        test.assert_equals(height(4*10 ** 4, 8*10 ** 4),303227698)
"""

# Constraints:
# * Don't repeat yourself. Never repeat `if` and `elif` conditions simply and slightly changing the values like:
# if n == 0:
#     return (0, 0, 0, 0)
# elif n == 1:
#     return (1, 0, 0, 0)
# elif n == 2:
#     return (1, 1, 0, 0)
# ...
# * The code should be clean, organized and constructed.
# * Don't pack non-iterable NoneType object.
# * The execution time must not be longer than 12000 milliseconds.
# * No need to generate test codes.

# Solution in a single function in Python:
```
