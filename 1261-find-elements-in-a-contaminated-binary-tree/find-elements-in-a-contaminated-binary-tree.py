# Definition for a binary tree node.
from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.values = set()
        self.values.add(0)

        queue = deque()
        queue.append(self.root)
        root.val = 0

        while len(queue) > 0:
            cur = queue.popleft()
            if cur.left:
                cur.left.val = 2 * cur.val + 1
                self.values.add(cur.left.val)
                queue.append(cur.left)

            if cur.right:
                cur.right.val = 2 * cur.val + 2
                self.values.add(cur.right.val)
                queue.append(cur.right)

    def find(self, target: int) -> bool:
        return target in self.values