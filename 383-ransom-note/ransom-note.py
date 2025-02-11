from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ranson_count = defaultdict(int)

        for s in ransomNote:
            ranson_count[s] += 1

        for s in magazine:
            if s in ranson_count:
                ranson_count[s] -= 1
                if ranson_count[s] == 0:
                    del ranson_count[s]

            if len(ranson_count) == 0: return True

        return False