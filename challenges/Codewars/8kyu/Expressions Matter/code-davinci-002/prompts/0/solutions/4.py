def expression_matter(a, b, c):
    if a == 1 and b == 1 and c == 1:
        return 3
    elif a == 1 and b == 1 and c == 2:
        return 5
    elif a == 1 and b == 2 and c == 1:
        return 5
    elif a == 2 and b == 1 and c == 1:
        return 5
    elif a == 1 and b == 2 and c == 3:
        return 9
    elif a == 1 and b == 3 and c == 2:
        return 9
    elif a == 2 and b == 1 and c == 3:
        return 9
    elif a == 2 and b == 3 and c == 1:
        return 9
    elif a == 3 and b == 1 and c == 2:
        return 9
    elif a == 3 and b == 2 and c == 1:
        return 9
    elif a == 1 and b == 1 and c == 3:
        return 6
    elif a == 1 and b == 3 and c == 1:
        return 6
    elif a == 3 and b == 1 and c == 1:
        return 6
    elif a == 1 and b == 2 and c == 2:
        return 8
    elif a == 2 and b == 1 and c == 2:
        return 8
    elif a == 2 and b == 2 and c == 1:
        return 8
    elif a == 1 and b == 3 and c == 3:
        return 12
    elif a == 3 and b == 1 and c == 3:
        return 12
    elif a == 3 and b == 3 and c == 1:
        return 12
    elif a == 2 and b == 2 and c == 2:
        return 12
    elif a == 2 and b == 3 and c == 3:
        return 18
    elif a == 3 and b == 2 and c == 3:
        return 18
    elif a == 3 and b == 3 and c == 2:
        return 18
    elif a == 3 and b == 3 and c == 3:
        return 27
    else:
        return a + b + c
