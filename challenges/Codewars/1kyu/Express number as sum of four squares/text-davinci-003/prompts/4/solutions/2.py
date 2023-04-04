from typing import Tuple

def four_squares(n: int) -> Tuple[int, int, int, int]:
    """
    Function to express a given number as a sum of four squares
    :param n: number to decompose
    :return: a tuple of four integers
    """
    # Initialize a tuple of four zeros
    result = (0, 0, 0, 0)
    # Iterate until n is zero
    while n > 0:
        # Find the largest number that can be expressed as a square
        # and subtract it from n
        max_square = int(n ** 0.5) ** 2
        n -= max_square
        # Increment the first element of the tuple
        result = (result[0] + 1, *result[1:])
        # If the first element of the tuple is greater than 4,
        # subtract 4 from it and increment the second element of the tuple
        if result[0] > 4:
            result = (result[0] - 4, result[1] + 1, *result[2:])
            # If the second element of the tuple is greater than 4,
            # subtract 4 from it and increment the third element of the tuple
            if result[1] > 4:
                result = (result[0], result[1] - 4, result[2] + 1, *result[3:])
                # If the third element of the tuple is greater than 4,
                # subtract 4 from it and increment the fourth element of the tuple
                if result[2] > 4:
                    result = (result[0], result[1], result[2] - 4, result[3] + 1)
    # Return the result
    return result
