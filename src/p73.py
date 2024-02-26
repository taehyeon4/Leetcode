# Leetcode 73. Set Matrix Zeroes
# https://leetcode.com/problems/set-matrix-zeroes/

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        indices = set()
        m, n = len(matrix), len(matrix[0])
        for row in range(m):
            for col in range(n):
                if matrix[row][col] != 0:
                    continue

                indices.update(set([(i, col) for i in range(m)]))
                indices.update(set([(row, i) for i in range(n)]))

        for row in range(m):
            for col in range(n):
                if (row, col) in indices:
                    matrix[row][col] = 0

    def setZeroes_optimal(self, matrix: List[List[int]]) -> None:
        """
        Source: https://leetcode.com/problems/set-matrix-zeroes/discuss/3472518/Full-Explanation-oror-Super-easy-oror-constant-space
        Note: We can keep whehter rows or cols should be 0 on the outer lines of matrix.
        Space Complexity: O(1)
        """
        row_0, col_0 = False, False
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] != 0:
                    continue

                if row == 0:
                    row_0 = True
                if col == 0:
                    col_0 = True
                matrix[row][0] = 0
                matrix[0][col] = 0

        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        if row_0:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0

        if col_0:
            for row in range(len(matrix)):
                matrix[row][0] = 0


def test_solution():
    s = Solution()

    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    s.setZeroes_optimal(matrix)
    assert matrix == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    s.setZeroes_optimal(matrix)
    assert matrix == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
