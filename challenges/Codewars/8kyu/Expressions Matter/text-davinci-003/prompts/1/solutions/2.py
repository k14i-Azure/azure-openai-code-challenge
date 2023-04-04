def expression_matter(a, b, c):
    # Find the maximum of the three numbers
    max_num = max(a, b, c)
    
    # Calculate the result of all the possible combinations of the three numbers
    result1 = a + b + c
    result2 = a * b * c
    result3 = a + b * c
    result4 = a * b + c
    result5 = (a + b) * c
    result6 = a * (b + c)
    
    # Find the maximum of the results
    max_result = max(result1, result2, result3, result4, result5, result6)
    
    # Return the maximum of the three numbers and the maximum of the results
    return max(max_num, max_result)
