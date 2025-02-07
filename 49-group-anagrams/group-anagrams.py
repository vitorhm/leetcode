class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for i in strs:
            m[''.join(sorted(i))].append(i)

        return list(m.values())