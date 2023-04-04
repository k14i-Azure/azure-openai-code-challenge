def expression_matter(a, b, c):
    # Find the maximum of the three numbers
    max_num = max(a, b, c)
    
    # If the maximum number is a, return the result of (a + b) * c
    if max_num == a:
        return (a + b) * c
    # If the maximum number is b, return the result of a * (b + c)
    elif max_num == b:
        return a * (b + c)
    # If the maximum number is c, return the result of a + b * c
    else:
        return a + b * c
