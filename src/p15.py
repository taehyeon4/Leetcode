# 15. 3Sum
# https://leetcode.com/problems/3sum/

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                two_sum = nums[left] + nums[right]
                if two_sum + nums[i] == 0:
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif two_sum + nums[i] < 0:
                    left += 1
                else:
                    right -= 1

        return [list(answer) for answer in result]


def test_solution():
    s = Solution()

    assert s.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, 0, 1], [-1, -1, 2]]
    assert s.threeSum([0, 1, 1]) == []
    assert s.threeSum([0, 0, 0]) == [[0, 0, 0]]
