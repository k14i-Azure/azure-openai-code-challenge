# Prompt 1

```
# Write a python function step by step to solve Expressing number as sum of four squares.

# Begin with following code snippet:
# """
from typing import Tuple

def four_squares(n: int) -> Tuple[int, int, int, int]:
"""

# Instructions:
# Recently you had a quarrel with your math teacher. Not only that nerd demands knowledge of all the theorems, but he turned to be an constructivist devotee! After you recited by heart Lagranges theorem of sum of four squares, he now demands a computer program to obtain such a decomposition, so that to see that you really understand a topic. What a downer!
# 
# You remember well the theorem. Any positive integer can be decomposed into a sum of four squares of integers. Seems not too hard... But after a quarrel, your teacher wants blood. Apparently he will test your program on extremely huge numbers... And your program better finished working before the break - you don't want to get F, do you?
# 
# Tip: random tests feature 20 numbers as high as 2^128 and 20 number as high as 2^1024.

# Test code to pass:
# """
from solution import four_squares

@test.describe("Static tests")
def static_tests():
    for i in [0, 1, 17, 33, 215, 333, 2**12-3, 1234567890, 106369249365575352836589875696130383747]:
        a, b, c, d = four_squares(i)
        error_msg = None
        if type(a) is not int: error_msg = "1st square is not of type int"
        if type(b) is not int: error_msg = "2nd square is not of type int"
        if type(c) is not int: error_msg = "3rd square is not of type int"
        if type(d) is not int: error_msg = "4th square is not of type int"
        s = a * a + b * b + c * c + d * d
        if s != i: 
            error_msg = f"Incorrect sum.\nSquares: [{a}, {b}, {c}, {d}]\nActual: {a * a + b * b + c * c + d * d}\nExpected: {i}"
        if error_msg is not None:
            test.fail(error_msg)
        else:
            test.pass_()
"""

# Constraints:
# * Don't repeat yourself.
# * The code should be clean, organized and constructed.
# * Don't pack non-iterable NoneType object.

# Solution:
```
