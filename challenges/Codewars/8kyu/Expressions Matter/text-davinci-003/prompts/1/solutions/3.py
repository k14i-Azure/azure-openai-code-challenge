def expression_matter(a, b, c):
    # Find the maximum of the three numbers
    max_num = max(a, b, c)
    
    # Calculate the result of the three possible expressions
    expression1 = a * (b + c)
    expression2 = a + b * c
    expression3 = (a + b) * c
    
    # Return the maximum of the three expressions
    return max(expression1, expression2, expression3)
