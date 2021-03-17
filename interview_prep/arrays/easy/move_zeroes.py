from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_index = -1
        zero_size = -1
        for index, value in enumerate(nums):
            if value == 0:
                zero_index = index
                zero_size += 1
            elif zero_index >= 0:
                    nums[zero_index-zero_size] = value
                    nums[index] = 0
                    zero_index = index