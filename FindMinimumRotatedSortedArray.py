# Suppose an array of length n sorted in ascending order is
# rotated between 1 and n times. For example, the array nums =
# [0,1,2,4,5,6,7] might become:
# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1
# time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements,
# return the minimum element of this array.
# You must write an algorithm that runs in O(log n) time.

'''
Original Answer:
class Solution(object):
    def findMin(self, nums):
        return min(nums)
'''


class Solution(object):
    def findMin(self, nums):
       l, r = 0, len(nums)-1

       while l < r:
        m = l + (r - l) // 2

        if nums[m] > nums[r]:
            l = m + 1
        else:  # nums[m] < nums[r]z
            r = m

        return nums[l]

nums = [4,5,6,7,0,1,2]
print(Solution().findMin(nums))
# Output = 0
