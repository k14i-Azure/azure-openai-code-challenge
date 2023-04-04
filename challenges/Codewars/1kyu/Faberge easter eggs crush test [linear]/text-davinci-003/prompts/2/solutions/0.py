MOD = 998244353

def height(n, m):
    # base cases
    if n == 0 or m == 0:
        return 0
    if n == 1 or m == 1:
        return m
    
    # pre-calculate squares
    squares = [i*i for i in range(1, int(n**0.5)+1)]
    
    # dp array
    dp = [[0]*(m+1) for _ in range(n+1)]
    
    # fill the dp array
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i in squares:
                dp[i][j] = j
            else:
                for k in range(1, int(i**0.5)+1):
                    dp[i][j] = (dp[i][j] + dp[i-k*k][j]) % MOD
    return dp[n][m]
