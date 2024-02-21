# Leetcode 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sub_sum = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            sub_sum[i + 1] += sub_sum[i] + num

        result = 10**5 + 1
        left, right = 0, 1
        while left < right and right <= len(nums):
            if sub_sum[right] - sub_sum[left] >= target:  # sum(nums[left:right])
                result = min(right - left, result)
                left += 1
            else:
                right += 1

        return result if result != 10**5 + 1 else 0

    def minSubArrayLen_space_optimal(self, target: int, nums: List[int]) -> int:
        result = 10**5 + 1
        left, right = 0, 1
        s = nums[left]  # sum(nums[left:right])
        while left < right:
            if target <= s:
                result = min(right - left, result)
                s -= nums[left]
                left += 1
            else:
                if right == len(nums):
                    break
                s += nums[right]
                right += 1

        return result if result != 10**5 + 1 else 0


def test_solution():
    s = Solution()

    assert s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
    assert s.minSubArrayLen(4, [1, 4, 4]) == 1
    assert s.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert s.minSubArrayLen(11, [1, 2, 3, 4, 5]) == 3
