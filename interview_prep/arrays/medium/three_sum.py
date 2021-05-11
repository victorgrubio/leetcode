from typing import List


class Solution:
    """
    Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
    Notice that the solution set must not contain duplicate triplets.
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        storage_list = []
        nums = list(set(nums))
        len_nums = len(nums)
        for index in range(0, len_nums):
            num = nums[index]
            if index == len_nums:
                break
            for second_index in range(index+1, len_nums):
                for third_index in range(second_index+1, len_nums):
                    final_list = [nums[second_index], nums[third_index]]
                    if sum(final_list) == -num:
                        final_list.insert(0, num)
                        if not len(storage_list):
                            storage_list = [final_list]
                        else:
                            storage_list.append(final_list)
        return storage_list
    
