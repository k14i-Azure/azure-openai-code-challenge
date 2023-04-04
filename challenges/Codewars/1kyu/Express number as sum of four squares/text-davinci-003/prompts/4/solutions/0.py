from typing import Tuple

def four_squares(n: int) -> Tuple[int, int, int, int]:
    if n == 0:
        return (0, 0, 0, 0)
    elif n == 1:
        return (1, 0, 0, 0)
    else:
        a = int(n**0.5)
        while a > 0:
            b2 = n - a**2
            b = int(b2**0.5)
            while b >= 0:
                c2 = b2 - b**2
                c = int(c2**0.5)
                while c >= 0:
                    d2 = c2 - c**2
                    d = int(d2**0.5)
                    if d2 == d**2:
                        return (a, b, c, d)
                    c -= 1
                b -= 1
            a -= 1
