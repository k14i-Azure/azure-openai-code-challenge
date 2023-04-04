class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # Get the starting and ending coordinates
        start_x, start_y = 0, 0
        end_x, end_y = 0, 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    start_x, start_y = i, j
                elif grid[i][j] == 2:
                    end_x, end_y = i, j
        
        # Initialize the number of paths to 0
        num_paths = 0
        
        # Define a helper function to recursively traverse the grid
        def traverse(x, y, num_empty):
            # Check if the current coordinates are valid
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == -1:
                return
            
            # Check if the current coordinates are the end point
            if x == end_x and y == end_y:
                # Check if all empty squares have been visited
                if num_empty == 0:
                    nonlocal num_paths
                    num_paths += 1
                return
            
            # Mark the current square as visited
            temp = grid[x][y]
            grid[x][y] = -1
            
            # Recursively traverse the grid
            traverse(x + 1, y, num_empty - 1)
            traverse(x - 1, y, num_empty - 1)
            traverse(x, y + 1, num_empty - 1)
            traverse(x, y - 1, num_empty - 1)
            
            # Reset the current square
            grid[x][y] = temp
        
        # Count the number of empty squares
        num_empty = 0
        for row in grid:
            for square in row:
                if square == 0:
                    num_empty += 1
        
        # Start traversing the grid from the starting point
        traverse(start_x, start_y, num_empty)
        
        # Return the number of paths
        return num_paths
