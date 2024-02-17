# Leetcode 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/


class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for c in s:
            if c.isalpha():
                new_s += c.lower()
            elif c.isnumeric():
                new_s += c

        return True if new_s == new_s[::-1] else False


def test_solution():
    s = Solution()

    assert s.isPalindrome("A man, a plan, a canal: Panama") == True
    assert s.isPalindrome("race a car") == False
    assert s.isPalindrome(" ") == True
    assert s.isPalindrome("0P") == False
