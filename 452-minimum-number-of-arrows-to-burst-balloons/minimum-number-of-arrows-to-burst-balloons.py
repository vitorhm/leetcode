from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort()
        end, arrows = float('-inf'), 0

        for point in points:
            if end < point[0]:
                arrows += 1
                end = point[1]
            elif end > point[1]:
                end = point[1]

        return arrows