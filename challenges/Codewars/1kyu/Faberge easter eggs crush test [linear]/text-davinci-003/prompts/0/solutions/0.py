MOD = 998244353

def height(n, m):
    if n == 0:
        return 0
    if n == 1:
        return m
    if n == 2:
        return m * (m + 1) // 2
    if n == 3:
        return m * (m + 1) * (m + 2) // 6
    if n == 4:
        return m * (m + 1) * (m + 2) * (m + 3) // 24
    if n == 5:
        return m * (m + 1) * (m + 2) * (m + 3) * (m + 4) // 120
    if n == 6:
        return m * (m + 1) * (m + 2) * (m + 3) * (m + 4) * (m + 5) // 720
    if n == 7:
        return m * (m + 1) * (m + 2) * (m + 3) * (m + 4) * (m + 5) * (m + 6) // 5040
    if n == 8:
        return m * (m + 1) * (m + 2) * (m + 3) * (m + 4) * (m + 5) * (m + 6) * (m + 7) // 40320
    return (m * (m + 1) * (m + 2) * (m + 3) * (m + 4) * (m + 5) * (m + 6) * (m + 7) * (m + 8)) % MOD
