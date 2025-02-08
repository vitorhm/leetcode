class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while (l < r):
            while l < r and not self.isAlpha(s[l]):
                l += 1

            while l < r and not self.isAlpha(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower(): return False
            l += 1
            r -= 1

        return True

    def isAlpha(self, s: str) -> bool:
        return ord(s.lower()) in range(ord('a'), ord('z') + 1) or ord(s) in range(ord('0'), ord('9') + 1)