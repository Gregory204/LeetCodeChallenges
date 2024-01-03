class Solution(object):
    def removeDuplicates(self, nums):
        
        # sorted(set(nums)): This sorts the unique elements obtained from the set 
        # in ascending order. 
        # When you use nums[:], you get a new list that is a copy of the original list. 
        # The reason for using this notation is to perform an "in-place" modification 
        # of the original list.
        
        nums[:] = sorted(set(nums))
        return len(nums)

# Example usage:
list1 = [1, 1, 2,3,4,4,5,5,6,1,1,2,3]
result = Solution().removeDuplicates(list1)

print(result)  # Output: 2
print(list1)   # Output: [1, 2, ...]

'''
A function like this isn't necessary to remove duplicates but its leetcode so I 
just did it for the fun of it. Main objective is to get rid of common elememts
in a list.
'''
