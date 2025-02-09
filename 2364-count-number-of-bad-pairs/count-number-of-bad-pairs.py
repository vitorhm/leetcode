from collections import defaultdict
from typing import List

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        m = defaultdict(int)
        total_pairs = len(nums) * (len(nums) - 1) // 2
        good_pairs = 0
        for i in range(len(nums)):
            s = nums[i] - i
            good_pairs += m[s]
            m[s] += 1

        return total_pairs - good_pairs