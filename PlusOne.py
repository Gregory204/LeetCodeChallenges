# You are given a large integer represented as an integer array digits,
# where each digits[i] is the ith digit of the integer. The digits are ordered
# from most significant to least significant in left-to-right order. The large integer
# does not contain any leading 0's.

class Solution(object):
    def plusOne(self, digits):
        string_list = ''.join(map(str, digits)) # 123
        int_string = int(string_list)+1         # 124
        string_int = str(int_string)            # 124 back to string for iteration
        int_list = [int(digit) for digit in string_int]
        return int_list

# map(str, my_list) is used to convert each integer in the list to a string, and
# ''.join(...) concatenates these strings.

bog = Solution()
digits = [1, 2, 3]
print(bog.plusOne(digits)) #Output: 1,2,4
digits = [9, 9, 9 ,9 ,9]
print(bog.plusOne(digits)) #Output: 1,0,0,0,0
