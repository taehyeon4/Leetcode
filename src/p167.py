# 167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            two_sum = numbers[left] + numbers[right]
            if two_sum == target:
                return [left + 1, right + 1]
            elif two_sum < target:
                left += 1
            else:
                right -= 1


def test_solution():
    s = Solution()

    assert s.twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert s.twoSum([2, 3, 4], 6) == [1, 3]
    assert s.twoSum([-1, 0], -1) == [1, 2]
