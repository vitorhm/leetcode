# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        arr1, arr2 = [], []

        self.dfs(p, arr1)
        self.dfs(q, arr2)

        return arr1 == arr2

    def dfs(self, node, arr):
        if node:
            arr.append(node.val)
            self.dfs(node.left, arr)
            self.dfs(node.right, arr)
        else:
            arr.append(None)