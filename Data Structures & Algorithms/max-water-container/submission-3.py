class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''this is a 2 pointers problem we aim for a time complexity of O(n) and space complexity O(1)'''
        if not heights:
            return 0
        #in this problem we find the bottleneck which will be the second to last highest height of a pillar
        #the body of water present is the bottleneck height multiplied by the width

        #here we set up the pointers at either end
        left, right = 0, len(heights)-1
        water = 0

        while left < right:
            current_height = min(heights[left],heights[right])
            current_width = right - left
            water = max(water, current_width*current_height)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return water
        
    
            

            







    
        