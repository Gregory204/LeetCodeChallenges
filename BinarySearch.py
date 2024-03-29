class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r -= 1
            else:  # if nums[mid] < target
                l += 1
        return -1

nums = [-1,0,3,5,9,12]
target = 9
print(Solution().search(nums, target))
# Output 4
# looking for index number where target is located using binary search
