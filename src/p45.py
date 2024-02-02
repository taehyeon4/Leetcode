# Leetcode 45. Jump Game II
# https://leetcode.com/problems/jump-game-ii/

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Time Complexity: O(N^2)
        Space Complexity: O(N)
        """
        min_steps = [10000 for i in range(len(nums))]
        min_steps[0] = 0

        current_idx = 1
        while current_idx < len(nums):
            for i in range(current_idx):
                if nums[i] + i < current_idx:
                    continue  # Unreachable to the current_idx
                min_steps[current_idx] = min(min_steps[current_idx], min_steps[i] + 1)

            current_idx += 1

        return min_steps[-1]

    def jump_optimal(self, nums: List[int]) -> int:
        """
        Source: https://leetcode.com/problems/jump-game-ii/discuss/1192401/Easy-Solutions-w-Explanation-or-Optimizations-from-Brute-Force-to-DP-to-Greedy-BFS
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        max_reachable, last_jumped_pos, jumps, i = 0, 0, 0, 0
        while last_jumped_pos < len(nums) - 1:
            max_reachable = max(max_reachable, i + nums[i])
            if i == last_jumped_pos:
                last_jumped_pos = max_reachable
                jumps += 1
            i += 1

        return jumps


def test_solution():
    s = Solution()

    assert s.jump_optimal([2, 3, 1, 1, 4]) == 2
    assert s.jump_optimal([2, 3, 0, 1, 4]) == 2
    assert s.jump_optimal([2, 3, 1, 4, 1, 1, 1, 2]) == 3
