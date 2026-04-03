class Solution:
    def maxArea(self, heights: List[int]) -> int:
        current = 0
        maxArea = 0

        l = 0
        r = len(heights) - 1
    
        while l < r:
            current = min(heights[l], heights[r]) * (r-l)
            maxArea = max(maxArea, current)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return maxArea

