from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_map = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in nums_map:
                if abs(nums_map[num] - i) <= k: return True

            nums_map[num] = i

        return False