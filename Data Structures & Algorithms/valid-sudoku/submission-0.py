class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        columns = [set() for i in range(9)]
        squares = [[set() for i in range(3)] for i in range(3)]

        for i in range(9):
            for j in range(9):
                temp = board[i][j]
                if temp == ".":
                    pass
                else:
                    if temp in rows[i] or temp in columns[j] or temp in squares[i//3][j//3]:
                        return False
                    rows[i].add(temp)
                    columns[j].add(temp)
                    squares[i//3][j//3].add(temp)
        return True
