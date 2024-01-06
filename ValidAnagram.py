# Given two strings s and t, return true if t is an anagram
# of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the
# letters of a different word or phrase, typically using all
# the original letters exactly once.

class Solution(object):
    def isAnagram(self, s, t):
        s_list = list(s)
        t_list = list(t)
        s_list.sort()
        t_list.sort()
        s_list.reverse()
        t_list.reverse()
        if s_list == t_list:
            return True
        return False


s = "anagram"
t = "nagaram"
print(Solution().isAnagram(s, t))        #True
print(Solution().isAnagram('rat', 'car')) #False
print(Solution().isAnagram('aa', 'a')) #False
print(Solution().isAnagram('a', 'b')) #False
