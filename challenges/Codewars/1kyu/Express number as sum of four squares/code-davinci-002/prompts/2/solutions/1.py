from typing import Tuple

def four_squares(n: int) -> Tuple[int, int, int, int]:
    a = 0
    b = 0
    c = 0
    d = 0
    while n % 4 == 0:
        n = n // 4
        a += 1
    while n % 8 == 7:
        n = n - 7
        b += 1
    while n % 8 == 3:
        n = n - 3
        c += 1
    while n % 8 == 5:
        n = n - 5
        d += 1
    return (a, b, c, d)
