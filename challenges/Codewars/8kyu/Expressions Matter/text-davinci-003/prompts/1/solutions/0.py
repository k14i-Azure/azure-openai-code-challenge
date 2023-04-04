def expression_matter(a, b, c):
    # Calculate the maximum of the three numbers
    max_num = max(a, b, c)
    
    # Calculate the result of the expression (a + b) * c
    expression_1 = (a + b) * c
    
    # Calculate the result of the expression a * (b + c)
    expression_2 = a * (b + c)
    
    # Calculate the result of the expression a + b * c
    expression_3 = a + b * c
    
    # Calculate the result of the expression (a + b + c)
    expression_4 = a + b + c
    
    # Calculate the result of the expression a * b * c
    expression_5 = a * b * c
    
    # Calculate the result of the expression (a * b) + c
    expression_6 = (a * b) + c
    
    # Calculate the result of the expression a + (b * c)
    expression_7 = a + (b * c)
    
    # Return the maximum of the seven expressions
    return max(expression_1, expression_2, expression_3, expression_4, expression_5, expression_6, expression_7)
