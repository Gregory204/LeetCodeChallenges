# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            left = self.dfs(root.left)
            right = self.dfs(root.right)

            return 1 + max(left, right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        left = self.dfs(root.left) # gets height of left sub tree
        right = self.dfs(root.right) # gets height of right sub tree
        
        if abs(left - right) < 2:  # compare both subtrees to see if they are under 2
            return self.isBalanced(root.left) and self.isBalanced(root.right) # recursively call 
        else:
            return False
