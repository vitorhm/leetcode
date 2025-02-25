class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        even_count, odd_count, parity_sum, res = 1, 0, 0, 0

        for n in arr:
            parity_sum += n

            if parity_sum % 2 == 0:
                even_count += 1
                res += odd_count
            else:
                odd_count += 1
                res += even_count

        return res % (10**9 + 7)