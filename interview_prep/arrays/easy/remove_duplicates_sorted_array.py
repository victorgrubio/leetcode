from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_value = None
        index = 0
        while index < len(nums):
            num = nums[index] 
            if num == last_value:
                del(nums[index])
            else:
                last_value = num
                index += 1
        return len(nums)
                