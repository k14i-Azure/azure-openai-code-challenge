def loopover(mixed_up_board, solved_board):
    # Size of the board
    N, M = len(mixed_up_board), len(mixed_up_board[0])
    # Dictionary to store the positions of the solved board
    solved_pos = {solved_board[i][j]: (i, j) for i in range(N) for j in range(M)}
    # List to store the moves
    moves = []
    # Dictionary to store the number of times each row and column has been moved
    moves_count = {i: 0 for i in range(N+M)}
    # Dictionary to store the position of each piece in the mixed up board
    mixed_pos = {mixed_up_board[i][j]: (i, j) for i in range(N) for j in range(M)}
    # Loop over the pieces of the solved board
    for i in range(N):
        for j in range(M):
            # If the piece is not in the correct position
            if mixed_up_board[i][j] != solved_board[i][j]:
                # Get the position of the piece in the solved board
                si, sj = solved_pos[mixed_up_board[i][j]]
                # If the piece is in the same row
                if i == si:
                    # Move the row up or down
                    if j < sj:
                        moves.append("R" + str(i))
                        moves_count[i] += 1
                    else:
                        moves.append("L" + str(i))
                        moves_count[i] -= 1
                # If the piece is in the same column
                elif j == sj:
                    # Move the column left or right
                    if i < si:
                        moves.append("D" + str(j))
                        moves_count[N+j] += 1
                    else:
                        moves.append("U" + str(j))
                        moves_count[N+j] -= 1
                # If the piece is not in the same row or column
                else:
                    # Move the row and column to the correct position
                    while i != si:
                        if i < si:
                            moves.append("D" + str(j))
                            moves_count[N+j] += 1
                            i += 1
                        else:
                            moves.append("U" + str(j))
                            moves_count[N+j] -= 1
                            i -= 1
                    while j != sj:
                        if j < sj:
                            moves.append("R" + str(i))
                            moves_count[i] += 1
                            j += 1
                        else:
                            moves.append("L" + str(i))
                            moves_count[i] -= 1
                            j -= 1
    # Check if the mixed up board is solved
    if mixed_up_board == solved_board:
        return moves
    # Check if the board is unsolvable
    if any(moves_count[i] % 2 != 0 for i in range(N+M)):
        return None
    # Return the list of moves
    return moves