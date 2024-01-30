class Solution(object):
    def romanToInt(self, s):
        my_dict = {'I': 1, 'V': 5, 'X': 10,
                   'L': 50, 'C': 100, 'D': 500,
                   'M': 1000}
        value = 0
        # already replacing the values of the string so there is no
        # errors when adding up the total
        s = s.replace('IV', 'IIII').replace('IX', 'IIIIV')
        s = s.replace('XL', 'XXXX').replace('XC', 'XXXXL')
        s = s.replace('CD', 'CCCC').replace('CM', 'CCCCD')
        for i in s:
            value += my_dict[i]
            # For example, if i is 'V', then my_dict[i] would evaluate to 5.
        return value


s = 'III'
answer = Solution()
print(answer.romanToInt(s))
#Ouput: 3

'''
Testing Code.
s = 'MCMXCIV'
my_dict = {'I': 1, 'V': 5, 'X': 10,
           'L': 50, 'C': 100, 'D': 500,
           'M': 500}

sum_values = 
print(sum_values)
'''
