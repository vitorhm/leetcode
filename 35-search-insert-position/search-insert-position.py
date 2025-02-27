from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            num = nums[middle]

            if target == num:
                return middle
            elif target > num:
                left = middle + 1
            else:
                right = middle - 1

        return left