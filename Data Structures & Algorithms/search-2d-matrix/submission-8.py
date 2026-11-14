class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i, row in enumerate(matrix): 
            l, r = 0, len(row) - 1
            for c in row: 
                mid = l + ((r - l) // 2)
                if matrix[i][mid] < target: 
                    l = mid + 1
                elif matrix[i][mid] > target: 
                    r = mid - 1
                else: 
                    return True 
        return False

                