from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        last_index = 0

        for i in range(len(nums)):
            if i < (len(nums) - 1) and nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

            if nums[i] != 0:
                res[last_index] = nums[i]
                last_index += 1

        return res
