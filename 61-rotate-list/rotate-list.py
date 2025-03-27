# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
            
        latest = head
        s = 1
        while latest.next:
            latest = latest.next
            s += 1

        rotations = k % s

        # make circular
        latest.next = head
        cur = head
        prev = head
        for _ in range(s, rotations, -1):
            prev = cur
            cur = cur.next

        prev.next = None
        return cur

