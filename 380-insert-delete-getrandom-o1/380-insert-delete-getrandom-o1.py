from collections import defaultdict
from random import random

class RandomizedSet:

    def __init__(self):
        self.structure = defaultdict(int)
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.structure:
            return False

        self.structure[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.structure:
            return False

        ind = self.structure[val]
        last_val = self.arr[-1]
        self.arr[ind] = self.arr[-1]
        self.structure[last_val] = ind

        del self.arr[-1]
        del self.structure[val]

        return True

    def getRandom(self) -> int:
        rand = random.randrange(0, len(self.arr))
        val = self.arr[rand]
        return val

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()