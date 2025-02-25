# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        left = self.get_level(root, True)
        right = self.get_level(root, False)

        if left == right:
            return (2 ** left) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def get_level(self, root: TreeNode, go_left: bool = True) -> int:

        level = 0
        while root:
            level += 1
            if go_left:
                root = root.left
            else:
                root = root.right

        return level