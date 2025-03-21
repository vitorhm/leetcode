class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True
        arr1 = [0] * 26
        arr2 = [0] * 26
        diff = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]: diff += 1
            if diff > 2: return False
            arr1[ord(s1[i]) - ord('a')] += 1
            arr2[ord(s2[i]) - ord('a')] += 1

        return arr2 == arr1