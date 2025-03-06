class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        total = len(grid) ** 2
        unique = set()
        res = []
        for n in grid:
            for x in n:
                if x in unique: res.append(x)
                else: unique.add(x)

        i = 1
        while i <= total:
            if i not in unique:
                res.append(i)
                return res
            i += 1