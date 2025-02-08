from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = []
        nums.sort()
        for i in range(len(nums)):
            current = nums[i]

            if current > 0: break
            if i > 0 and current == nums[i-1]: continue

            l = i + 1
            r = len(nums) - 1
            while (l < r):
                s = current + nums[l] + nums[r]
                if (s > 0):
                    r -= 1
                elif (s < 0):
                    l += 1
                else:
                    arr.append([current, nums[l], nums[r]])
                    l += 1
                    while l < len(nums) and nums[l] == nums[l - 1]:
                        l += 1

        return arr