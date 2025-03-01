class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n + 1)

        def climbStairsMemo(n: int) -> int:
            if n <= 3: return n

            if memo[n] != -1: return memo[n]

            s = climbStairsMemo(n - 2) + climbStairsMemo(n - 1)
            memo[n] = s

            return s

        return climbStairsMemo(n)