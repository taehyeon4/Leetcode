# Leetcode 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

from collections import defaultdict
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i - 1] < prices[i]:
                profit += prices[i] - prices[i - 1]

        return profit


def test_solution():
    s = Solution()

    assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 7
    assert s.maxProfit([1, 2, 3, 4, 5]) == 4
    assert s.maxProfit([7, 6, 4, 3, 1]) == 0
