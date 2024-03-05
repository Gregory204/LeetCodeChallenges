# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root

        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:  # if we find values p or q
                return curr

# p = 2
# q = 8

''' Tree Represenation
            6
          /   \
         2      8
        / \    / \
       0   4  7   9
          / \
         3   5
'''   

# RESULT = 6
