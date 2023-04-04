class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # Initialize variables to store the number of rows and columns in the grid
        rows = len(grid)
        cols = len(grid[0])
        
        # Initialize variables to store the starting and ending points
        start_row, start_col = 0, 0
        end_row, end_col = 0, 0
        
        # Initialize a variable to store the number of empty squares
        empty_squares = 0
        
        # Iterate through the grid to find the starting and ending points, and the number of empty squares
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    start_row, start_col = row, col
                elif grid[row][col] == 2:
                    end_row, end_col = row, col
                elif grid[row][col] == 0:
                    empty_squares += 1
        
        # Initialize a variable to store the number of unique paths
        paths = 0
        
        # Call the helper function to calculate the number of unique paths
        paths = self.dfs(grid, start_row, start_col, end_row, end_col, empty_squares, paths)
        
        # Return the number of unique paths
        return paths
    
    def dfs(self, grid, start_row, start_col, end_row, end_col, empty_squares, paths):
        # Check if the current position is the ending point
        if start_row == end_row and start_col == end_col:
            # Check if all empty squares have been visited
            if empty_squares == 0:
                # Increment the number of paths
                paths += 1
            return paths
        
        # Mark the current position as visited
        grid[start_row][start_col] = -2
        empty_squares -= 1
        
        # Iterate through the 4 directions
        for row, col in [(start_row+1, start_col), (start_row-1, start_col), (start_row, start_col+1), (start_row, start_col-1)]:
            # Check if the new position is valid
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] >= 0:
                # Call the helper function to explore the new position
                paths = self.dfs(grid, row, col, end_row, end_col, empty_squares, paths)
        
        # Mark the current position as unvisited
        grid[start_row][start_col] = 0
        empty_squares += 1
        
        # Return the number of paths
        return paths
