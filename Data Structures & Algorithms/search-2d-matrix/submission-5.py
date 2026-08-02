class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowno = len(matrix)
        colno = len(matrix[0])
        l = 0
        r = colno - 1

        for i in range(len(matrix)):
            if target >= matrix[i][l] and target <= matrix[i][r]:               
                while l <= r:
                    mid = (l + r) // 2
                    if target > matrix[i][mid]:
                        l  = mid + 1
                    elif target < matrix[i][mid]:
                        r = mid - 1
                    else:
                        return True
        return False 