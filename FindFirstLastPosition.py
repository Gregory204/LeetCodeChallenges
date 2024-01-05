# Given an array of integers nums sorted in non-decreasing order, find the starting
# and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

class Solution(object):
    def searchRange(self, nums, target):
        left = 0
        right = len(nums)-1
        my_list = []
        if target not in nums:
            return [-1,-1]

        while left <= right:
            if nums[left] == target:
                my_list.append(left)
                left += 1
            elif nums[right] == target:
                my_list.append(right)
                right -= 1
            else:
                left += 1
                right -= 1
        if len(set(my_list)) == 1:
            return [my_list[0], my_list[0]]
        if len(my_list) > 2:
            my_list = [min(my_list), max(my_list)]

        my_list.sort()
        return my_list
    
nums = [3,3,3]
target = 3

print(Solution().searchRange(nums, target))
#Output would be [0,2]

'''
This Problem was one of the hardest ive done since its a medium difficulty but it really tested my brain and really boosted my 
confidence in my coding skills. 
'''
