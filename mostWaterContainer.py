class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        p2 = len(heights) - 1
        maxArea = 0
        while p1 < p2: 
            if heights[p1] > heights[p2]: 
                currArea = heights[p2] * (p2-p1)
                if(currArea > maxArea):
                    maxArea = currArea
                
                p2 -= 1
            else:
                currArea = heights[p1] * (p2-p1)
                if(currArea > maxArea):
                    maxArea = currArea
                
                p1 += 1
        
        return maxArea

            
        
