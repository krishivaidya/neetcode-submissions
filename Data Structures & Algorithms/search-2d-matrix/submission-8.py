class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        trav = float("inf")

        leftrow = 0 
        rightrow = rows - 1
        while leftrow <= rightrow:
            midrow = leftrow + (rightrow - leftrow) // 2
            if target >= matrix[midrow][0] and target <= matrix[midrow][cols - 1]:
                trav = midrow
                break
                
            elif target < matrix[midrow][0]:
                rightrow = midrow - 1

            else:
                leftrow = midrow + 1

        if trav == float("inf"):
            return False

        l = 0
        r = cols - 1
        while l <= r:
            mid = l + (r - l)//2

            if target == matrix[trav][mid]:
                return True 

            elif target > matrix[trav][mid]:
                l = mid + 1

            else:
                r = mid - 1

        return False



            
        