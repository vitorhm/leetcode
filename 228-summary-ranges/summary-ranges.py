from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0

        while (i < len(nums)):
            start = nums[i]

            while i < len(nums) - 1 and nums[i + 1] == nums[i] + 1:
                i += 1

            if start == nums[i]:
                res.append(str(nums[i]))
            else:
                res.append(f'{start}->{nums[i]}')

            i += 1

        return res
