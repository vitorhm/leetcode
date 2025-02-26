# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev_val = -float('inf')
        self.diff = float('inf')

        self.dfs(root)
        return self.diff

    def dfs(self, node: Optional[TreeNode]):
        if not node: return
        
        self.dfs(node.left)

        self.diff = min(self.diff, node.val - self.prev_val)
        self.prev_val = node.val

        self.dfs(node.right)
