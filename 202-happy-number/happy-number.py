class Solution:
    def isHappy(self, n: int) -> bool:
        sum_squares = set()
        num = n
        while num != 1:
            sum_sq = 0
            for i in str(num):
                sum_sq += pow(int(i), 2)

            num = sum_sq

            if num in sum_squares: break
            sum_squares.add(num)

        return num == 1