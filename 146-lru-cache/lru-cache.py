class Node:
    def __init__(self, key: int, value: int, next = None, previous = None):
        self.key = key
        self.value = value
        self.next = next
        self.previous = previous

class LRUCache:
    def __init__(self, capacity: int):
        self.keys = {}
        self.head = None
        self.tail = None
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.keys:
            node = self.keys[key]
            # if node is already the head, then we simple return the value
            if node == self.head:
                return node.value
            
            # We need to move this node to the head
            self._moveToHead(node)

            return self.head.value
            
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            node = self.keys[key]
            node.value = value
            self._moveToHead(node)
        else:
            node = Node(key, value)
            self._moveToHead(node)
            
            self.keys[key] = node
            if len(self.keys) > self.capacity:
                self._removeLRU()

    def _removeLRU(self) -> None:
        if self.tail:
            del self.keys[self.tail.key]
            self.tail = self.tail.previous
            if self.tail:
                self.tail.next = None
            else:
                self.head = None

    def _moveToHead(self, node: Node) -> None:        

        if node == self.head:
            return
        
        self._unlink(node)
        self._addToHead(node)
        
    def _unlink(self, node: Node) -> None:
        # update the next pointer of the previous node to the next pointer of our node
        # PREV_NODE -> OUR_NODE -> NEXT_NODE ==> PREV_NODE -> NEXT_NODE
        if node.previous:
            node.previous.next = node.next
        if node.next:
            node.next.previous = node.previous
        
        if node == self.tail:
            self.tail = node.previous
            self.tail.next = None

    def _addToHead(self, node: Node) -> None:
        # Update the next point of our node to the head
        node.next = self.head
        # Set the previous node to None
        node.previous = None
        # Set the previous pointer of the head node to our node
        if self.head:
            self.head.previous = node
        # Set the head to be our node
        self.head = node

        if not self.tail:
            self.tail = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)