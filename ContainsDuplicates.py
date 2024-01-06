# Given an integer array nums, return true if any value appears
# at least twice in the array, and return false if every element is
# distinct.

class Solution(object):
    def containsDuplicate(self, nums):
        nums_length = len(nums)
        set_nums = set(nums)
        if nums_length > len(set_nums):
            return True
        return False

nums = [1,2,3,1]
print(Solution().containsDuplicate(nums))        #True
print(Solution().containsDuplicate([1,2,3,4]))   #False
print(Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]))  #True
print(Solution().containsDuplicate([3,3]))  #True
