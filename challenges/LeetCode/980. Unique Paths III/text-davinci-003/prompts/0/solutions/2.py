class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # Store the number of rows and columns in the grid
        rows = len(grid)
        cols = len(grid[0])
        
        # Store the starting and ending coordinates
        start_row, start_col = 0, 0
        end_row, end_col = 0, 0
        
        # Count the number of empty squares
        empty_squares = 0
        
        # Iterate through the grid to find the starting and ending coordinates
        # and count the number of empty squares
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    start_row, start_col = row, col
                elif grid[row][col] == 2:
                    end_row, end_col = row, col
                elif grid[row][col] == 0:
                    empty_squares += 1
        
        # Create a visited matrix to store the visited coordinates
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        
        # Call the helper function to find the number of unique paths
        return self.uniquePaths(grid, start_row, start_col, end_row, end_col, empty_squares, visited)
    
    def uniquePaths(self, grid, start_row, start_col, end_row, end_col, empty_squares, visited):
        # Base case: If the starting and ending coordinates are the same,
        # check if all the empty squares have been visited
        if start_row == end_row and start_col == end_col:
            if empty_squares == 0:
                return 1
            else:
                return 0
        
        # Mark the current coordinates as visited
        visited[start_row][start_col] = True
        
        # Initialize the number of unique paths
        paths = 0
        
        # Check if the current coordinates are valid
        if 0 <= start_row < len(grid) and 0 <= start_col < len(grid[0]) and grid[start_row][start_col] >= 0 and not visited[start_row][start_col]:
            # Check the adjacent coordinates
            for row, col in [(start_row + 1, start_col), (start_row - 1, start_col), (start_row, start_col + 1), (start_row, start_col - 1)]:
                # If the adjacent coordinates are empty squares, 
                # decrement the number of empty squares and 
                # call the helper function to find the number of unique paths
                if grid[row][col] == 0:
                    empty_squares -= 1
                    paths += self.uniquePaths(grid, row, col, end_row, end_col, empty_squares, visited)
                    empty_squares += 1
        
        # Mark the current coordinates as unvisited
        visited[start_row][start_col] = False
        
        # Return the number of unique paths
        return paths
