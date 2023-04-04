# Solution: (Backtracking Approach)
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n, empty = len(grid), len(grid[0]), 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x, y = (i, j)
                elif grid[i][j] == 0:
                    empty += 1
        self.res = 0
        def backtrack(x, y, empty):
            if not (0 <= x < m and 0 <= y < n and grid[x][y] >= 0): return
            if grid[x][y] == 2:
                self.res += empty == 0
                return
            grid[x][y] = -2
            backtrack(x + 1, y, empty - 1)
            backtrack(x - 1, y, empty - 1)
            backtrack(x, y + 1, empty - 1)
            backtrack(x, y - 1, empty - 1)
            grid[x][y] = 0
        backtrack(x, y, empty)
        return self.res
''' Complexity analysis:
Time: O(m*n*2^(m*n)), as we need to traverse the whole matrix once and at each cell we have 2 choices, either we can go to next cell or not.
Space: O(m*n), since we need to store the cells in the recursion stack. '''
