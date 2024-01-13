# Given an unsorted array of integers nums, return the length of the
# longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
# Time O(n), Mem O(n)
# More efficient solution
class Solution(object):
    def longestConsecutive(self, nums):
        Set_Nums = set(nums)  # {0, 1, 2, 3, 4, 5, 6, 7, 8}
        longest = 0

        for n in nums:  # 0, 3, 7, 2, 5, 8, 4, 6, 0, 1
            if (n - 1) not in Set_Nums:
                # checking for starting value which is 0 in this case
                length = 0
                # finds consecutive integers from starting point 0
                # 0 + 0, = 0 | 0 + 1 = 1 | 0 + 2 = 2 ....
                while (n + length) in Set_Nums:
                    length += 1  # means it is a consecutive integer as length increments
                longest = max(length, longest)
        return longest  # longest == 9

nums = [0,3,7,2,5,8,4,6,0,1]
print(Solution().longestConsecutive(nums))
# Output: 9

"""
Original Solution.

nums = [0,0]

#if nums == [] or len(nums) == 1:
    #return len(nums)
if nums
length = 0
max_length = 0
nums = list(set(nums))
nums.sort()     # [0,1,2]
cons_list = [nums[0]]
pos = 0
for i in range(len(nums)-1):
    if nums[i]+1 == nums[i+1]:
        cons_list.append(nums[i+1])
        length = len(cons_list)
        max_length = max(max_length, length)
        pos += 1
    else:
        length = len(cons_list)
        max_length = max(max_length, length)
        pos = 0
        cons_list = []

print(max_length)


        if len(nums) < 2:
            return max_length
        else:
            cons_list = [nums[i+1]]
"""
