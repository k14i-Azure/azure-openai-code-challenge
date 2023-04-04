from typing import Tuple

def four_squares(n: int) -> Tuple[int, int, int, int]:
    a = int(n**0.5)
    if a*a == n:
        return a, 0, 0, 0
    for b in range(a+1):
        c = int((n - b*b)**0.5)
        if c*c == n - b*b:
            return b, c, 0, 0
        for d in range(c+1):
            e = int((n - b*b - d*d)**0.5)
            if e*e == n - b*b - d*d:
                return b, d, e, 0
            for f in range(e+1):
                if f*f == n - b*b - d*d - e*e:
                    return b, d, e, f
