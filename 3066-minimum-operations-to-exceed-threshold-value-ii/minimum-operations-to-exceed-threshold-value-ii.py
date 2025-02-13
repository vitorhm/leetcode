import heapq
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        res = 0
        x = heapq.heappop(nums)
        while x < k:
            y = heapq.heappop(nums)
            res += 1

            op = min(x, y) * 2 + max(x, y)
            x = heapq.heappushpop(nums, op)

        return res