class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        for i in range(len(haystack) - len(needle) + 1):
            curN = 0
            while curN < len(needle) and haystack[i+curN] == needle[curN]:
                curN += 1

            if curN == len(needle): return i

        return -1