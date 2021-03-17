from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
        else:
            index = -1
            while digits[index] == 9:
                digits[index] = 0
                if abs(index) == len(digits):
                    digits.insert(0, 1)
                    return digits
                index -= 1
            digits[index] += 1
        return digits