class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        begin, end = 0, len(nums) - 1
        
        first_pos = len(nums)
        while begin <= end:
            ind = begin + (end - begin)
            
            if nums[ind] < 0:
                begin = ind + 1
            else:
                first_pos = ind
                end = ind - 1

        first_neg = len(nums)
        begin, end = 0, len(nums) - 1
        while begin <= end:
            ind = begin + (end - begin)
            
            if nums[ind] <= 0:
                begin = ind + 1
            else:
                first_neg = ind
                end = ind - 1

        return max(first_pos, len(nums) - first_neg)