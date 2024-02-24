# Leetcode 30. Substring with Concatenation of All Words
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

from collections import Counter, defaultdict
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = set()
        n = len(words[0])
        frequency = Counter(words)

        for k in range(n):
            counter = defaultdict(int)
            counted_words = []

            for i in range(k, len(s), n):
                word = s[i : i + n]
                if frequency[word]:
                    if counter[word] < frequency[word]:
                        counter[word] += 1
                    else:  # counter[word] == frequency[word]
                        counted_word = counted_words.pop(0)
                        while counted_word != word:
                            counter[counted_word] -= 1
                            counted_word = counted_words.pop(0)
                    counted_words.append(word)
                else:
                    counter = defaultdict(int)
                    counted_words = []

                if counter == dict(frequency):
                    result.add(i - (len(words) - 1) * n)

        return list(result)


def test_solution():
    s = Solution()

    assert set(s.findSubstring("barfoothefoobarman", ["foo", "bar"])) == set([0, 9])
    assert set(
        s.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"])
    ) == set([])
    assert set(
        s.findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"])
    ) == set([6, 9, 12])
    assert set(
        s.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"])
    ) == set([8])
    assert set(
        s.findSubstring(
            "lingmindraboofooowingdingbarrwingmonkeypoundcake",
            ["fooo", "barr", "wing", "ding", "wing"],
        )
    ) == set([13])
    assert set(s.findSubstring("aaaaaaaaaaaaaa", ["aa", "aa"])) == set(
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    )
