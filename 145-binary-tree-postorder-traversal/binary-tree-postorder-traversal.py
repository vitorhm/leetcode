# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        self.postorder(root, arr)
        return arr

    def postorder(self, node: Optional[TreeNode], arr: List[int]):
        if not node: return

        self.postorder(node.left, arr)
        self.postorder(node.right, arr)
        arr.append(node.val)