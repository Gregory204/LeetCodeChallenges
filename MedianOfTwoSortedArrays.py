# Given two sorted arrays nums1 and nums2 of size m and n respectively,
# return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).
# Brute Force Method

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums3 = nums1 + nums2
        nums3.sort()

        bog = len(nums3)
        if bog % 2 == 1:  # if odd
            return float(nums3[bog] // 2)
        else:
            m1 = nums3[bog // 2 -1]  # 2
            m2 = nums3[bog // 2]     # 3
            print(m1, m2)
            return float(m1 + m2) / 2


nums1 = [1,2]
nums2 = [3,4]
print(Solution().findMedianSortedArrays(nums1, nums2))
# Output 2.5
