from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        left = m -1
        cur = n - 1
        right = (m + n) - 1

        while cur >= 0:
            if left >= 0 and nums1[left] > nums2[cur]:
                nums1[right] = nums1[left]
                left -= 1
            else:
                nums1[right] = nums2[cur]
                cur -= 1

            right -= 1
