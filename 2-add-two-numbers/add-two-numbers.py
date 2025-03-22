# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_cur, l2_cur, res = l1, l2, None
        cur_res = None
        rest = 0

        while l1_cur or l2_cur or rest > 0:
            v = rest
            if l1_cur:
                v += l1_cur.val
                l1_cur = l1_cur.next
            if l2_cur:
                v += l2_cur.val
                l2_cur = l2_cur.next

            if v >= 10:
                rest = 1
                v -= 10
            else:
                rest = 0

            node = ListNode(v)
            if cur_res:
                cur_res.next = node
                cur_res = node
            else:
                res = node
                cur_res = res

        return res