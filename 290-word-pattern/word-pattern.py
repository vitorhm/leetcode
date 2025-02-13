class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        m_word = {}
        m_pattern = {}
        j = 0

        for pat in pattern:
            word = ''
            while j < len(s):
                c = s[j]
                j += 1
                if c == ' ': break
                word += c

            if word == '': return False
            if pat in m_pattern and m_pattern[pat] != word: return False
            if word in m_word and m_word[word] != pat: return False

            m_word[word] = pat
            m_pattern[pat] = word

        if j != len(s): return False

        return True