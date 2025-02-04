from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, maximum, r, = 0, 0, len(heights) - 1

        while (l < r):
            amount = (r - l) * min(heights[l], heights[r])
            maximum = max(maximum, amount)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maximum