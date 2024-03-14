# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root):
        if not root:
            return []

        res = []  # final list to return
        d = collections.deque()  # get a deque
        d.append(root)   # start with root
        while d:   # while deque is not empty
            dLen = len(d)

            for i in range(dLen):   # iterate for elements in deque
                curr = d.popleft()    # pop the leftmost element
                if i == dLen - 1:  # If it's the last element at this level, append to result
                    res.append(curr.val)

                # Add children if they aren't None
                if curr.left:
                    d.append(curr.left)
                if curr.right:
                    d.append(curr.right)

        return res
      
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

solution = Solution()
print(solution.rightSideView(root))

# Answer: [1, 3, 4]
