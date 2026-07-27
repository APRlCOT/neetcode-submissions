class Solution:
    def trap(self, height: List[int]) -> int:
        # Edge case: If the array is empty, no water can be trapped
        if not height:
            return 0
        
        # Initialize the two pointers at opposite ends of the array
        left = 0
        right = len(height) - 1
        
        # Initialize the maximum boundaries seen so far
        maxLeft = height[left]
        maxRight = height[right]
        
        totalWater = 0
        
        # The engine: keep moving inward until every spot is evaluated
        while left < right:
            
            # The decision-maker: process the side with the shorter boundary
            if maxLeft < maxRight:
                left += 1
                # Update the boundary FIRST (The Invariant)
                maxLeft = max(maxLeft, height[left])
                # Calculate water using the newly updated boundary
                totalWater += maxLeft - height[left]
                
            else:
                right -= 1
                # Update the boundary FIRST (The Invariant)
                maxRight = max(maxRight, height[right])
                # Calculate water using the newly updated boundary
                totalWater += maxRight - height[right]
                
        return totalWater