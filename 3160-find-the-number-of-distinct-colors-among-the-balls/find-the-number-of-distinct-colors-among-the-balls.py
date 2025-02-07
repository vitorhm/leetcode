class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        mCircles = defaultdict(int)
        mColors = defaultdict(int)
        res = []
        for query in queries:
            circle = query[0]
            color = query[1]

            if circle in mCircles:
                oldColor = mCircles[circle]
                mColors[oldColor] -= 1
                if mColors[oldColor] == 0:
                    del mColors[oldColor]

            mCircles[circle] = color
            mColors[color] += 1
            res.append(len(mColors))
        
        return res