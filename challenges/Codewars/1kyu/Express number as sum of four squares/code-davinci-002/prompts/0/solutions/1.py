from typing import Tuple

def four_squares(n: int) -> Tuple[int, int, int, int]:
    if n == 0:
        return (0, 0, 0, 0)
    elif n == 1:
        return (1, 0, 0, 0)
    else:
        i = 1
        while i * i <= n:
            a = i * i
            b, c, d = four_squares(n - a)
            if b * b + c * c + d * d == n - a:
                return (i, b, c, d)
            i += 1
        return (0, 0, 0, 0)
