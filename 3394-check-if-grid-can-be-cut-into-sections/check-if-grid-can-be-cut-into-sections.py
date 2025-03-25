class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:

        rectangles.sort()

        max_end_x, max_end_y, count_sec, count_sec_y = rectangles[0][2], rectangles[0][3], 0, 0
        for start_x, start_y, end_x, end_y in rectangles:
            if start_x >= max_end_x:
                count_sec += 1
            if start_y >= max_end_y:
                count_sec_y += 1

            max_end_x = max(max_end_x, end_x)
            max_end_y = max(max_end_y, end_y)

            if count_sec == 2 or count_sec_y == 2:
                return True

        return False