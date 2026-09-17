class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows-1
        row = -1
        while right >= left:
            mid = (right+left)//2
            if target >= matrix[mid][0] and target <= matrix[mid][cols-1]:
                row = mid
                break
            elif target > matrix[mid][0] and target > matrix[mid][cols-1]:
                left = mid + 1
            elif target < matrix[mid][0] and target < matrix[mid][cols-1]:
                right = mid-1
        if row == -1:
            return False
        
        left = 0
        right = cols-1

        while right >= left:
            mid = (right+left)//2
            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                right = mid-1
            else:
                left = mid+1
        return False