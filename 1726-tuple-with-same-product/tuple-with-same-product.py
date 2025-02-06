class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        m = defaultdict(int)
        res = 0
        for i in range(len(nums)):
            for x in range(i+1, len(nums)):
                product = nums[i] * nums[x]
                res += m[product] * 8                    
                m[product] += 1

        return res