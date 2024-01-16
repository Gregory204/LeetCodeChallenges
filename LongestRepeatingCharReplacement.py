# You are given a string s and an integer k. You can choose any
# character of the string and change it to any other uppercase
# English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same
# letter you can get after performing the above operations.

class Solution(object):
    def characterReplacement(self, s, k):
        count = {}
        l = 0
        r = 0
        longest = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)  # Using get() is useful when you want to avoid a KeyError if the key is not present
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1  # decrease the value of that specific character
                l += 1  # increase the pointer for the windows beginning
            longest = max(longest, r-l+1)
        return longest


s = "AABABBA"
k = 1
print(Solution().characterReplacement(s, k))
# Output 4
