from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == ".": continue

                if (num in rows[r] or
                    num in columns[c] or
                    num in squares[r // 3, c // 3]):
                    return False

                rows[r].add(num)
                columns[c].add(num)
                squares[r // 3, c // 3].add(num)

        return True