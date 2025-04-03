class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_num = 0
        max_diff = 0
        max_val = 0

        for i in range(len(nums)):
            max_val = max(max_val, max_diff * nums[i])
            max_num = max(max_num, nums[i])
            max_diff = max(max_diff, max_num - nums[i])

        return max_val