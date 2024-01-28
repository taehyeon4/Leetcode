# Leetcode 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        already_exists = set()
        idx = 0

        for i in range(len(nums)):
            if nums[i] not in already_exists:
                nums[idx] = nums[i]
                already_exists.add(nums[i])
                idx += 1

        return idx

    def removeDuplicates_optimal(self, nums: List[int]) -> int:
        """
        Source: https://leetcode.com/problems/remove-duplicates-from-sorted-array/discuss/3676877/Best-Method-oror-100-oror-C++-oror-JAVA-oror-PYTHON-oror-Beginner-Friendly
        Note: The given nums are already sorted
        """
        j = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[j] = nums[i]
                j += 1

        return j


def test_solution():
    s = Solution()

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

    expected_nums = [0, 1, 2, 3, 4]
    expected_k = 5

    k = s.removeDuplicates_optimal(nums)
    assert k == expected_k
    for i in range(k):
        assert nums[i] == expected_nums[i]
