class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.res = 0
        self.empty = 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    x, y = (i, j)
                elif grid[i][j] == 0:
                    self.empty += 1
        
        def dfs(x, y, empty):
            if not (0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] >= 0):
                return
            if grid[x][y] == 2:
                self.res += empty == 0
                return
            grid[x][y] = -2
            dfs(x + 1, y, empty - 1)
            dfs(x - 1, y, empty - 1)
            dfs(x, y + 1, empty - 1)
            dfs(x, y - 1, empty - 1)
            grid[x][y] = 0
        
        dfs(x, y, self.empty)
        return self.res
