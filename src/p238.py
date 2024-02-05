# Leetcode 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Source: https://leetcode.com/problems/product-of-array-except-self/discuss/3186745/Best-C%2B%2B-3-Solution-oror-DP-oror-Space-optimization-oror-Brute-Force-greater-Optimize-oror-One-Stop-Solution.
        Time Complexity: O(N)
        Space Complexity: O(1) except for the output result
        """
        n = len(nums)
        result = [1] * n

        for i in range(1, n):
            result[i] = result[i - 1] * nums[i - 1]

        right = 1
        for i in reversed(range(n - 1)):
            right *= nums[i + 1]
            result[i] *= right

        return result


def test_solution():
    s = Solution()

    assert s.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert s.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
