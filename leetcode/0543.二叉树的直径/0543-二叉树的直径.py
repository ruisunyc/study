# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(root):

            if not root:return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.ans = max(self.ans,left+right)
            return max(left,right)+1
        dfs(root)
        return self.ans