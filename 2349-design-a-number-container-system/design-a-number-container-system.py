from collections import defaultdict

from sortedcontainers import SortedSet


class NumberContainers:

    def __init__(self):
        self.container = defaultdict(SortedSet)
        self.indexedNumbers = {}

    def change(self, index: int, number: int) -> None:

        if index in self.indexedNumbers:
            oldNumber = self.indexedNumbers[index]
            self.container[oldNumber].remove(index)

        self.indexedNumbers[index] = number
        self.container[number].add(index)

    def find(self, number: int) -> int:
        heap = self.container[number]
        if len(heap) == 0:
            return -1

        return self.container[number][0]