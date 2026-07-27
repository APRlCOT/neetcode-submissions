class Solution:
    def trap(self, height: List[int]) -> int:
        #The trapping rainwater problem is a two pointer problem
        #It utilises a check of the left height and right height 
        #We need time complexity of O(n)
        #We need space complexity of O(1)
        if not height:
            return 0
        #set the pointers at either end.
        left, right = 0, len(height)-1
        #Keep a tally of the height we have seen which makes it easier to compare down the line.
        max_left, max_right = 0, 0
        #also keep a tally of the bodies of water as our pointers move inward.
        water = 0
        #we start out indefinite iteration when our left peak < right peak and the termination only occurs when they meet in the middle so we leave the iteration when left == right.
        while left < right:
            if height[left] < height[right]:
                #The bottleneck is on the LEFT
                #we also need to check if this new left height is our new max left
                if height[left] >= max_left:
                    max_left = height[left] #here we are now updating our new max left
                else:
                    #if the max left does not get replaced this tells us that bodies of water are present above the current height in our list.
                    #we should now calculate the bodies of water above.
                    water += max_left - height[left]
                    #now since we have calculated the water above, we should move our pointer one space inward.
                left += 1
            else:
                #the bottleneck is on the RIGHT
                #this also tells us to check if the current right is our new max 
                if height[right] > max_right:
                    max_right = height[right]
                else:
                    water += max_right - height[right]
                right -= 1
        return water