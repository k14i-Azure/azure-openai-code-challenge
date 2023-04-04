def expression_matter(a, b, c):
    # Calculate the result of the three possible expressions
    expression1 = a * (b + c)
    expression2 = a * b * c
    expression3 = a + b * c
    expression4 = (a + b) * c
    expression5 = a + b + c
    
    # Return the maximum of the five expressions
    return max(expression1, expression2, expression3, expression4, expression5)
