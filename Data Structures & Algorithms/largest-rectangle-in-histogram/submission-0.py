class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h: #if top of the stack has height greater than the the current height
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index)) #this i - index part can calcualate maxArea for multiple histo if the height was big enough
                start = index

            stack.append((start, h))


        #and here we check if there are some stacks of increasing height and what the max area can be
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea

        
        