# Leetcode 27. Remove Element
# https://leetcode.com/problems/remove-element/

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[idx] = nums[i]
                idx += 1

        return idx


def test_solution():
    s = Solution()

    nums = [3, 2, 2, 3]
    val = 3

    expected_nums = [2, 2, 3, 3]
    expected_k = 2

    k = s.removeElement(nums, val)

    assert k == expected_k
    for i in range(k):
        assert nums[i] == expected_nums[i]
