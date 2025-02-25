# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        return self.dfs(root, 0, targetSum)
    
    def dfs(self, node: TreeNode, cur_sum: int, targetSum: int) -> bool:
        if not node:
            return False

        cur_sum += node.val

        # We reached a leaf node
        if not node.right and not node.left:
            return cur_sum == targetSum

        return self.dfs(node.left, cur_sum, targetSum) or self.dfs(node.right, cur_sum, targetSum)