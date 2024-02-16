# Leetcode 68. Text Justification
# https://leetcode.com/problems/text-justification/

from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        count = 0
        s = []
        result = []
        for word in words:
            if count + len(word) + len(s) > maxWidth:
                new_s = ""
                num_of_spaces = len(s) - 1 if len(s) - 1 else 1
                size_of_group, remainder = divmod(maxWidth - count, num_of_spaces)
                spaces = [
                    " " * (size_of_group + (1 if i < remainder else 0))
                    for i in range(num_of_spaces)
                ]

                for i in range(len(s)):
                    new_s += s[i] + (spaces[i] if i < num_of_spaces else "")
                result.append(new_s)
                count = 0
                s = []

            s.append(word)
            count += len(word)

        new_s = " ".join(s)
        result.append(new_s + " " * (maxWidth - len(new_s)))
        return result


def test_solution():
    s = Solution()

    assert s.fullJustify(
        ["This", "is", "an", "example", "of", "text", "justification."], 16
    ) == [
        "This    is    an",
        "example  of text",
        "justification.  ",
    ]

    assert s.fullJustify(
        ["What", "must", "be", "acknowledgment", "shall", "be"], 16
    ) == [
        "What   must   be",
        "acknowledgment  ",
        "shall be        ",
    ]

    assert s.fullJustify(
        [
            "Science",
            "is",
            "what",
            "we",
            "understand",
            "well",
            "enough",
            "to",
            "explain",
            "to",
            "a",
            "computer.",
            "Art",
            "is",
            "everything",
            "else",
            "we",
            "do",
        ],
        20,
    ) == [
        "Science  is  what we",
        "understand      well",
        "enough to explain to",
        "a  computer.  Art is",
        "everything  else  we",
        "do                  ",
    ]
