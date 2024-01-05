# Given two strings needle and haystack, return the index of the first
# occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution(object):
    def strStr(self, haystack, needle):
        if needle in haystack:
            return haystack.index(needle)
        return -1

bog = Solution()
haystack = "sadbutsad"
needle = "sad"
print(bog.strStr(haystack, needle)) #0 being the first occurrence of the word 'sad' in haystack

haystack = "leetcode"
needle = "leeto"
print(bog.strStr(haystack, needle)) #-1 due to not being in the 
