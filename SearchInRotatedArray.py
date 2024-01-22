# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown
# pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k],
# nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target,
# return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.
'''
class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums)-1

        while l <= r:

            if nums[l] != target:
                l += 1
            else:
                return l
            if nums[r] != target:
                r -= 1
            else:
                return r

        if nums[l] != target or nums[r] != target:
            return -1

# Another Solution
class Solution(object):
    def search(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            return(-1)
'''
# Another Solution
class Solution(object):
    def search(self, nums, target):
        try:
            return nums.index(target)
        except Exception:
            return -1

nums = [1]
target = 1
print(Solution().search(nums, target))
# Output: 0
