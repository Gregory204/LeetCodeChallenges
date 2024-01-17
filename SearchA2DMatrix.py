# You are given an m x n integer matrix [matrix] with the
# following two properties:
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer
# of the previous row. Given an integer target, return true
# if target is in matrix or false otherwise.
# You must write a solution in O(log(m * n)) time complexity.

# FASTER SOLUTION
class Solution(object):
    def searchMatrix(self, matrix, target):
        for row in matrix:
            if target in row:
                return True
        return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
print(Solution().searchMatrix(matrix, target))
#Output: False

'''
Original Solution:
class Solution(object):
    def searchMatrix(self, matrix, target):
        l, r = 0, len(matrix)-1  # r = 2

        while l <= r:
            m = (l + r) // 2
            # matrix[m] = [10,11,16,20]
            if target not in matrix[m]:
                matrix.remove(matrix[m])
            else:
                return True
            r -= 1

        return False
'''
