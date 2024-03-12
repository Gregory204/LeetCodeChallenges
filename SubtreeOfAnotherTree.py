# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        def SameTree(tree1, tree2):  # used code from previous leetcode (EFFICIENT)
            if tree1 is None and tree2 is None:
                return True
            if tree1 is None or tree2 is None:
                return False

            return (tree1.val == tree2.val and
                    SameTree(tree1.left, tree2.left) and
                    SameTree(tree1.right, tree2.right))

        stack = [root]

        while stack:
            curr = stack.pop()

            if curr.val == subRoot.val and SameTree(curr, subRoot):
                return True

            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)

        return False

