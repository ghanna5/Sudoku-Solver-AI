from sudokutools import valid
from collections import OrderedDict

# class State:
#     def __init__(self, board, cost):
#         self.board = board
#         self.cost = cost
#         self.hcost = self.calculate_hcost()
#         self.total = self.cost + self.hcost

#     def calculate_hcost(self):
#         # number of empty cells counted
#         return sum(row.count(0) for row in self.board)

#     def goal(self):
#         # If cells are not empty, then goal reached
#         return self.hcost == 0

# def calculate_hcost(cell_cand):
#     return sum(len(candidates) for candidates in cell_cand.values())


def empty_cells_cand(board):

    # Dictionary for empty cells
    cell_cand = {}
    #path_cost = 0

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                candidates = []

                for num in range(1, 10):
                    if valid(board, (i, j), num):
                        candidates.append(num)

                if candidates:
                    #Setting position of empty cell to key and values to candidates
                    cell_cand[(i, j)] = candidates

    #path_cost = len(cell_cand)
    return cell_cand

def update_candidates(cell_cand, board, pos, num, add=True):

    if add:
        # Remove the cell from the dictionary since it's now filled
        if pos in cell_cand:
            del cell_cand[pos]
    else:
        # Recalculate candidates for the cell being reset
        candidates = []
        for n in range(1, 10):
            if valid(board, pos, n):
                candidates.append(n)
        if candidates:
            cell_cand[pos] = candidates

    # Update candidates for other cells in the same row, column, and box
    row, col = pos
    for i in range(9):
        # Update row
        if (row, i) in cell_cand and num in cell_cand[(row, i)]:
            cell_cand[(row, i)].remove(num)
        # Update column
        if (i, col) in cell_cand and num in cell_cand[(i, col)]:
            cell_cand[(i, col)].remove(num)

    start_i, start_j = row - row % 3, col - col % 3
    for i in range(3):
        for j in range(3):
            cell = (start_i + i, start_j + j)
            if cell in cell_cand and num in cell_cand[cell]:
                cell_cand[cell].remove(num)