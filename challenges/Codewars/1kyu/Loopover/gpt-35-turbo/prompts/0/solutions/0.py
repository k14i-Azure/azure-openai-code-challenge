from typing import List, Optional

def loopover(mixed_up_board: List[List[str]], solved_board: List[List[str]]) -> Optional[List[str]]:
    from itertools import product
    from collections import deque
    
    def hash_board(board):
        return ''.join(''.join(row) for row in board)
    
    def unhash_board(board):
        return [list(row) for row in board.split()]
    
    def get_possible_moves(board):
        moves = []
        for i, j in product(range(len(board)), range(len(board[0]))):
            moves.append(f'R{i}{j}')
            moves.append(f'L{i}{j}')
            moves.append(f'U{i}{j}')
            moves.append(f'D{i}{j}')
        return moves
    
    def apply_move(board, move):
        if move[0] == 'R':
            row = int(move[1])
            board[row] = board[row][-1:] + board[row][:-1]
        elif move[0] == 'L':
            row = int(move[1])
            board[row] = board[row][1:] + board[row][:1]
        elif move[0] == 'U':
            col = int(move[1])
            board = [row[:col] + [row[col-1]] + row[col+1:] for row in board]
        elif move[0] == 'D':
            col = int(move[1])
            board = [row[:col+1] + [row[col]] + row[col+2:] for row in board]
        return board
    
    def solve(mixed_up_board, solved_board):
        visited = set()
        q = deque([(mixed_up_board, [])])
        while q:
            board, moves = q.popleft()
            if hash_board(board) == hash_board(solved_board):
                return moves
            if hash_board(board) in visited:
                continue
            visited.add(hash_board(board))
            for move in get_possible_moves(board):
                new_board = apply_move([row[:] for row in board], move)
                q.append((new_board, moves + [move]))
        return None
    
    return solve(mixed_up_board, solved_board)
