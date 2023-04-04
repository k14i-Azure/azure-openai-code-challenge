def expression_matter(a, b, c):
    # Calculate the maximum value of a + b + c
    abc = a + b + c
    # Calculate the maximum value of a * (b + c)
    abc1 = a * (b + c)
    # Calculate the maximum value of a + b * c
    abc2 = a + b * c
    # Calculate the maximum value of (a + b) * c
    abc3 = (a + b) * c
    # Calculate the maximum value of a * b * c
    abc4 = a * b * c
    # Return the maximum value
    return max(abc, abc1, abc2, abc3, abc4)
