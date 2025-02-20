# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None: return False

        se = set()
        cur = head.next
        while cur is not None:
            if cur in se: return True
            se.add(cur)
            cur = cur.next

        return False