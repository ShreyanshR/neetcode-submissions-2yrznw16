class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        area = 0

        while l < r:
            width = r - l
            hL, hR = heights[l], heights[r]
            area = max(area,width * min(hL, hR))
            if min(hL,hR) == hL:
                l += 1
            else: 
                r -= 1

        return area

            
            
