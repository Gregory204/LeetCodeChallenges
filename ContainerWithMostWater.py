'''
Two Pointer
class Solution(object):
    def twoSum(self, numbers, target):
        l = 0
        r = len(numbers)-1

        while l <= r:
            m = (numbers[l] + numbers[r])
            if m == target:
                return [l+1, r+1]
            elif m > target:
                r -= 1
            elif m < target:
                l += 1
'''
# You are given an integer array height of length n. There are n
# vertical lines drawn such that the two endpoints of the ith line
# are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such
# that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

class Solution(object):
    def maxArea(self, height):
        max_water = 0

        l = 0
        r = len(height)-1
        while l < r:
            d = r - l  # distance of elements
            water = min(height[l], height[r]) * d  # min l or r
            max_water = max(water, max_water)  # continuously update max
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return max_water

height = [2,3,4,5,18,17,6]
print(Solution().maxArea(height))
