# 13. Integer to Roman
# https://leetcode.com/problems/integer-to-roman/


class Solution:
    INT_TO_ROMAN = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }

    def intToRoman(self, num: int) -> str:
        result = ""
        for i, roman in self.INT_TO_ROMAN.items():
            n, num = divmod(num, i)
            result += roman * n
        return result


def test_solution():
    s = Solution()

    assert s.intToRoman(3) == "III"
    assert s.intToRoman(58) == "LVIII"
    assert s.intToRoman(1994) == "MCMXCIV"
