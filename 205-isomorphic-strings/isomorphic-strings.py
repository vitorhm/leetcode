class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        for i in range(len(s)):
            cur_s = s[i]
            cur_t = t[i]
            if cur_s in s_map and s_map[cur_s] != cur_t:
                return False
            if cur_t in t_map and t_map[cur_t] != cur_s:
                return False

            s_map[cur_s] = t[i]
            t_map[cur_t] = s[i]

        return True