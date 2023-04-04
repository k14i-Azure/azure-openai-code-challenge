def expression_matter(a, b, c):
    # Calculate the maximum value by using all possible combinations of a, b, c with [+*()]
    return max(a + b + c, a * b * c, (a + b) * c, a * (b + c))
