class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxHeight,l,r = 0,0,len(heights)-1
        while l < r:
            temp = min(heights[l],heights[r]) * (r-l)
            print(str(heights[l])+"*"+str(heights[r])+"="+str(temp))
            if temp > maxHeight:
                maxHeight = temp
            if heights[l] < heights[r]:
                l+=1
            elif heights[l] >= heights[r]:
                r-=1
        return maxHeight