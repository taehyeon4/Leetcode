# 135. Candy
# https://leetcode.com/problems/candy/

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        n = len(ratings)
        candies = [1] * n

        for i in range(n):
            if i - 1 >= 0 and ratings[i - 1] < ratings[i]:
                candies[i] = candies[i - 1] + 1

        for i in reversed(range(n)):
            if i + 1 < n and ratings[i + 1] < ratings[i]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)


def test_solution():
    s = Solution()

    assert s.candy([1, 0, 2]) == 5
    assert s.candy([1, 2, 2]) == 4
    assert s.candy([1, 2, 87, 87, 87, 2, 1]) == 13
    assert s.candy([1, 2, 3, 4, 5]) == 15
