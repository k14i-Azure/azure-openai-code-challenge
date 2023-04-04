MOD = 998244353

def height(n, m):
    # base cases
    if n == 0:
        return 0
    elif n == 1:
        return m
    elif n == 2:
        return m + 1
    elif n == 3:
        return m + 2
    
    # create a lookup table to store the results
    lookup = [[[0 for k in range(n+1)] for j in range(n+1)] for i in range(n+1)]
    
    # fill the lookup table
    for i in range(n+1):
        for j in range(n+1):
            for k in range(n+1):
                if i == 0 and j == 0 and k == 0:
                    lookup[i][j][k] = 0
                elif i == 0 and j == 0 and k != 0:
                    lookup[i][j][k] = (k * m) % MOD
                elif i == 0 and j != 0 and k == 0:
                    lookup[i][j][k] = (j * (j + 1)) % MOD
                elif i == 0 and j != 0 and k != 0:
                    lookup[i][j][k] = (lookup[i][j-1][k] + lookup[i][j][k-1]) % MOD
                elif i != 0 and j == 0 and k == 0:
                    lookup[i][j][k] = (i * (i + 1)) % MOD
                elif i != 0 and j == 0 and k != 0:
                    lookup[i][j][k] = (lookup[i-1][j][k] + lookup[i][j][k-1]) % MOD
                elif i != 0 and j != 0 and k == 0:
                    lookup[i][j][k] = (lookup[i-1][j][k] + lookup[i][j-1][k]) % MOD
                else:
                    lookup[i][j][k] = (lookup[i-1][j][k] + lookup[i][j-1][k] + lookup[i][j][k-1]) % MOD
    
    # return the result
    return lookup[n][n][n] % MOD
