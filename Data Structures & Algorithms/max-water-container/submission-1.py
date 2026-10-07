class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea,l,r = 0,0,len(heights)-1
        while (l < r):
            maxArea = max(maxArea, (r-l) * min(heights[l],heights[r]))
            if (heights[l] <= heights[r]):
                l+=1
            elif(heights[l] > heights[r]):
                r-=1
        return maxArea
