class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                temp = board[i][j]
                
                if temp == ".":
                    continue
                
                # Check row
                if temp in rows[i]:
                    return False
                
                # Check column
                if temp in columns[j]:
                    return False
                
                # Check box
                box_index = (i // 3) * 3 + (j // 3)
                if temp in boxes[box_index]:
                    return False
                
                # Add to row, column, and box
                rows[i].add(temp)
                columns[j].add(temp)
                boxes[box_index].add(temp)
        
        return True
