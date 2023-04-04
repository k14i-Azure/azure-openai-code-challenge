from typing import Tuple

def four_squares(n: int) -> Tuple[int, int, int, int]:
    if n == 0:
        return (0, 0, 0, 0)
    a = int(n**0.5)
    while a > 0:
        b = int((n - a**2)**0.5)
        while b > 0:
            c = int((n - a**2 - b**2)**0.5)
            while c > 0:
                d = int((n - a**2 - b**2 - c**2)**0.5)
                if d**2 + c**2 + b**2 + a**2 == n:
                    return (a, b, c, d)
                c -= 1
            b -= 1
        a -= 1
    return (0, 0, 0, 0)
