"""
https://leetcode.com/problems/valid-sudoku/
"""


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # notice, if a row or column or a small sudoku are all ".", it is not a valid Sudoku
        def isValidRow(row):
            s = set()
            for i in range(0, 9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in s:
                    return False
                else:
                    s.add(board[row][i])
            return True

        def isValidColumn(column):
            s = set()
            for i in range(0, 9):
                if board[i][column] == ".":
                    continue
                if board[i][column] in s:
                    return False
                s.add(board[i][column])
            return True

        def isValidSmallSudoku(top):
            s = set()
            for i in range(top[0], top[0] + 3):
                for j in range(top[1], top[1] + 3):
                    if board[i][j] == ".":
                        continue
                    if board[i][j] in s:
                        return False
                    s.add(board[i][j])
            return True

        for i in range(0, 9):
            if not isValidColumn(i):
                return False
            if not isValidRow(i):
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not isValidSmallSudoku((i, j)):
                    return False
        return True


if __name__ == "__main__":
    solution = Solution()
    assert solution.isValidSudoku([[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]) == False
    assert solution.isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]) == True

    assert solution.isValidSudoku([
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]) == False