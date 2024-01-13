# Given n non-negative integers representing an elevation map where
# the width of each bar is 1, compute how much water it can trap
# after raining.

# Two Pointer Solution
class Solution(object):
    def trap(self, height):

        if not height:
            return 0
        l = 0
        r = len(height)-1
        maxl = height[l]
        maxr = height[r]
        tot = 0

        while l < r:
            if maxl < maxr:
                l += 1
                maxl = max(maxl, height[l])  # never becomes negative
                tot += maxl - height[l]
            else:
                r -= 1
                maxr = max(maxr, height[r])
                tot += maxr - height[r]
        return tot




height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trap(height))
