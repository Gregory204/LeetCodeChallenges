class Solution:
    def findRepeatedDnaSequences(self, s):
        Freq = {} # HashMap
        burger = ""
        solution = [] # put answers here
        for i in range(len(s)): # iterate through all chars
            burger = s[i:i+10] # rolling HashMap TECH
            if len(burger) == 10: # we have a 10 letter word
                if burger in Freq and burger not in solution:
                    solution.append(burger) 
                else:
                    Freq[burger] = 1 # just putting it in dictionary
                                     # for future use in the problem
        return solution

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

