from typing import List, Optional

def loopover(mixed_up_board: List[List[str]], solved_board: List[List[str]]) -> Optional[List[str]]:
    if len(mixed_up_board) != len(solved_board) or len(mixed_up_board[0]) != len(solved_board[0]):
        return None
    n = len(mixed_up_board)
    m = len(mixed_up_board[0])
    board = mixed_up_board
    moves = []
    for i in range(n):
        for j in range(m):
            if board[i][j] != solved_board[i][j]:
                for k in range(n):
                    if board[k][j] == solved_board[i][j]:
                        moves.append('D' + str(j))
                        board = move_down(board, j)
                        break
                for k in range(m):
                    if board[i][k] == solved_board[i][j]:
                        moves.append('R' + str(i))
                        board = move_right(board, i)
                        break
    return moves

def move_down(board, j):
    n = len(board)
    m = len(board[0])
    new_board = []
    for i in range(n):
        new_board.append([])
        for k in range(m):
            new_board[i].append(board[(i + 1) % n][k])
    return new_board

def move_right(board, i):
    n = len(board)
    m = len(board[0])
    new_board = []
    for k in range(n):
        new_board.append([])
        for j in range(m):
            new_board[k].append(board[k][(j + 1) % m])
    return new_board
