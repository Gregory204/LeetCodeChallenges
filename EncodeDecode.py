# Encode and Decode Strings
# Design an algorithm to encode a list of strings to a single string.
# The encoded string is then decoded back to the original list of strings.

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1

            # if s[j] == "#" grab the number
            length = int(s[i:j]) # excludes "#"
            i = j + 1 # at first character of wrd
            j = i + length # gets whole word between i & j
            res.append(s[i:j]) # append to result
            i = j 

        return res



            
