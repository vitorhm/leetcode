# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # [4,9,5,1,0]
        stack = []
        self.res = 0
        def dfs(node: TreeNode, prev: str = ''):
            prev += f'{node.val}'

            if node.left:
                dfs(node.left, prev)
            if node.right:
                dfs(node.right, prev)

            if not node.left and not node.right:
                self.res += int(prev)

        dfs(root)
        return self.res