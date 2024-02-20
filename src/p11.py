# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/

from typing import List


class Solution:
    def maxArea_bruteforce(self, height: List[int]) -> int:
        max_area = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                max_area = max((j - i) * min(height[i], height[j]), max_area)
        return max_area

    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:
            area = (right - left) * min(height[left], height[right])
            max_area = max(area, max_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


def test_solution():
    s = Solution()

    assert s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert s.maxArea([1, 1]) == 1
    assert s.maxArea([1, 8, 100, 2, 100, 4, 8, 3, 7]) == 200
