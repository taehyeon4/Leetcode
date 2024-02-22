# Leetcode 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            numbers = set()
            for col in range(9):
                if board[row][col] in numbers:
                    return False
                if board[row][col] != ".":
                    numbers.add(board[row][col])

        for col in range(9):
            numbers = set()
            for row in range(9):
                if board[row][col] in numbers:
                    return False
                if board[row][col] != ".":
                    numbers.add(board[row][col])

        mask = [
            [-1, -1],
            [-1, 0],
            [-1, 1],
            [0, -1],
            [0, 0],
            [0, 1],
            [1, -1],
            [1, 0],
            [1, 1],
        ]
        for row in range(1, 8, 3):
            for col in range(1, 8, 3):
                numbers = set()
                for dy, dx in mask:
                    if board[row + dy][col + dx] in numbers:
                        return False
                    if board[row + dy][col + dx] != ".":
                        numbers.add(board[row + dy][col + dx])

        return True

    def isValidSudoku_simple(self, board: List[List[str]]) -> bool:
        """
        Source: https://leetcode.com/problems/valid-sudoku/discuss/3277043/Beats-96.78-oror-Short-7-line-Python-solution-(with-detailed-explanation)
        """
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != ".":
                    res += [
                        (i, "*", element),
                        ("*", j, element),
                        (i // 3, j // 3, element),
                    ]
        return len(res) == len(set(res))


def test_solution():
    s = Solution()
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert s.isValidSudoku_simple(board) == True

    board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert s.isValidSudoku_simple(board) == False

    board = [
        [".", ".", ".", ".", "5", ".", ".", "1", "."],
        [".", "4", ".", "3", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", "3", ".", ".", "1"],
        ["8", ".", ".", ".", ".", ".", ".", "2", "."],
        [".", ".", "2", ".", "7", ".", ".", ".", "."],
        [".", "1", "5", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", "2", ".", ".", "."],
        [".", "2", ".", "9", ".", ".", ".", ".", "."],
        [".", ".", "4", ".", ".", ".", ".", ".", "."],
    ]
    assert s.isValidSudoku_simple(board) == False
