def height(n, m):
    MOD = 998244353
    dp = [[[[0 for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)]
    dp[0][0][0][0] = 1
    for i in range(1, n + 1):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    for p in range(2):
                        for q in range(2):
                            for r in range(2):
                                for s in range(2):
                                    if p + q + r + s > j + k + l:
                                        continue
                                    if p + q + r + s == j + k + l and (p, q, r, s) > (j, k, l, 0):
                                        continue
                                    if i == n and p + q + r + s < j + k + l:
                                        continue
                                    if i == n and p + q + r + s == j + k + l and (p, q, r, s) < (j, k, l, 0):
                                        continue
                                    dp[i][j + (p + q + r + s)][k + (p + q + r)][l + (p + q)][s] += dp[i - 1][j][k][l][p][q][r][s]
                                    dp[i][j + (p + q + r + s)][k + (p + q + r)][l + (p + q)][s] %= MOD
    res = 0
    for i in range(1, n + 1):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    res += dp[i][j][k][l][j][k][l][1]
                    res %= MOD
    return res % MOD
