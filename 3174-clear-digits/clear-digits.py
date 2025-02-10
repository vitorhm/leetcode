class Solution:
    def clearDigits(self, s: str) -> str:
        res = ""
        remove = 0
        i = len(s) - 1
        while i >= 0:
            if s[i].isdigit():
                remove += 1
            else:
                if remove > 0:
                    remove -= 1
                else:
                    res = s[i] + res

            i -= 1

        return res