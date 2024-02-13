# 6. Zigzag Conversion
# https://leetcode.com/problems/zigzag-conversion/


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s

        new_s = ""
        for i in range(numRows):
            up = i
            down = numRows - 1 - up

            j = i
            direction = [1, 0]  # Down, up direction flags
            while j < len(s):
                new_s += s[j]

                if up == 0:
                    j += down * 2
                elif down == 0:
                    j += up * 2
                else:
                    j += direction[0] * down * 2 + direction[1] * up * 2
                    direction.reverse()

        return new_s


def test_solution():
    s = Solution()

    assert s.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    """
    P   A   H   N  // s[0] s[4] s[8] s[12]      (down * 2, down * 2, ...)
    A P L S I I G  // s[1] s[3] s[5] s[7] ...   (down * 2, up * 2, ...)
    Y   I   R      // s[2] s[6] s[10]           (up * 2, up * 2, ...
    """

    assert s.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    """
    P     I    N  // s[0] s[6] s[12] 
    A   L S  I G  // s[1] s[5] s[7] s[11] s[13]
    Y A   H R     // s[2] s[4] s[8] s[10]
    P     I       // s[3] s[9]
    """

    assert s.convert("A", 1) == "A"
    assert s.convert("AB", 1) == "AB"
