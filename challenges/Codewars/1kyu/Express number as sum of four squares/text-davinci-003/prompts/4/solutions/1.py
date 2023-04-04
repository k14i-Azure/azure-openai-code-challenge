from typing import Tuple

def four_squares(n: int) -> Tuple[int, int, int, int]:
    """
    Expresses a given number as a sum of four squares.
    
    Args:
        n (int): The number to be expressed as a sum of four squares.
    
    Returns:
        Tuple[int, int, int, int]: A tuple of four integers, each of which is a square.
    """
    # Initialize the four squares
    a, b, c, d = 0, 0, 0, 0
    
    # If the number is 0, return (0, 0, 0, 0)
    if n == 0:
        return (a, b, c, d)
    
    # If the number is greater than 0, start from the largest square
    else:
        # Find the largest square number that is less than or equal to n
        largest_square = int(n**0.5)
        
        # Set the first square to the largest square
        a = largest_square
        
        # Subtract the largest square from n
        n -= a**2
        
        # If n is 0, return the four squares
        if n == 0:
            return (a, b, c, d)
        
        # If n is greater than 0, find the second largest square
        else:
            # Find the second largest square number that is less than or equal to n
            second_largest_square = int(n**0.5)
            
            # Set the second square to the second largest square
            b = second_largest_square
            
            # Subtract the second largest square from n
            n -= b**2
            
            # If n is 0, return the four squares
            if n == 0:
                return (a, b, c, d)
            
            # If n is greater than 0, find the third largest square
            else:
                # Find the third largest square number that is less than or equal to n
                third_largest_square = int(n**0.5)
                
                # Set the third square to the third largest square
                c = third_largest_square
                
                # Subtract the third largest square from n
                n -= c**2
                
                # If n is 0, return the four squares
                if n == 0:
                    return (a, b, c, d)
                
                # If n is greater than 0, find the fourth largest square
                else:
                    # Set the fourth square to the fourth largest square
                    d = n
                    
                    # Return the four squares
                    return (a, b, c, d)
