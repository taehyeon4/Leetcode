# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/


class Solution:
    ROAM_TO_INT = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    ROAM_TO_RAOM = {
        "IV": "IIII",
        "IX": "VIIII",
        "XL": "XXXX",
        "XC": "LXXXX",
        "CD": "CCCC",
        "CM": "DCCCC",
    }

    def romanToInt(self, s: str) -> int:
        for pattern, replacement in self.ROAM_TO_RAOM.items():
            s = s.replace(pattern, replacement)

        result = 0
        for char in s:
            result += self.ROAM_TO_INT[char]
        return result

    def romanToInt2(self, s: str) -> int:
        result = 0
        n = len(s)
        for i in range(n):
            if i + 1 < n and self.ROAM_TO_INT[s[i]] < self.ROAM_TO_INT[s[i + 1]]:
                result -= self.ROAM_TO_INT[s[i]]
            else:
                result += self.ROAM_TO_INT[s[i]]

        return result


def test_solution():
    s = Solution()

    assert s.romanToInt2("III") == 3
    assert s.romanToInt2("LVIII") == 58
    assert s.romanToInt2("MCMXCIV") == 1994
