from typing import List, Set


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_nums1: Set[int] = set(nums1)
        set_nums2: Set[int] = set(nums2)
        return list(set_nums1.intersection(set_nums2))