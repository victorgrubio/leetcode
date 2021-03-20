"""
Write a function that reverses a string. The input string is given as an array of characters s.
"""

from typing import List


class Solution:
  def reverseString(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    s[:] = s[::-1] # Equals to the content, not the variable, as the modification is inside the list