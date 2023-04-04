def loopover(mixed_up_board: List[List[str]], solved_board: List[List[str]]) -> Optional[List[str]]:
    """
    This function takes two 2D arrays (or lists of lists) of symbols representing the initial (unsolved) and final (solved) grids.
    It returns a list of moves to transform the mixedUpBoard grid to the solvedBoard grid.
    If the configuration is unsolvable, it returns None.
    """
    # Check if the grids are of the same size
    if len(mixed_up_board) != len(solved_board) or len(mixed_up_board[0]) != len(solved_board[0]):
        return None
    
    # Initialize the list of moves
    moves = []
    
    # Iterate through the rows and columns of the board
    for row in range(len(mixed_up_board)):
        for col in range(len(mixed_up_board[0])):
            # Check if the current cell is in the wrong position
            if mixed_up_board[row][col] != solved_board[row][col]:
                # Find the row/column where the current cell should be
                for i in range(len(mixed_up_board)):
                    for j in range(len(mixed_up_board[0])):
                        if mixed_up_board[row][col] == solved_board[i][j]:
                            # Calculate the number of moves needed to move the current cell to the correct position
                            num_moves = abs(row - i) + abs(col - j)
                            # Append the moves to the list
                            if row == i:
                                if col < j:
                                    moves.extend(['R' + str(row)] * num_moves)
                                else:
                                    moves.extend(['L' + str(row)] * num_moves)
                            else:
                                if row < i:
                                    moves.extend(['D' + str(col)] * num_moves)
                                else:
                                    moves.extend(['U' + str(col)] * num_moves)
    
    # Check if the board is solved
    if mixed_up_board == solved_board:
        return moves
    else:
        return None
