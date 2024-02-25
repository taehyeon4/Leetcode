# Leetcode 76. Rotate Image
# https://leetcode.com/problems/rotate-image/

import copy
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        new_matrix = []
        for col in range(len(matrix[0])):
            new_row = [matrix[row][col] for row in reversed(range(len(matrix)))]
            new_matrix.append(new_row)

        for row in range(len(matrix)):
            matrix[row] = new_matrix[row]

    def rotate_optimal(self, matrix: List[List[int]]) -> None:
        """
        Source: https://leetcode.com/problems/rotate-image/discuss/18872/A-common-method-to-rotate-the-image
        Note: first reverse up to down, then swap the symmetry
        1 2 3     7 8 9     7 4 1
        4 5 6  => 4 5 6  => 8 5 2
        7 8 9     1 2 3     9 6 3
        """
        matrix.reverse()
        for row in range(len(matrix)):
            for col in range(row + 1, len(matrix[0])):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]


def test_solution():
    s = Solution()

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s.rotate_optimal(matrix)
    assert matrix == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    s.rotate_optimal(matrix)
    assert matrix == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
