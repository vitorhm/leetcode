class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        num_reversed = 0
        n = x
        while n > 0:
            last_digit = n % 10
            num_reversed = num_reversed * 10 + last_digit
            n = n // 10

        return num_reversed == x