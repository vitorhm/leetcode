class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        s = nums[0]
        temp = s
        for i in range(1, len(nums)):
            cur = nums[i]
            prev = nums[i-1]

            if cur > prev:
                temp += cur
            else:
                temp = cur

            s = max(s, temp)

        return s