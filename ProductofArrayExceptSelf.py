# Given an integer array nums, return an array answer such that answer[i]
# is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using
# the division operation.

nums = [1, 2, 3, 4]
answer = [1] * (len(nums))

r = len(nums)
prefix = 1
for i in range(r):
    answer[i] = prefix
    prefix *= nums[i]

postfix = 1
for i in range(r - 1, -1, -1):  # 3, 2, 1, 0
    answer[i] *= postfix
    postfix *= nums[i]

# nums = [1, 2, 3, 4]
# print(Solution().productExceptSelf(nums))
# Output = [24, 12, 8, 6]

'''
class Solution(object):
    def productExceptSelf(self, nums):
        answer = [1] * (len(nums))

        # nums = [1, 2, 3, 4]
        # answer = [1, 1, 1, 1]
        r = len(nums)
        prefix = 1
        for i in range(r):  # 0, 1, 2, 3
            answer[i] = prefix  # 1, prefix = 1 | 1, prefix = 1, | 1, prefix = 2, answer[2] = 2 | 1, prefix = 6, answer[3] = 6
            prefix *= nums[i]  # prefix *= 1 | prefix *= 2 | prefix *= 3
        # answer = [1,1,2,6]
        postfix = 1
        for i in range(r -1, -1, -1):  # 3, 2, 1, 0
            answer[i] *= postfix  # answer[3] = 6, postfix = 1, answer[3] = 6 | answer[2] = 2, postfix = 4, answer[2] = 8 |
                                  # answer[1] = 1, postfix = 12, answer[1] = 12 | answer[0] = 1, postfix = 24, answer[0] = 24 |
            postfix *= nums[i]  # 1 *= 4 = 4, 4 *= 3 = 12, 12 *= 2 = 24
        # Output = [24, 12, 8, 6]
        return answer
'''
