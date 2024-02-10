# Leetcode 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        return len(s.split()[-1])


def test_solution():
    s = Solution()

    assert s.lengthOfLastWord("Hello World") == 5
    assert s.lengthOfLastWord("   fly me   to   the moon  ") == 4
    assert s.lengthOfLastWord("luffy is still joyboy") == 6
