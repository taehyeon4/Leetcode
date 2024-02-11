# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        result = strs[0]

        for s in strs[1:]:
            for i in range(len(s)):
                if i == len(result):
                    break
                if result[i] != s[i]:
                    if i == 0:
                        result = ""
                    else:
                        result = result[:i]
                    break
        return result

    def longestCommonPrefix_optimal(self, strs: List[str]) -> str:
        """
        Source: https://leetcode.com/problems/longest-common-prefix/discuss/3273176/Python3-oror-C%2B%2Boror-Java-19-ms-oror-Beats-99.91
        Note: You only need to compare the fisrt and last elements to calculate longest prefix, once the strs are sorted.
        """
        strs.sort()
        result = ""
        for i in range(len(strs[0])):
            if strs[0][i] == strs[-1][i]:
                result += strs[0][i]
            else:
                break
        return result


def test_solution():
    s = Solution()

    assert s.longestCommonPrefix_optimal(["flower", "flow", "flight"]) == "fl"
    assert s.longestCommonPrefix_optimal(["dog", "racecar", "car"]) == ""
    assert s.longestCommonPrefix_optimal(["ab", "a"]) == "a"
