# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        self.preorder(root, arr)

        return arr

    def preorder(self, node: Optional[TreeNode], arr: List[int]):
        if not node: return

        arr.append(node.val)
        self.preorder(node.left, arr)
        self.preorder(node.right, arr)