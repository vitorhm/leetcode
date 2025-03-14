class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # find the max candy on a pile (also sum the candies)
        max_candy, sum_candy = 0, 0
        for c in candies:
            sum_candy += c
            if c > max_candy:
                max_candy = c
        
        # more kids than the total of candies
        if sum_candy < k:
            return 0

        # use binary search to find the maximum number
        max_number = 0
        begin, end = 1, max_candy
        while begin <= end:
            candidate = begin + (end - begin) // 2
            piles = 0
            for c in candies:
                piles += c // candidate

            if piles >= k:
                max_number = candidate
                begin = candidate + 1
            else:
                end = candidate - 1    
            
        return max_number