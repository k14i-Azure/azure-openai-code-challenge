# Prompt 0

```
# Write a python function step by step to solve Loopover.

# Begin with following code snippet:
# """
from typing import List, Optional

def loopover(mixed_up_board: List[List[str]], solved_board: List[List[str]]) -> Optional[List[str]]:
"""

# Instructions:
# Everybody likes sliding puzzles! For this kata, we're going to be looking at a special type of sliding puzzle called Loopover. With Loopover, it is more like a flat rubik's cube than a sliding puzzle. Instead of having one open spot for pieces to slide into, the entire grid is filled with pieces that wrap back around when a row or column is slid.
# 
# Try it out: https://www.openprocessing.org/sketch/576328
# 
# Note: computer scientists start counting at zero!
# 
# Your task: return a List of moves that will transform the unsolved grid into the solved one. All values of the scrambled and unscrambled grids will be unique! Moves will be 2 character long Strings like the ones below.
# 
# For example, if we have the grid:
# 
# ABCDE
# FGHIJ
# KLMNO
# PQRST
# UVWXY
# and we do R0 (move the 0th row right) then we get:
# 
# EABCD
# FGHIJ
# KLMNO
# PQRST
# UVWXY
# Likewise, if we do L0 (move the 0th row left), we get:
# 
# ABCDE
# FGHIJ
# KLMNO
# PQRST
# UVWXY
# if we do U2 (2nd column up):
# 
# ABHDE
# FGMIJ
# KLRNO
# PQWST
# UVCXY
# and if we do D2 (2nd column down) we will once again return to the original grid. With all of this in mind, I'm going to make a Loopover with a scrambled grid, and your solve method will give me a List of moves I can do to get back to the solved grid I give you.
# 
# For example:
# 
# SCRAMBLED GRID:
# 
# DEABC
# FGHIJ
# KLMNO
# PQRST
# UVWXY
# SOLVED GRID:
# 
# ABCDE
# FGHIJ
# KLMNO
# PQRST
# UVWXY
# One possible solution would be ["L0", "L0"] as moving the top row left twice would result in the original, solved grid. Another would be ["R0", "R0", "R0"], etc. etc.
# 
# NOTE: The solved grid will not always look as nice as the one shown above, so make sure your solution can always get the mixed up grid to the "solved" grid!
# 
# Input
# mixedUpBoard and solvedBoard are two-dimensional arrays (or lists of lists) of symbols representing the initial (unsolved) and final (solved) grids.
# 
# Different grid sizes are tested: from 2x2 to 9x9 grids (including rectangular grids like 4x5).
# 
# Output
# Return a list of moves to transform the mixedUpBoard grid to the solvedBoard grid.
# 
# Some configurations cannot be solved. Return null (None in Python) for unsolvable configurations.
# 
# Good luck! Let me know if there are any issues with the kata! :)

# Test code to pass:
# """
def run_test(start, end, unsolvable):
    def board(str):
        return [list(row) for row in str.split('\n')]
    print_info(board(start), board(end))
    moves = loopover(board(start), board(end))
    if unsolvable:
        test.assert_equals(moves, None, 'Unsolvable configuration')
    else:
        test.assert_equals(check(board(start), board(end), moves), True)

@test.it('Test 2x2 (1)')
def test_2x2_1():
    run_test('12\n34', 
             '12\n34', 
             False)
             
@test.it('Test 2x2 (2)')
def test_2x2_1():
    run_test('42\n31',
             '12\n34',
             False)

@test.it('Test 4x5')
def test_4x5_1():
    run_test('ACDBE\nFGHIJ\nKLMNO\nPQRST',
             'ABCDE\nFGHIJ\nKLMNO\nPQRST',
             False)

@test.it('Test 5x5 (1)')
def test_5x5_1():
    run_test('ACDBE\nFGHIJ\nKLMNO\nPQRST\nUVWXY',
             'ABCDE\nFGHIJ\nKLMNO\nPQRST\nUVWXY',
             False)

@test.it('Test 5x5 (2)')
def test_5x5_2():
    run_test('ABCDE\nKGHIJ\nPLMNO\nFQRST\nUVWXY',
             'ABCDE\nFGHIJ\nKLMNO\nPQRST\nUVWXY',
             False)

@test.it('Test 5x5 (3)')
def test_5x5_3():
    run_test('CWMFJ\nORDBA\nNKGLY\nPHSVE\nXTQUI',
             'ABCDE\nFGHIJ\nKLMNO\nPQRST\nUVWXY',
             False)

@test.it('Test 5x5 (unsolvable)')
def test_5x5_4():
    run_test('WCMDJ\nORFBA\nKNGLY\nPHVSE\nTXQUI',
             'ABCDE\nFGHIJ\nKLMNO\nPQRST\nUVWXY',
             True)

@test.it('Test 6x6')
def test_6x6():
    run_test('WCMDJ0\nORFBA1\nKNGLY2\nPHVSE3\nTXQUI4\nZ56789',
             'ABCDEF\nGHIJKL\nMNOPQR\nSTUVWX\nYZ0123\n456789',
             False)
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

# Solution in a single function in Python:
```