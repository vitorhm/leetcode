# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        inorder = []
        def dfs(node: TreeNode):

            if len(inorder) == k:
                return

            if not node:
                return

            dfs(node.left)
            if len(inorder) < k:
                inorder.append(node.val)
            dfs(node.right)

        dfs(root)
        return inorder[-1]