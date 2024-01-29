# Leetcode 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/1735550/Python-Javascript-Easy-solution-with-very-clear-Explanation
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left, right = 0, 1
        current_max = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                current_max = max(current_max, prices[right] - prices[left])
            else:
                left = right
            right += 1

        return current_max


def test_solution():
    s = Solution()

    assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert s.maxProfit([7, 6, 4, 3, 1]) == 0
