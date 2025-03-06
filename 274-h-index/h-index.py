from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        bucket = [0] * (len(citations) + 1)
        n = len(citations)

        for i in range(len(citations)):
            if citations[i] > n:
                bucket[n] += 1
            else:
                bucket[citations[i]] += 1

        total = 0
        for i in range(n, -1, -1):
            total += bucket[i]
            if total >= i:
                return i