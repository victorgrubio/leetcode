"""
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
"""
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        list_s = list(s)
        less_index = len(s)
        char_counter = Counter(s)
        for element, value in char_counter.items():
          if value == 1:
            index = list_s.index(element)
            if index < less_index:
              less_index = index
        if less_index == len(s):
          return -1
        return less_index