def loopover(mixed_up_board: List[List[str]], solved_board: List[List[str]]) -> Optional[List[str]]:
    """
    Returns a list of moves to transform the mixedUpBoard grid to the solvedBoard grid.
    """
    # Check if the board is solvable
    if not is_solvable(mixed_up_board, solved_board):
        return None
    
    # Create a visited set to store visited boards
    visited = set()
    
    # Create a queue to store the current board and its associated moves
    queue = [(mixed_up_board, [])]
    
    # Loop until the queue is empty
    while queue:
        # Get the current board and its associated moves
        board, moves = queue.pop(0)
        
        # Check if the board is the solved board
        if board == solved_board:
            return moves
        
        # Check if the board has been visited
        if board not in visited:
            # Add the board to the visited set
            visited.add(board)
            
            # Generate the possible moves
            for move in generate_moves(board):
                # Create a new board based on the move
                new_board = apply_move(board, move)
                
                # Add the new board and its associated moves to the queue
                queue.append((new_board, moves + [move]))
                
    # Return None if the board is not solvable
    return None

def is_solvable(mixed_up_board: List[List[str]], solved_board: List[List[str]]) -> bool:
    """
    Checks if the board is solvable.
    """
    # Get the number of rows and columns
    rows, cols = len(mixed_up_board), len(mixed_up_board[0])
    
    # Get the number of inversions in the mixed up board
    inv_mixed_up = get_inversions(mixed_up_board, rows, cols)
    
    # Get the number of inversions in the solved board
    inv_solved = get_inversions(solved_board, rows, cols)
    
    # Check if the number of inversions is even
    if (inv_mixed_up + inv_solved) % 2 == 0:
        return True
    else:
        return False

def get_inversions(board: List[List[str]], rows: int, cols: int) -> int:
    """
    Returns the number of inversions in the board.
    """
    # Initialize the number of inversions
    inversions = 0
    
    # Loop through the board
    for i in range(rows):
        for j in range(cols):
            # Get the current element
            element = board[i][j]
            
            # Loop through the remaining elements
            for x in range(i, rows):
                for y in range(j + 1, cols):
                    # Get the remaining element
                    remaining_element = board[x][y]
                    
                    # Check if the element is greater than the remaining element
                    if element > remaining_element:
                        # Increment the number of inversions
                        inversions += 1
                        
    return inversions

def generate_moves(board: List[List[str]]) -> List[str]:
    """
    Generates the possible moves.
    """
    # Get the number of rows and columns
    rows, cols = len(board), len(board[0])
    
    # Initialize the list of moves
    moves = []
    
    # Generate the possible row moves
    for i in range(rows):
        moves.append(f'L{i}')
        moves.append(f'R{i}')
        
    # Generate the possible column moves
    for j in range(cols):
        moves.append(f'U{j}')
        moves.append(f'D{j}')
        
    return moves

def apply_move(board: List[List[str]], move: str) -> List[List[str]]:
    """
    Applies the move to the board.
    """
    # Get the number of rows and columns
    rows, cols = len(board), len(board[0])
    
    # Create a new board
    new_board = [row[:] for row in board]
    
    # Get the direction and index of the move
    direction, index = move[0], int(move[1])
    
    # Check the direction of the move
    if direction == 'L':
        # Move the row left
        new_board[index] = board[index][-1:] + board[index][:-1]
    elif direction == 'R':
        # Move the row right
        new_board[index] = board[index][1:] + board[index][:1]
    elif direction == 'U':
        # Move the column up
        for i in range(rows):
            new_board[i][index] = board[(i - 1) % rows][index]
    elif direction == 'D':
        # Move the column down
        for i in range(rows):
            new_board[i][index] = board[(i + 1) % rows][index]
            
    return new_board
