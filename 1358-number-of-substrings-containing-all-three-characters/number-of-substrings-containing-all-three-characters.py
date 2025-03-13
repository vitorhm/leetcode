class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left, right, res = 0, 0, 0
        abc_count = defaultdict(int)

        while right < len(s):

            abc_count[s[right]] += 1
                
            while len(abc_count) == 3:
                res += len(s) - right

                count_letter = abc_count[s[left]]

                if count_letter == 1:
                    del abc_count[s[left]]
                else:
                    abc_count[s[left]] -= 1

                left += 1

            right += 1

        return res