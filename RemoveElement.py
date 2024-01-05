# Given an integer array nums and an integer val, remove all
# occurrences of val in nums in-place. The order of the elements
# may be changed. Then return the number of elements in nums which
# are not equal to val.

class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else: # if nums[i] != val
                i += 1
        return len(nums)

nums = [3, 2, 2, 3]
val = 3
bog = Solution()
print(bog.removeElement(nums, val))
print(bog.removeElement([0,1,2,2,3,0,4,2], 2))

# Yes, the line nums[:] = [x for x in nums if x != val] modifies
# the original list nums in-place. The [:] syntax is used to perform
# a slice assignment, and it replaces the contents of the entire list
# with the result of the list comprehension.
#BEST WAY MY OPINION
nums[:] = [x for x in nums if x != val]
print(nums)
