class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        un_nums = set()

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in un_nums:
                return i // 3 + 1
            un_nums.add(nums[i])

        return 0