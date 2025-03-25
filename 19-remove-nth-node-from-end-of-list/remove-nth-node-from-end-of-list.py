# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dic = {}
        cur, ind = head, 1
        while cur:
            dic[ind] = cur
            cur = cur.next
            ind += 1

        deleted_pos = ind - n

        # The first node was deleted
        if deleted_pos == 1:
            # If we have only 1 node, then return None
            if len(dic) == 1:
                return None

            # Return the next node (now he is the head)
            return dic[deleted_pos + 1]

        # Set the next to the previous
        dic[deleted_pos - 1].next = dic[deleted_pos].next
        
        return dic[1]
            