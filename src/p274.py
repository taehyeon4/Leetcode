# Leetcode 274. H-Index
# https://leetcode.com/problems/h-index/

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h_idx = 0
        for i in range(1, len(citations) + 1):
            h_idx = max(h_idx, min(i, len([j for j in citations if j >= i])))
        return h_idx

    def hIndex_sort(self, citations: List[int]) -> int:
        citations.sort()

        h_idx = 0
        for i, citation in enumerate(citations):
            if len(citations) - i <= citation:
                h_idx = len(citations) - i
                break
        return h_idx

    def hIndex_sort_binary_search(self, citations: List[int]) -> int:
        citations.sort()

        h_idx = 0
        n = len(citations)
        start, end = 0, n - 1

        while start <= end:
            mid = (start + end) // 2
            if n - mid <= citations[mid]:
                h_idx = max(h_idx, n - mid)
                end = mid - 1
            else:
                start = mid + 1

        return h_idx


def test_solution():
    s = Solution()

    assert s.hIndex_sort_binary_search([3, 0, 6, 1, 5]) == 3
    assert s.hIndex_sort_binary_search([1, 3, 1]) == 1
    assert s.hIndex_sort_binary_search([100]) == 1
