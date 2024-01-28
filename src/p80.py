# Leetcode 80. Remove Duplicates from Sorted Array II
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)

        j = 2
        for i in range(2, len(nums)):
            if not (nums[j - 2] == nums[j - 1] == nums[i]):
                nums[j] = nums[i]
                j += 1

        return j


def test_solution():
    s = Solution()

    nums = [1, 1, 1, 2, 2, 3]

    expected_k = 5
    expected_nums = [1, 1, 2, 2, 3]

    k = s.removeDuplicates(nums)

    assert k == expected_k
    for i in range(k):
        assert nums[i] == expected_nums[i]
