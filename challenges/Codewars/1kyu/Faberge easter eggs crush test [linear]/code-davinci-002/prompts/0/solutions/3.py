def height(n, m):
    def pow_mod(a, b):
        if b == 0:
            return 1
        elif b == 1:
            return a
        elif b % 2 == 0:
            return pow_mod(a * a % MOD, b // 2)
        else:
            return a * pow_mod(a * a % MOD, b // 2) % MOD
    def inverse(a):
        return pow_mod(a, MOD - 2)
    def comb(n, m):
        if n < m:
            return 0
        elif n == m:
            return 1
        elif m == 0:
            return 1
        elif m == 1:
            return n
        elif m == 2:
            return n * (n - 1) // 2
        elif m == 3:
            return n * (n - 1) * (n - 2) // 6
        elif m == 4:
            return n * (n - 1) * (n - 2) * (n - 3) // 24
        else:
            return 0
    if n == 0:
        return 1
    elif n == 1:
        return m
    elif n == 2:
        return m * (m - 1) // 2
    elif n == 3:
        return m * (m - 1) * (m - 2) // 6
    elif n == 4:
        return m * (m - 1) * (m - 2) * (m - 3) // 24
    elif n == 5:
        return m * (m - 1) * (m - 2) * (m - 3) * (m - 4) // 120
    elif n == 6:
        return m * (m - 1) * (m - 2) * (m - 3) * (m - 4) * (m - 5) // 720
    elif n == 7:
        return m * (m - 1) * (m - 2) * (m - 3) * (m - 4) * (m - 5) * (m - 6) // 5040
    elif n == 8:
        return m * (m - 1) * (m - 2) * (m - 3) * (m - 4) * (m - 5) * (m - 6) * (m - 7) // 40320
    else:
        return 0
