class Solution(object):
    def isPalindrome(self, s):
        tab = []
        bog = "".join(map(str, s))
        # A man, a plan, a canal: Panama
        for string in range(len(bog)):
            if bog[string].isalnum():
                tab.append(bog[string].lower())
        if tab == tab[::-1]:
            return True
        return False

'''
I love one line solutions.
class Solution(object):
    def isPalindrome(self, s):
        return [x.lower() for x in "".join(map(str, s)) if x.isalnum()] == [x.lower() for x in "".join(map(str, s)) if x.isalnum()][::-1]
'''
s = [" "]
print(Solution().isPalindrome(s))
# Output: True
