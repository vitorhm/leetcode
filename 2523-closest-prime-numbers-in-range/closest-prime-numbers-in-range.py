class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        arr = [True] * (right + 1)
        arr[0] = arr[1] = False

        p = 2
        while p * p <= right:
            if arr[p] == True:
                for n in range(p * p, right + 1, p):
                    arr[n] = False
            
            p += 1

        primes = []
        for i in range(left, right + 1):
            if arr[i] == True:
                primes.append(i)

        pair = (-1, -1)
        min_diff = float('inf')
        for i in range(1, len(primes)):
            diff = primes[i] - primes[i - 1]
            if diff < min_diff:
                min_diff = diff
                pair = (primes[i-1], primes[i])

        return pair
