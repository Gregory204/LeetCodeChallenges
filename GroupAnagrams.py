# Given an array of strings strs, group the anagrams together.
# You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the
# letters of a different word or phrase, typically using all
# the original letters exactly once.

'''
#HASHMAP
class Solution:
    def groupAnagrams(self, strs):
        strs_table = {}

        for string in strs:
            sorted_string = ''.join(sorted(string))

            if sorted_string not in strs_table:
                strs_table[sorted_string] = []
            print(strs_table)
            strs_table[sorted_string].append(string)
            print(strs_table)

        return list(strs_table.values())

'''
# if is an anagram we look for possible elements with same
# number of letters and same letters


class Solution(object):
    def groupAnagrams(self, strs):
        string_table = {}  # Hash
        '''
        string_table = {}  # Hash
        string_table['sorted_str'] = []
        print(string_table)
        Output: {'sorted_str': []}
        '''
        for string in strs:
            sorted_str = ''.join(sorted(string))

            if sorted_str not in string_table:  # aet
                string_table[sorted_str] = []  # aet : []
            string_table[sorted_str].append(string)  # aet : ['eat']

        return list(string_table.values())



strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))
# Output [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
