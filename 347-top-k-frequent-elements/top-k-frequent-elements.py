from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = defaultdict(int)
        for i in nums:
            m[i] += 1

        res = [[] for i in range(len(nums) + 1)]
        for num, count in m.items():
            res[count].append(num)

        r = []
        for i in range(len(res) - 1, -1, -1):
            while len(res[i]) > 0:
                r.append(res[i].pop())
                if len(r) == k:
                    return r