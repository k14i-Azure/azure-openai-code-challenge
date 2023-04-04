MOD = 998244353

def height(n, m):
    if n == 0:
        return (0, 0, 0, 0)
    elif n == 1:
        return (1, 0, 0, 0)
    elif n == 2:
        return (1, 1, 0, 0)
    elif n == 3:
        return (1, 1, 1, 0)
    elif n == 4:
        return (1, 1, 1, 1)
    else:
        x = n // 4
        y = n % 4
        z = m // x
        w = m % x
        if y == 0:
            return (x, x, x, x)
        elif y == 1:
            return (x + 1, x, x, x)
        elif y == 2:
            return (x + 1, x + 1, x, x)
        elif y == 3:
            return (x + 1, x + 1, x + 1, x)
        else:
            return (x + 1, x + 1, x + 1, x + 1)
    return (x + y + z + w) % MOD
