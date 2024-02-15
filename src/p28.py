# Leetcode 28. Find the Index of the First Occurrence in a String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

    def strStr_manual(self, haystack: str, needle: str) -> int:
        n = len(needle)
        for i in range(len(haystack) - n + 1):
            if needle == haystack[i : i + n]:
                return i
        return -1


def test_solution():
    s = Solution()

    assert s.strStr_manual("sadbutsad", "sad") == 0
    assert s.strStr_manual("leetcode", "leeto") == -1
    assert s.strStr_manual("hello", "ll") == 2
    assert s.strStr_manual("mississippi", "issip") == 4
