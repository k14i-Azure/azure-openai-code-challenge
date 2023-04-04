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
                                    dp[i & 1][j + (p + q + r + s)][k + (p + q + r)][l + (p + q)][s] += dp[(i - 1) & 1][j][k][l][p][q][r][s]
                                    dp[i & 1][j + (p + q + r + s)][k + (p + q + r)][l + (p + q)][s] %= MOD
                                    dp[(i - 1) & 1][j][k][l][p][q][r][s] = 0
    res = 0
    for i in range(1, n + 1):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    res += dp[i & 1][j][k][l][j][k][l][1]
                    res %= MOD
    return res % MOD

"""
# Sample Test
print(height(1,51)) # Expected output: 51
print(height(2,1)) # Expected output: 1
print(height(4,17)) # Expected output: 3213
print(height(16,19)) # Expected output: 524096
print(height(23,19)) # Expected output: 524287
print(height(13,550)) # Expected output: 621773656
print(height(531,550)) # Expected output: 424414512
print(height(10 ** 4, 10 ** 5)) # Expected output: 132362171
print(height(8*10 ** 4, 10 ** 5)) # Expected output: 805097588
print(height(3000,2 ** 200)) # Expected output: 141903106
print(height(8*10 ** 4, 4*10 **4 )) # Expected output: 616494770
print(height(4*10 ** 4, 8*10 ** 4)) # Expected output: 303227698

# Performance Test
import time
start = time.time()
print(height(80000, 100000)) # Expected output: 528130401
print("Execution Time:", time.time() - start)
"""
