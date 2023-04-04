from typing import Tuple

def four_squares(n: int) -> Tuple[int, int, int, int]:
    # Step 1: Make a function to check if a number is a perfect square
    def is_perfect_square(n):
        return n == int(n**0.5)**2
    
    # Step 2: Check if the number is a perfect square
    if is_perfect_square(n):
        return (int(n**0.5), 0, 0, 0)
    
    # Step 3: Check if the number is a sum of two perfect squares
    for i in range(int(n**0.5) + 1):
        if is_perfect_square(n - i**2):
            return (i, int((n - i**2)**0.5), 0, 0)
    
    # Step 4: Check if the number is a sum of three perfect squares
    for i in range(int(n**0.5) + 1):
        for j in range(int((n - i**2)**0.5) + 1):
            if is_perfect_square(n - i**2 - j**2):
                return (i, j, int((n - i**2 - j**2)**0.5), 0)
    
    # Step 5: Check if the number is a sum of four perfect squares
    for i in range(int(n**0.5) + 1):
        for j in range(int((n - i**2)**0.5) + 1):
            for k in range(int((n - i**2 - j**2)**0.5) + 1):
                if is_perfect_square(n - i**2 - j**2 - k**2):
                    return (i, j, k, int((n - i**2 - j**2 - k**2)**0.5))
    
    # Step 6: Return None if the number is not a sum of four perfect squares
    return None
