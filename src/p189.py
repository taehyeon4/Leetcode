# Leetcode 189. Rotate Array
# https://leetcode.com/problems/rotate-array/

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return

        k = k % len(nums)
        if k == 0:
            return

        nums_temp = nums[-k:] + nums[: len(nums) - k]
        nums[:] = nums_temp[:]

    def roate_optimal(self, nums: List[int], k: int) -> None:
        """
        Source: https://leetcode.com/problems/rotate-array/discuss/3506340/Beats-100-3-Line-Solution-oror-Fully-MOST-Optimised-Code
        Time complexity: O(N)
        Space complexity: O(1)
        """
        k = k % len(nums)
        nums[: len(nums) - k] = reversed(nums[: len(nums) - k])
        nums[-k:] = reversed(nums[-k:])
        nums.reverse()


def test_solution():
    s = Solution()

    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3

    s.roate_optimal(nums, k)
    assert nums == [5, 6, 7, 1, 2, 3, 4]
