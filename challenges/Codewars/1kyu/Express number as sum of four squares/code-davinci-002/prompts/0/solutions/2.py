from typing import Tuple

def four_squares(n: int) -> Tuple[int, int, int, int]:
    # Check for the trivial case
    if n == 0:
        return (0, 0, 0, 0)
    # If n is not a perfect square, find the largest square
    # less than n and recurse
    x = int(n ** 0.5)
    if x * x != n:
        a, b, c, d = four_squares(n - x * x)
        return (x, a, b, c)
    # Otherwise, we've found a square, and we can recurse
    # to find the other three
    else:
        a, b, c, d = four_squares(x)
        return (a, b, c, d)