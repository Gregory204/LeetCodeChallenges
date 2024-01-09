# Given an integer array nums and an integer k, return the k
# most frequent elements. You may return the answer in any order.

class Solution(object):
    def topKFrequent(self, nums, k):
        my_dict = {}
        for num in nums:
            if num in my_dict:  # 1
                my_dict[num] += 1 # 1 : 2 then becomes 3
            else:   # if num not in my_dict
                my_dict[num] = 1    # since num wasnt in beginning it would be first 1 : 1
        sorted_keys = sorted(my_dict, key=lambda x: my_dict[x], reverse=True)
        return sorted_keys[:k]

# sorted_keys = sorted(my_dict, key=lambda x: my_dict[x], reverse=True)
# The lambda function extracts the values corresponding to each
# key: my_dict['a'], my_dict['b'], my_dict['c'], my_dict['d'].
# The keys are then sorted based on these values in descending order, resulting in
# [1,2,3].
# If reverse = False it would be ascending order 3 lowest, 2, 1 highest
nums = [1,1,1,2,2,3]
print(Solution().topKFrequent(nums, k = 2))
# Output: [1,2]
