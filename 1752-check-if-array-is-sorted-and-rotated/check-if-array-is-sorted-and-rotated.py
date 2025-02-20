class Solution:
    def check(self, nums: List[int]) -> bool:

        rotated = False
        for i in range(1, len(nums)):
            num = nums[i]
            if num < nums[i-1]:
                if rotated: return False
                if nums[-1] > nums[0]: return False
                rotated = True

        return True