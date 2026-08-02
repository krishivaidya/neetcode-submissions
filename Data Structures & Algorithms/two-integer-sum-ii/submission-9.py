class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        currentsum = numbers[left] + numbers[right]
        if currentsum == target:
            return [left + 1, right + 1]

        while left < right and currentsum != target:
            if currentsum < target:
                left += 1

            elif currentsum > target:
                right -= 1

            currentsum = numbers[left] + numbers[right]

        return [left + 1, right + 1]

        
          
            


        
        