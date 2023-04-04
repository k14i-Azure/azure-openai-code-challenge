class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # Get the number of rows and columns
        rows = len(grid)
        cols = len(grid[0])
        
        # Get the starting and ending points
        start_row, start_col = 0, 0
        end_row, end_col = 0, 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    start_row, start_col = i, j
                elif grid[i][j] == 2:
                    end_row, end_col = i, j
        
        # Count the number of empty squares
        empty_squares = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    empty_squares += 1
        
        # Initialize the number of paths
        paths = 0
        
        # Define a helper function to count the number of paths
        def count_paths(row, col, empty_squares):
            # If the current cell is out of bounds or is an obstacle, return 0
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == -1:
                return 0
            
            # If the current cell is the ending cell, return 1 if all empty squares are visited
            if row == end_row and col == end_col:
                return 1 if empty_squares == 0 else 0
            
            # Mark the current cell as visited
            grid[row][col] = -1
            empty_squares -= 1
            
            # Count the number of paths
            paths = 0
            paths += count_paths(row + 1, col, empty_squares)
            paths += count_paths(row - 1, col, empty_squares)
            paths += count_paths(row, col + 1, empty_squares)
            paths += count_paths(row, col - 1, empty_squares)
            
            # Unmark the current cell
            grid[row][col] = 0
            empty_squares += 1
            
            return paths
        
        # Call the helper function
        paths = count_paths(start_row, start_col, empty_squares)
        
        return paths
