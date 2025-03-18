class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left, res = 0, 0
        bitmask = 0

        for right in range(len(nums)):
            while (bitmask & nums[right]) != 0:
                bitmask ^= nums[left]
                left += 1

            bitmask |= nums[right]
            res = max(res, right - left + 1)

        return res