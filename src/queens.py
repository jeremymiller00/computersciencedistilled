""" 
Note: algorithm exceeds Python recursion limit
Increasing recursion limit results in segfault
"""

import sys

class Board:
    """
    Convert position in list 0-63 to position by:
    p // 8 = X
    p % 8 = y


    """
    def __init__(self):
        super().__init__()
        self.attacked_positions = [0 for x in range(64)]
        self.unattacked_positions = [1 for x in range(64)]
        self.queens = [0 for x in range(64)]
        self.boarder_values = list(range(0,8))
        self.boarder_values.extend([x+56 for x in self.boarder_values])
        self.boarder_values.extend([x*8 for x in list(range(0,8))])
        self.boarder_values.extend([ (x*8)+7 for x in list(range(0,8))])
        self.boarder_values = set(self.boarder_values)
        
        # self.queens = []
        # self.positions = [(x,y) for x in range(8) for y in range(8)]

    def place_queen(self, position):
        if self.queens[position] == 1:
            return "Queen already present; no action taken."
        self.queens[position] = 1
        for pos in self._attackable_pos(position):
            self.attacked_positions[pos] = 1
        self.unattacked_positions = [1 if x==0 else 0 for x in self.attacked_positions]

    def remove_queen(self, position):
        if self.queens[position] == 0:
            return "No queen to remove; no action taken."
        self.queens[position] = 0
        self.attacked_positions = [0 for x in range(64)]
        for i, q in enumerate(self.queens):
            if q == 1:
                for pos in self._attackable_pos(i):
                    self.attacked_positions[pos] = 1
        self.unattacked_positions = [1 if x==0 else 0 for x in self.attacked_positions]

    def has_8_queens(self):
        return sum(self.queens) == 8


    def _attackable_pos(self, position):
        """Positions on the board that are attackable by a queen from a given position

        Args:
            position (int):

        Returns:
            [set]:
        """
        row = position // 8
        row_basis = list(range(0,8))
        row_values = set([ (row*8) + x for x in row_basis ])
        col_values = set()
        a = position
        while a >= 0:
            col_values.add(a)
            a -= 8
        b = position
        while b <= 63:
            col_values.add(b)
            b += 8
        diag_values = set()
        c = position
        while c >= 0:
            diag_values.add(c)
            c -= 9
            if c in self.boarder_values:
                diag_values.add(c)
                break
            else:
                continue
        d = position
        while d <= 63:
            diag_values.add(d)
            d += 9
            if d in self.boarder_values:
                diag_values.add(d)
                break
            else:
                continue
        e = position
        while e >= 0:
            diag_values.add(e)
            e -= 7
            if e in self.boarder_values:
                diag_values.add(e)
                break
            else:
                continue
        f = position
        while f <= 63:
            diag_values.add(f)
            f += 7
            if f in self.boarder_values:
                diag_values.add(f)
                break
            else:
                continue
        return row_values.union(col_values).union(diag_values)
        # return row_values, col_values, diag_values


def queens(board):
    """Algorithm using recursion and backtracking to find positions
    Must place 8 queens on the 8X8 board, where none can attack each other

    Args:
        board (Board): blank chess board with queens

    Returns:
        [Board]: chess board with 8 safe queens
    """
    if board.has_8_queens():
        return board
    for pos in board.unattacked_positions:
        board.place_queen(pos)
        solution = queens(board)
        if solution:
            return solution
        board.remove_queen(pos)
    return False


def main():
    board = Board()
    solution = queens(board)
    print("Positions for 8 safe queens: ")
    print(solution.queens)
    return solution


#########################

if __name__ == '__main__':
    sys.setrecursionlimit(30000)
    solution = main()