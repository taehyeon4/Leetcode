# Leetcode 205. Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/

from collections import Counter


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_map = {}
        for i in range(len(s)):
            if s[i] not in char_map:
                if t[i] in char_map.values():
                    return False
                char_map[s[i]] = t[i]
                continue
            if t[i] != char_map[s[i]]:
                return False
        return True


def test_solution():
    s = Solution()

    assert s.isIsomorphic("egg", "add") == True
    assert s.isIsomorphic("foo", "bar") == False
    assert s.isIsomorphic("paper", "title") == True
    assert s.isIsomorphic("bbbaaaba", "aaabbbba") == False
    assert s.isIsomorphic("badc", "baba") == False
