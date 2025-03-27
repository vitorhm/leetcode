# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        smaller_tree, greater_tree = ListNode(-1), ListNode(-1)
        cur, cur_smaller, cur_greater = head, smaller_tree, greater_tree

        while cur:
            if cur.val < x:
                cur_smaller.next = cur
                cur_smaller = cur
            else:
                cur_greater.next = cur
                cur_greater = cur

            cur = cur.next

        cur_smaller.next = greater_tree.next
        cur_greater.next = None

        return smaller_tree.next