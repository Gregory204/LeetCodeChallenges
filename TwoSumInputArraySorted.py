# Two Pointer Solution
class Solution(object):
    def twoSum(self, numbers, target):
        l = 0
        r = len(numbers)-1

        while l <= r:
            m = (numbers[l] + numbers[r])
            if m == target:
                return [l+1, r+1]
            elif m > target:
                r -= 1
            elif m < target:
                l += 1

numbers = [2,3,4]
target = 6
print(Solution().twoSum(numbers, target))
