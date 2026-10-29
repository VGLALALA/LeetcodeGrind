from collections import Counter

class Solution:
    def checkdup(self, d):
        for key, val in d.items():
            if key != "." and val > 1:
                return False
        return True

    def checkbox(self, board):
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                boxlst = []

                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        boxlst.append(board[r][c])

                d = Counter(boxlst)
                if not self.checkdup(d):
                    return False

        return True

    def checkrow(self, board):
        for r in board:
            d = Counter(r)
            if not self.checkdup(d):
                return False

        return True

    def checkcol(self, board):
        for x in range(9):
            collst = [board[r][x] for r in range(9)]
            d = Counter(collst)

            if not self.checkdup(d):
                return False

        return True

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        return (self.checkbox(board)
                and self.checkrow(board)
                and self.checkcol(board))