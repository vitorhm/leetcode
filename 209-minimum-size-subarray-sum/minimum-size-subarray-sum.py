from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cur_sum, left = 0, 0
        res = 0

        for right in range(len(nums)):
            cur_sum += nums[right]

            while cur_sum >= target:
                cur_len = right - left + 1
                cur_sum -= nums[left]
                left += 1

                if res == 0:
                    res = cur_len
                else:
                    res = min(res, cur_len)

        return res

