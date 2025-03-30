class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        let_count = defaultdict(int)
        for letter in s:
            let_count[letter] += 1

        current_letters, temp_count, res = defaultdict(int), 0, []
        for letter in s:
            temp_count += 1
            current_letters[letter] += 1
            if current_letters[letter] == let_count[letter]:
                del current_letters[letter]
            if len(current_letters) == 0:
                res.append(temp_count)
                temp_count = 0

        return res