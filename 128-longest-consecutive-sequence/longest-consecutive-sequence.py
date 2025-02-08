class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        maxSeq = 0
        for i in uniqueNums:
            if (i - 1) in uniqueNums:
                continue

            c = 1
            while (i + c) in uniqueNums:
                c += 1

            maxSeq = max(maxSeq, c)

        return maxSeq