class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L, R = 0, len(matrix[0])-1

        rowStore = 0
        for row in range(len(matrix)):
            if matrix[row][0] <= target:
                rowStore = row
            else:
                break
        
        while L <= R:
            mid = (L + R)//2

            if matrix[rowStore][mid] < target:
                L = mid + 1
            elif matrix[rowStore][mid] > target:
                R = mid - 1
            else:
                return True
        
        return False