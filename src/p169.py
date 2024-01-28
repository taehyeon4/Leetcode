# Leetcode 169. Majority Element
# https://leetcode.com/problems/majority-element/

from collections import defaultdict
import math
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        threshold = math.ceil(len(nums) / 2.0)

        i, count = 1, 1
        while count < threshold:
            if nums[i - 1] == nums[i]:
                count += 1
            else:
                count = 1
            i += 1

        return nums[i - 1]

    def majorityElement_sort(self, nums: List[int]) -> int:
        """
        Source: https://leetcode.com/problems/majority-element/discuss/3676530/3-Method's-oror-Beats-100-oror-C++-oror-JAVA-oror-PYTHON-oror-Beginner-Friendly
        Note: The majority element has to be at the middle of the array after sort it
        Time Complexity: O(NlogN)
        Space Complexity: No additional space
        """
        nums.sort()
        n = len(nums)
        return nums[n // 2]

    def majorityElement_hashmap(self, nums: List[int]) -> int:
        """
        Source: https://leetcode.com/problems/majority-element/discuss/3676530/3-Method's-oror-Beats-100-oror-C++-oror-JAVA-oror-PYTHON-oror-Beginner-Friendly
        Note: Hashmap!
        Time Complexity: O(N)
        Space Complexity: O(N/2)
        """
        n = len(nums)
        m = defaultdict(int)

        for num in nums:
            m[num] += 1

        n = n // 2
        for key, value in m.items():
            if value > n:
                return key

    def majorityElement_moorVoting(self, nums: List[int]) -> int:
        """
        Source: https://leetcode.com/problems/majority-element/discuss/3676530/3-Method's-oror-Beats-100-oror-C++-oror-JAVA-oror-PYTHON-oror-Beginner-Friendly
        Note: Boyer-Moore majority vote algorithm which can be used when the majority element guaranteed
        Time Complexity: O(N)
        Space Complexity: No additional space
        """
        count = 0
        candidate = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate


def test_solution():
    s = Solution()

    nums = [3, 2, 3]
    assert s.majorityElement_moorVoting(nums) == 3

    nums = [2, 2, 1, 1, 1, 2, 2]
    assert s.majorityElement_moorVoting(nums) == 2
