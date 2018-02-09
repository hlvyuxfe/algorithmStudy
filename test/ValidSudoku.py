#Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
#The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
#A partially filled sudoku which is valid.
#Note:
#A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            dic = {}
            for i in row:
                if i !='.':
                    if i in dic:
                        return False
                    else:
                        dic[i]=1
        for col in range(9):
            dic = {}
            for row in range(9):
                if board[row][col]!='.':
                    if board[row][col] in dic:
                        return False
                    else:
                        dic[board[row][col]]=1
        for row in [0,3,6]:
            for col in [0,3,6]:
                dic = {}
                for row1 in [0,1,2]:
                    for col1 in [0,1,2]:
                        if board[row+row1][col+col1]!='.':
                            if board[row+row1][col+col1] in dic:
                                return False
                            else:
                                dic[board[row+row1][col+col1]]=1
        return True