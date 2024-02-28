# Leetcode 383. Ransom Note
# https://leetcode.com/problems/set-matrix-zeroes/

from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        characters = defaultdict(int)
        for c in magazine:
            characters[c] += 1

        for c in ransomNote:
            if not characters[c]:
                return False
            characters[c] -= 1

        return True


def test_solution():
    s = Solution()

    assert s.canConstruct("a", "b") == False
    assert s.canConstruct("aa", "ab") == False
    assert s.canConstruct("aa", "aab") == True
