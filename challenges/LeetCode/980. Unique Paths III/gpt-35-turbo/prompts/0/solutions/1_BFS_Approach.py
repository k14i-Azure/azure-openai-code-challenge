# Solution: (BFS Approach)
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n, empty = len(grid), len(grid[0]), 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x, y = (i, j)
                elif grid[i][j] == 0:
                    empty += 1
        q, res = [(x, y, empty)], 0
        for x, y, empty in q:
            if grid[x][y] == 2 and empty == 0:
                res += 1
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= x + dx < m and 0 <= y + dy < n and grid[x + dx][y + dy] % 2 == 0:
                    grid[x + dx][y + dy] -= 1
                    q.append((x + dx, y + dy, empty - 1))
        return res
''' Complexity analysis:
Time: O(m*n*2^(m*n)), as we need to traverse the whole matrix once and at each cell we have 2 choices, either we can go to next cell or not.
Space: O(m*n), since we need to store the cells in the queue. '''
