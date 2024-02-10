# Leetcode 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/

import copy
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        left = []
        for i in range(len(height)):
            while left and height[left[-1]] < height[i]:
                left_i = left.pop()

                if left:
                    l, left_bound = left[-1], height[left[-1]]
                    min_bound = min(height[i], left_bound)
                    result += (i - l - 1) * (min_bound - height[left_i])

            left.append(i)

        return result


def test_solution():
    s = Solution()

    assert s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert s.trap([4, 2, 0, 3, 2, 5]) == 9
    assert s.trap([4, 2, 3]) == 1
    assert s.trap([5, 4, 1, 2]) == 1
