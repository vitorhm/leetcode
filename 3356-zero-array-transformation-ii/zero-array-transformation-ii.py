from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        left, right, res = 0, len(queries), -1

        if not self.can_be_zero(nums, queries, right):
            return -1

        while left <= right:
            cur = left + (right - left) // 2
            if self.can_be_zero(nums, queries, cur):
                res = cur
                right = cur - 1
            else:
                left = cur + 1

        return res

    def can_be_zero(self, nums: List[int], queries: List[List[int]], n: int) -> bool:

        diff_array = [0] * (len(nums) + 1)

        # build the diff array
        for i in range(n):
            l, r, val = queries[i]
            diff_array[l] -= val
            diff_array[r + 1] += val

        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += diff_array[i]
            temp = nums[i] + cur_sum
            if temp > 0:
                return False

        return True