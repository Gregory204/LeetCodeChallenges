#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

#Notice that the solution set must not contain duplicate triplets.

class Solution(object):
    def threeSum(self, nums):
        fin = []
        nums.sort()
        # [-4, -1, -1, 0, 1, 2]
        for i, n in enumerate(nums):
            # setting n == nums[i-1] which is the first element of the array
            if i > 0 and n == nums[i-1]:
                continue

            l = i+1
            r = len(nums)-1
            while l < r:
                tot = n + nums[l] + nums[r]
                if tot > 0:  # value to big move right to left
                    r -= 1
                elif tot < 0:  # value to small move left to right
                    l += 1
                else:  # Total == 0
                    fin.append([n, nums[l], nums[r]])
                    l += 1  # increase left to keep moving. along with n to increase
                    while l < r and nums[l] == nums[l - 1]:  # if nums is the same as previous
                        l += 1  # continue increasing l till its not the same as previous
        return fin


nums = [-1,0,1,2,-1,-4]
print(Solution().threeSum(nums))
# Output: [[-1, -1, 2], [-1, 0, 1]]
