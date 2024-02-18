# 392. Is Subsequence
# https://leetcode.com/problems/is-subsequence/


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for c in t:
            if i == len(s):
                break
            if s[i] == c:
                i += 1
        return i == len(s)


def test_solution():
    s = Solution()

    assert s.isSubsequence("abc", "ahbgdc") == True
    assert s.isSubsequence("axc", "ahbgdc") == False
