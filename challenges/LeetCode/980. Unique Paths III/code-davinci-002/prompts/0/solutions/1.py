class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # Get starting position
        # Get number of empty squares
        # DFS on starting position
        #   if number of empty squares == 0 and position == ending position
        #       increment count
        #   else
        #       for each direction
        #           if next position is valid
        #               DFS
        #               backtrack
        # return count
        start = (0, 0)
        empty = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 0:
                    empty += 1
        count = [0]
        self.dfs(grid, start, empty, count)
        return count[0]
    
    def dfs(self, grid, pos, empty, count):
        if empty == 0 and grid[pos[0]][pos[1]] == 2:
            count[0] += 1
        else:
            for d in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                next_pos = (pos[0] + d[0], pos[1] + d[1])
                if self.is_valid(grid, next_pos):
                    grid[next_pos[0]][next_pos[1]] = -1
                    self.dfs(grid, next_pos, empty - 1, count)
                    grid[next_pos[0]][next_pos[1]] = 0
                    
    def is_valid(self, grid, pos):
        return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0]) and grid[pos[0]][pos[1]] >= 0
