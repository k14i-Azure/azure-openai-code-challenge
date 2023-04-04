def expression_matter(a, b, c):
    # Initialize the maximum value
    max_value = 0
    
    # Check all the combinations of the three numbers
    # and update the maximum value
    max_value = max(max_value, a + b + c)
    max_value = max(max_value, a * b * c)
    max_value = max(max_value, a + b * c)
    max_value = max(max_value, (a + b) * c)
    max_value = max(max_value, a * (b + c))
    max_value = max(max_value, a * b + c)
    
    # Return the maximum value
    return max_value
