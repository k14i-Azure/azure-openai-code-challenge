from typing import Tuple

def four_squares(n: int) -> Tuple[int, int, int, int]:
    a, b, c, d = 0, 0, 0, 0
    while n > 0:
        if n >= 4:
            a += 1
            n -= 4
        elif n >= 3:
            b += 1
            n -= 3
        elif n >= 2:
            c += 1
            n -= 2
        elif n >= 1:
            d += 1
            n -= 1
    return (a, b, c, d)
