from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = []
        i, j = 0, 0

        while i < len(nums1) or j < len(nums2):
            if i >= len(nums1):
                res.append(nums2[j])
                j += 1
                continue
            if j >= len(nums2):
                res.append(nums1[i])
                i += 1
                continue

            arr1 = nums1[i]
            arr2 = nums2[j]

            if arr1[0] < arr2[0]:
                res.append(arr1)
                i += 1
            elif arr1[0] > arr2[0]:
                res.append(arr2)
                j += 1
            else:
                res.append([arr1[0], arr1[1] + arr2[1]])
                i += 1
                j += 1

        return res