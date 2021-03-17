from typing import List
from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter: Counter = Counter(nums)
        for value in counter:
            if counter[value] == 1:
                return value