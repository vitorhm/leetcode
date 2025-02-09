from collections import defaultdict
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = defaultdict(int)
        max_count = 0
        majority = 0
        for i in nums:
            m[i] += 1
            cur = m[i]
            if cur > max_count:
                max_count = cur
                majority = i

        return majority