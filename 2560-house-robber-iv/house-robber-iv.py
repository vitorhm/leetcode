from typing import List

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        min_val, max_val = float('inf'), 0
        for n in nums:
            min_val = min(min_val, n)
            max_val = max(max_val, n)

        while min_val <= max_val:
            candidate = min_val + (max_val - min_val) // 2
            if self.find_min(nums, k, candidate):
                max_val = candidate - 1
            else:
                min_val = candidate + 1

        return min_val

    def find_min(self, nums: List[int], k: int, candidate: int) -> bool:
        houses, i = 0, 0

        while i < len(nums):
            if nums[i] <= candidate:
                houses += 1
                i += 1
                if houses == k:
                    return True

            i += 1

        return False