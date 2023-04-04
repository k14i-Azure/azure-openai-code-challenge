def calc(expression):
    # Strip whitespace
    expression = expression.replace(" ", "")

    # Handle parentheses
    while "(" in expression:
        start = expression.index("(")
        end = start + expression[start:].rindex(")")
        result = calc(expression[start + 1:end])
        expression = expression[:start] + str(result) + expression[end + 1:]

    # Handle multiplication and division
    ops = ["*", "/"]
    while any(op in expression for op in ops):
        for op in ops:
            if op in expression:
                index = expression.index(op)
                num1 = float(expression[:index])
                num2 = float(expression[index + 1:expression.index(op, index + 1) if op in expression[index + 1:] else None])
                if op == "*":
                    result = num1 * num2
                else:
                    result = num1 / num2
                expression = expression[:expression.index(op)] + str(result) + expression[expression.index(op, index + 1) + 1 if op in expression[index + 1:] else len(expression):]

    # Handle addition and subtraction
    ops = ["+", "-"]
    while any(op in expression for op in ops):
        for op in ops:
            if op in expression:
                index = expression.index(op)
                num1 = float(expression[:index])
                num2 = float(expression[index + 1:expression.index(op, index + 1) if op in expression[index + 1:] else None])
                if op == "+":
                    result = num1 + num2
                else:
                    result = num1 - num2
                expression = expression[:expression.index(op)] + str(result) + expression[expression.index(op, index + 1) + 1 if op in expression[index + 1:] else len(expression):]

    return float(expression)
