# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:

        root = TreeNode()
        cur = root
        visited_levels, i, max_level = {}, 0, 0

        while i < len(traversal):
            num, level = '', 0

            while i < len(traversal) and traversal[i].isdigit():
                num += traversal[i]
                i += 1

            cur.val = int(num)

            while i < len(traversal) and traversal[i] == '-':
                level += 1
                i += 1

            max_level = max(max_level, level)

            if level:
                if level in visited_levels:
                    visited_levels[level].right = TreeNode()
                    cur = visited_levels[level].right
                    del visited_levels[level]

                    level += 1
                    while level <= max_level:
                        if level in visited_levels: del visited_levels[level]
                        level += 1
                else:
                    visited_levels[level] = cur
                    cur.left = TreeNode()
                    cur = cur.left

        return root