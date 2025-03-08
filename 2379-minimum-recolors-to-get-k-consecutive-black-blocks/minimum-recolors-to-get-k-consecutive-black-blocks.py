class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        w_count, left, right = 0, 0, k - 1

        for i in range(k):
            if blocks[i] == 'W':
                w_count += 1

        current_w_count = w_count

        while right < len(blocks) - 1:
            if w_count == 0:
                return 0

            right += 1
            left += 1

            if blocks[left - 1] == 'W':
                current_w_count -= 1

            if blocks[right] == 'W':
                current_w_count += 1

            w_count = min(w_count, current_w_count)

        return w_count
