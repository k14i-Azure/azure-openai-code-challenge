# Solution: (DP Approach)
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n, empty = len(grid), len(grid[0]), 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x, y = (i, j)
                elif grid[i][j] == 0:
                    empty += 1
        dp = [[0] * n for _ in range(m)]
        dp[x][y] = 1
        for _ in range(empty):
            cur = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 0:
                        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            if 0 <= i + dx < m and 0 <= j + dy < n and grid[i + dx][j + dy] % 2 == 0:
                                cur[i][j] += dp[i + dx][j + dy]
            dp = cur
        return dp[x][y]
''' Complexity analysis:
Time: O(m*n*2^(m*n)), as we need to traverse the whole matrix once and at each cell we have 2 choices, either we can go to next cell or not.
Space: O(m*n), since we need to store the cells in the dp array. '''
