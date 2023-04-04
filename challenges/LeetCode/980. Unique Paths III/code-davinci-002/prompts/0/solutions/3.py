class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.res = 0
        self.n = len(grid)
        self.m = len(grid[0])
        self.grid = grid
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == 1:
                    self.start = (i, j)
                elif grid[i][j] == 2:
                    self.end = (i, j)
        self.dfs(self.start[0], self.start[1], 0)
        return self.res
    
    def dfs(self, x, y, step):
        if self.grid[x][y] == -1:
            return
        if (x, y) == self.end:
            if step == self.n * self.m - 1:
                self.res += 1
            return
        self.grid[x][y] = -1
        for i, j in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if 0 <= i < self.n and 0 <= j < self.m:
                self.dfs(i, j, step+1)
        self.grid[x][y] = 0
