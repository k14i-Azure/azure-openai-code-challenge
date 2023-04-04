from typing import Tuple

def four_squares(n: int) -> Tuple[int, int, int, int]:
    if n == 0:
        return (0, 0, 0, 0)
    elif n == 1:
        return (1, 0, 0, 0)
    elif n == 2:
        return (1, 1, 0, 0)
    elif n == 3:
        return (1, 1, 1, 0)
    elif n == 4:
        return (2, 0, 0, 0)
    elif n == 5:
        return (2, 1, 0, 0)
    elif n == 6:
        return (2, 1, 1, 0)
    elif n == 7:
        return (2, 1, 1, 1)
