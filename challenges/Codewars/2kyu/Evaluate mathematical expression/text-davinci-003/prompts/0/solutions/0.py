def calc(expression):
    # Strip whitespace
    expression = expression.replace(" ", "")

    # Handle parentheses
    while "(" in expression:
        start = expression.index("(")
        end = start + expression[start:].index(")")
        result = calc(expression[start + 1:end])
        expression = expression[:start] + str(result) + expression[end + 1:]

    # Handle multiplication and division
    while "*" in expression or "/" in expression:
        if "*" in expression:
            op = "*"
            index = expression.index("*")
        else:
            op = "/"
            index = expression.index("/")
        num1 = float(expression[:index])
        num2 = float(expression[index + 1:expression.index(" ", index) if " " in expression[index + 1:] else None])
        if op == "*":
            result = num1 * num2
        else:
            result = num1 / num2
        expression = expression[:expression.index(op)] + str(result) + expression[expression.index(" ", index) + 1 if " " in expression[index + 1:] else len(expression):]

    # Handle addition and subtraction
    while "+" in expression or "-" in expression:
        if "+" in expression:
            op = "+"
            index = expression.index("+")
        else:
            op = "-"
            index = expression.index("-")
        num1 = float(expression[:index])
        num2 = float(expression[index + 1:expression.index(" ", index) if " " in expression[index + 1:] else None])
        if op == "+":
            result = num1 + num2
        else:
            result = num1 - num2
        expression = expression[:expression.index(op)] + str(result) + expression[expression.index(" ", index) + 1 if " " in expression[index + 1:] else len(expression):]

    return float(expression)