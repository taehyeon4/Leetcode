# Leetcode 134. Gas Station
# https://leetcode.com/problems/gas-station/

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """Simple brute force solution
        Note: Time Limit Exceeded on Leetcode
        Time Complexity: O(N^2)
        Space complexity: O(1)
        """
        n = len(gas)
        for start in range(n):
            current_idx = start
            current_gas = gas[current_idx]
            for i in range(1, n + 1):
                current_gas -= cost[current_idx]
                if current_gas < 0:
                    break
                next_idx = (start + i) % n
                current_gas += gas[next_idx]
                current_idx = next_idx

            if current_gas >= 0:
                return start
        return -1

    def canCompleteCircuit_optimal(self, gas: List[int], cost: List[int]) -> int:
        """
        Source: https://leetcode.com/problems/gas-station/discuss/1706142/JavaC%2B%2BPython-An-explanation-that-ever-EXISTS-till-now!!!!
        Time Complexity: O(N)
        Space complexity: O(1)
        """
        n, total_surplus, surplus, start = len(gas), 0, 0, 0

        for i in range(n):
            total_surplus += gas[i] - cost[i]
            surplus += gas[i] - cost[i]
            if surplus < 0:
                surplus = 0
                start = i + 1
        return -1 if (total_surplus < 0) else start


def test_solution():
    s = Solution()

    assert s.canCompleteCircuit_optimal([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
    assert s.canCompleteCircuit_optimal([2, 3, 4], [3, 4, 3]) == -1
