# Leetcode 76. Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        frequency = Counter(t)
        counter = {char: 0 for char in frequency}

        min_window = ""
        left, right = 0, 1
        if s[left] in frequency:
            counter[s[left]] += 1
        while left < right:
            found = all(counter[key] >= frequency[key] for key in frequency)
            if found:
                sub_str = s[left:right]
                if not min_window or len(sub_str) < len(min_window):
                    min_window = sub_str

                if s[left] in frequency:
                    counter[s[left]] -= 1
                left += 1
            else:
                if right == len(s):
                    break
                if s[right] in frequency:
                    counter[s[right]] += 1
                right += 1

        return min_window


def test_solution():
    s = Solution()

    assert s.minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert s.minWindow("a", "a") == "a"
    assert s.minWindow("a", "aa") == ""
