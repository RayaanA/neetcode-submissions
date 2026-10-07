class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        row = len(matrix)
        column = len(matrix[0])
        l = 0
        r = row*column-1
        while l <= r:
            mid = (r+l) // 2
            midc,midr = divmod(mid,column)
            if matrix[midc][midr] == target:
                return True
            elif matrix[midc][midr] > target:
                r = mid-1
            else:
                l = mid+1
        return False