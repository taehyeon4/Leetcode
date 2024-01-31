# Leetcode 55. Jump Game
# https://leetcode.com/problems/jump-game/

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        current_dest = len(nums) - 1
        idx = current_dest - 1
        while idx >= 0:
            if current_dest <= idx + nums[idx]:
                current_dest = idx
            idx -= 1

        return current_dest == 0


def test_solution():
    s = Solution()

    assert s.canJump([2, 3, 1, 1, 4]) == True
    assert s.canJump([3, 2, 1, 0, 4]) == False
