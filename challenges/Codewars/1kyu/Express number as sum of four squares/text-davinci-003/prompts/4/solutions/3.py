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
    else:
        # Initialize the variables
        a = 0
        b = 0
        c = 0
        d = 0
        # Iterate until n is 0
        while n > 0:
            # Check if n is divisible by 4
            if n % 4 == 0:
                a += 1
                n -= 4
            # Check if n is divisible by 3
            elif n % 3 == 0:
                b += 1
                n -= 3
            # Check if n is divisible by 2
            elif n % 2 == 0:
                c += 1
                n -= 2
            # If n is not divisible by 4, 3 or 2, subtract 1
            else:
                d += 1
                n -= 1
        return (a, b, c, d)
