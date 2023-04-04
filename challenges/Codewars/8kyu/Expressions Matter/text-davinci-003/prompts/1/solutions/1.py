def expression_matter(a, b, c):
    # Find the maximum of the three numbers
    max_num = max(a, b, c)
    
    # Calculate the maximum of the following expressions
    max_expression = max(a + b + c, a * (b + c), (a + b) * c, a * b * c)
    
    # Return the maximum of the maximum number and the maximum expression
    return max(max_num, max_expression)
