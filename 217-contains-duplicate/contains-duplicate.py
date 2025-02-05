class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniques = set()
        for i in nums:
            if i in uniques: return True
            uniques.add(i)
        
        return False