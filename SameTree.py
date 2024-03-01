# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def isSameTree(self, p: [TreeNode], q: [TreeNode]) -> bool:
        if p == None and q == None:
            return True
        elif p is None or q is None:
            return False

        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

  # Recursion made this so much easier also p.val and q.val just so nodes are converted back into
  # numbers such as 0 == 0 or 4 == 4.
