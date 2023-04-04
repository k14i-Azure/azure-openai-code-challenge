class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        total = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    total += 1
        self.ans = 0
        def dfs(i, j, remain):
            if not (0 <= i < m and 0 <= j < n and grid[i][j] >= 0):
                return
            if grid[i][j] == 2:
                self.ans += remain == 0
                return
            grid[i][j] = -2
            dfs(i + 1, j, remain - 1)
            dfs(i - 1, j, remain - 1)
            dfs(i, j + 1, remain - 1)
            dfs(i, j - 1, remain - 1)
            grid[i][j] = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j, total - 1)
        return self.ans
