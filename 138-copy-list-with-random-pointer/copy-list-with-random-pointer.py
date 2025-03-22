"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        cur, res, relat_nodes = head, Node(head.val), {}
        cur_copy = res
        while cur:
            relat_nodes[cur] = cur_copy
            cur_copy.val = cur.val
            if cur.next:
                if cur.next in relat_nodes:
                    cur_copy.next = relat_nodes[cur.next]
                else:
                    cur_copy.next = Node(0)
                    relat_nodes[cur.next] = cur_copy.next
            if cur.random:
                if cur.random in relat_nodes:
                    cur_copy.random = relat_nodes[cur.random]
                else:
                    cur_copy.random = Node(0)
                    relat_nodes[cur.random] = cur_copy.random

            cur = cur.next
            cur_copy = cur_copy.next

        return res