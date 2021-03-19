from typing import List, Dict


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        if Solution.__is_not_edge_case(k, len_nums):
            # Nums[:] to mutate the object
            # Always use the remainder of the division of k and length
            # first k%len_nums = rotated nums from the end
            # Then we move the rest K%len_nums positions to the right
            nums[:] = nums[(-k%len_nums):] + nums[:(len_nums-k%len_nums)]
        else:
            pass
        return nums

    @classmethod
    def __is_not_edge_case(cls, k, len_nums):
        """
        Edge cases:
            k = 0 -> return nums (no rotate)
            len_nums = 1 -> we can't rotate
            k % len_nums = 0 -> no rotation due to rest = 0 
        """
        return k > 0 and len_nums > 1 and k%len_nums != 0

    @staticmethod
    def rotate_1(nums, k):
        """First attempt to solve using a dict
        It was slow and also crashed in hard_test. Check test to see failure.
        It worked perfectly for edge cases
        """
        len_nums = len(nums)
        tmp_dict = {num: (index + k)%len_nums for index, num in enumerate(nums)}
        for key, value in tmp_dict.items():
            nums[value] = key
        return nums
    