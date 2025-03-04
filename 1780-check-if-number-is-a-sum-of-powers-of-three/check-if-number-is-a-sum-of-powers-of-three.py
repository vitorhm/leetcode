class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        i = n
        while i > 0:
            if i % 3 == 2: return False
            i = i // 3

        return True