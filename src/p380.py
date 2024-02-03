# 380. Insert Delete GetRandom O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1/

import random


class RandomizedSet:

    def __init__(self):
        self._internal_set = set()

    def insert(self, val: int) -> bool:
        if val in self._internal_set:
            return False

        self._internal_set.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self._internal_set:
            return False

        self._internal_set.remove(val)
        return True

    def getRandom(self) -> int:
        return random.choice(list(self._internal_set))


def test_solution():
    randomizedSet = RandomizedSet()
    assert randomizedSet.insert(1) == True
    assert randomizedSet.remove(2) == False
    assert randomizedSet.insert(2) == True
    assert randomizedSet.getRandom() in [1, 2]
    assert randomizedSet.remove(1) == True
    assert randomizedSet.insert(2) == False
    assert randomizedSet.getRandom() == 2
