from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True

        for i in range(len(nums) - 1):
            num1 = nums[i]
            num2 = nums[i + 1]

            if num1 % 2 == 0 and num2 % 2 == 0: return False
            if num1 % 2 != 0 and num2 % 2 != 0: return False

        return True