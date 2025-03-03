from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        begin, end = 0, len(nums) - 1
        left, right = 0, len(nums) - 1
        res = [pivot] * len(nums)
        pivot_count = 0

        while begin < len(nums):
            if nums[begin] < pivot:
                res[left] = nums[begin]
                left += 1

            if nums[end] > pivot:
                res[right] = nums[end]
                right -= 1

            if nums[left] == pivot:
                pivot_count += 1

            begin += 1
            end -= 1

        return res