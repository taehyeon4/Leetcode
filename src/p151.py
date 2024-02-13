# 151. Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string/


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))


def test_solution():
    s = Solution()

    assert s.reverseWords("the sky is blue") == "blue is sky the"
    assert s.reverseWords("  hello world  ") == "world hello"
    assert s.reverseWords("a good   example") == "example good a"
