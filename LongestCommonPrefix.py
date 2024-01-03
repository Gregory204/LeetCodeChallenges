#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string ""

class Solution(object):
    def longestCommonPrefix(self, strs):
        if strs == []:
            return ''
        
        prefix = 0
# zip(*strs) operation will essentially group the characters at the same positions together:
# iterates through each group made by the zip(*strs)
        for chars in zip(*strs):
            #(expression for element in iterable)
            if all(c == chars[0] for c in chars):
                prefix += 1                  
            else:
                break
            # extract the substring from the first string up to index 2 
            # (excluding the character at index 2):
        return strs[0][:prefix]
        
        
list1 = ['akshat', 'akash', 'akshay', 'akshita']
Result = Solution()
Other = Result.longestCommonPrefix(list1)

print(Other)
