class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1: return x

        left = 1
        right = x
        middle = -1

        while left <= right:
            middle = left + (right - left) // 2

            sqr = middle * middle
            if sqr == x: 
                return middle
            elif sqr > x:
                right = middle - 1
            else:
                left = middle + 1
                
        return right
