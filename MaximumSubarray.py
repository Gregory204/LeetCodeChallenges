# Given an integer array nums, find the subarray with the largest sum,
# and return its sum.

class Solution(object):
    def maxSubArray(self, nums):
        current_sum = 0
        max_sum = -100000000 # Initialize maxSum to a very small value
        for num in nums:
            current_sum += num # Add the current number to the current sum

            if (current_sum > max_sum):
                max_sum = current_sum # Update maxSum if the current sum becomes larger

            if (current_sum < 0):
                current_sum = 0  # Reset the current sum to 0 if it becomes negative

        return max_sum


nums = [-2,1,-3,4,-1,2,1,-5,4]
bog = Solution()
print(bog.maxSubArray(nums))
# Output: 6
print(bog.maxSubArray([1]))
# Output: 1
print(bog.maxSubArray([5,4,-1,7,8]))
# Output: 23
print(bog.maxSubArray([-2,1]))
# Output: 1
print(bog.maxSubArray([1,2]))
# Output: 3
