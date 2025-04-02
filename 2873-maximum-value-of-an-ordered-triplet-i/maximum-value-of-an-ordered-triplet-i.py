class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        
        maxElement = 0
        maxDiff = 0
        maxTriplet = 0
        for i in range(len(nums)):
            maxTriplet = max(maxTriplet, maxDiff * nums[i])
            maxElement = max(maxElement, nums[i])
            maxDiff = max(maxDiff, maxElement - nums[i])

        return maxTriplet