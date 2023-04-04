from typing import Tuple

def four_squares(n: int) -> Tuple[int, int, int, int]:
    a, b, c, d = 0, 0, 0, 0
    while n > 0:
        if n >= 4:
            d += 1
            n -= 4
        elif n >= 1:
            c += 1
            n -= 1
        elif n >= 1:
            b += 1
            n -= 1
        elif n >= 1:
            a += 1
            n -= 1
    return (a, b, c, d)
