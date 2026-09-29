class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxv = 0

        while l < r:
            volume = min(heights[l], heights[r]) * (r - l)
            maxv = max(volume, maxv)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1


        return maxv

        