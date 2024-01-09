'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to
be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the
digits 1-9 without repetition.

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.

'''
# First check rows
# Second check columns
# Third check 3 x 3 to make sure none have repetition

class Solution(object):
    def isValidSudoku(self, board):
        row_safe = []
        col_safe = []
        box_safe = []

        # Found rows if it has duplicates
        for row in range(len(board)):  # 0
            for col in range(len(board[row])):  # row 0. ["5","3",".",".","7",".",".",".","."]
                if board[row][col].isdigit():
                    row_safe.append(board[row][col])
                    if row_safe.count(board[row][col]) > 1:
                        return False
            row_safe = []
        # Found cols if it has duplicates
        for col in range(len(board)):  # 0
            for row in range(len(board[col])):  # col 0. [5,6,8,4,7]
                if board[row][col].isdigit():
                    col_safe.append(board[row][col])
                    if col_safe.count(board[row][col]) > 1:
                        return False
            col_safe = []

        # Third check 3 x 3 to make sure none have repetition
        for box_row in range(0, len(board), 3):  # jumps to 3 after first iteration
            for box_col in range(0, len(board), 3):  # len(board) == 9
                for row in range(box_row, box_row + 3):  # row 0, 1, 2 | 3, 4, 5 | 6, 7, 8
                    for col in range(box_col, box_col + 3):  # col 0, 1, 2 | 3, 4, 5 | 6, 7, 8
                        if board[row][col].isdigit():
                            box_safe.append(board[row][col])
                            print(box_safe)
                            if box_safe.count(board[row][col]) > 1:
                                return False
                box_safe = []

        return True

board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

print(Solution().isValidSudoku(board))
'''
# O(n^2)
