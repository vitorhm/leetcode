from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for interval in intervals:
            if len(res) == 0:
                res.append(interval)
            else:
                last_interval = res[-1]
                if interval[0] >= last_interval[0] and interval[0] <= last_interval[1]:
                    last_interval[1] = max(last_interval[1], interval[1])
                else:
                    res.append(interval)

        return res