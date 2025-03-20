class Solution:
    def minOperations(self, nums: List[int]) -> int:
        left, right, res, has_zero = 0, 2, 0, False

        while right < len(nums):
            if nums[right] == 0:
                has_zero = True
                
            if nums[left] != 0:
                left += 1
                right += 1
                continue

            res += 1

            has_zero = False
            for i in range(left, right + 1):
                nums[i] = abs(nums[i] - 1)
                if nums[i] == 0:
                    has_zero = True

            right += 1
            left += 1
        
        if has_zero:
            return -1

        return res
        