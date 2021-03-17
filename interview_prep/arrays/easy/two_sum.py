from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         # for index, num in enumerate(nums):
         #   for index_2 in range(index+1, len(nums)):
         #       if nums[index_2] == (target - nums[index]):
         #           return [index, index_2]
         myHash = {}
         for index, value in enumerate(nums):
            if target - value in myHash:
                return [myHash[target-value], index]
            myHash[value] = index