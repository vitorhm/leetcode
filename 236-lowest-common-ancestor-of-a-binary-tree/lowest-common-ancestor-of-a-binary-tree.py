# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def lca(node: TreeNode) -> TreeNode:
            if not node or node == p or node == q:
                return node

            l = lca(node.left)
            r = lca(node.right)

            if l and r:
                return node
            
            if not l:
                return r

            return l

        return lca(root)
            
