# Leetcode 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        result = []
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1

        result.extend(nums1[i:m])
        result.extend(nums2[j:n])
        nums1[:] = result[:]

    def merge_optimal(self, nums1, m, nums2, n):
        """
        Source: https://leetcode.com/problems/merge-sorted-array/discuss/3436053/Beats-100-oror-Best-C++JavaPython-and-JavaScript-Solution-oror-Two-Pointer-oror-STL
        Note: Override nums1 in reverse order.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1


def test_solution():
    s = Solution()

    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m, n = 3, 3

    s.merge(nums1, m, nums2, n)

    assert nums1 == [1, 2, 2, 3, 5, 6]
