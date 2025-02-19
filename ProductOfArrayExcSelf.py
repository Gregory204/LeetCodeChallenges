"""
Products of Array Except Self
Given an integer array nums, return an array output where output[i] 
is the product of all the elements of nums except nums[i]
"""

# NOT OPTIMAL (O (n^2))
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            holder = 1
            for j in range(len(nums)):
                if j != i:
                   holder *= nums[j]
            res.append(holder)
        
        return res
