# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            candidate = left + (right - left) // 2
            res = guess(candidate)

            if res == 0:
                return candidate
            elif res == -1:
                right = candidate - 1
            else:
                left = candidate + 1