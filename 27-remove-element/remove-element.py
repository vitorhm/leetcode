from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, end_index = 0, len(nums) - 1

        while i < len(nums):
            while end_index >= i and nums[i] == val:
                nums[i] = nums[end_index]
                end_index -= 1

            i += 1

        return end_index + 1