# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        def dfs(node: TreeNode, prev: TreeNode) -> TreeNode:
            temp_left = node.left
            temp_right = node.right

            node.left = None
            if prev:
                prev.right = node

            last = node

            if temp_left:
                last = dfs(temp_left, node)
            
            if temp_right:
                last = dfs(temp_right, last)

            return last

        dfs(root, None)