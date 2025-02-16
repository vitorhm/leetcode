class Solution:
    def can_partition(self, str_num, target):

        if not str_num and target == 0:
            return True

        if target < 0:
            return False

        for index in range(len(str_num)):
            left = str_num[: index + 1]
            right = str_num[index + 1 :]
            left_num = int(left)

            if self.can_partition(right, target - left_num):
                return True

        return False

    def punishmentNumber(self, n: int) -> int:
        res = 0

        for num in range(1, n + 1):
            square_num = num * num

            if self.can_partition(str(square_num), num):
                res += square_num

        return res