def generate(num):
    res = [0]
    for i in range(1, num + 1):
        res += [i] + [i] * (i - 1) + [i]
    return res[:2 * num + 1]
