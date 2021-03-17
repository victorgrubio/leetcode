from typing import List, Set


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_nums: Set[int] = set(nums)
        return len(set_nums) < len(nums)
        