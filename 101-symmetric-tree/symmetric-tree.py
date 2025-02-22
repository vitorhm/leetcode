# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSymmetricRec(root.left, root.right)

    def isSymmetricRec(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right: return True
        if not left or not right: return False

        return left.val == right.val and self.isSymmetricRec(left.left, right.right) and self.isSymmetricRec(left.right, right.left)