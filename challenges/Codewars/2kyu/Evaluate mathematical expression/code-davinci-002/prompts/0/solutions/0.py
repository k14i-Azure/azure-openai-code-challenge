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
                num2 = float(expression[index + 1:expression.index(" ", index) if " " in expression[index + 1:] else None])
                if op == "*":
                    result = num1 * num2
                else:
                    result = num1 / num2
                expression = expression[:expression.index(op)] + str(result) + expression[expression.index(" ", index) + 1 if " " in expression[index + 1:] else len(expression):]

    # Handle addition and subtraction
    ops = ["+", "-"]
    while any(op in expression for op in ops):
        for op in ops:
            if op in expression:
                index = expression.index(op)
                num1 = float(expression[:index])
                num2 = float(expression[index + 1:expression.index(" ", index) if " " in expression[index + 1:] else None])
                if op == "+":
                    result = num1 + num2
                else:
                    result = num1 - num2
                expression = expression[:expression.index(op)] + str(result) + expression[expression.index(" ", index) + 1 if " " in expression[index + 1:] else len(expression):]

    return float(expression)

"""
/*
Notes:
* The key point is to handle the operators in order of precedence.
* It is important to handle the parentheses first.
* It is important to handle the multiplication and division before the addition and subtraction.
* It is important to handle the `*` and `/` before the `+` and `-`.
* It is important to handle the `+` and `-` before the `*` and `/`.
* It is important to handle the `*` and `/` before the `+` and `-`.
* It is important to handle the `+` and `-` before the `*` and `/`.
* It is important to handle the `*` and `/` before the `+` and `-`.
* It is important to handle the `+` and `-` before the `*` and `/`.
* It is important to handle the `*` and `/` before the `+` and `-`.
* It is important to handle the `+` and `-` before the `*` and `/`.
* It is important to handle the `*` and `/` before the `+` and `-`.
* It is important to handle the `+` and `-` before the `*` and `/`.
* It is important to handle the `*` and `/` before the `+` and `-`.
* It is important to handle the `+` and `-` before the `*` and `/`.
"""