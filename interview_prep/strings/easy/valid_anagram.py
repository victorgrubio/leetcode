from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(s) != len(t):
        return False
      counter_s = Counter(s)
      counter_t = Counter(t)
      for element, value in counter_s.items():
        t_value = counter_t.get(element)
        if t_value and t_value == value:
          continue
        else:
          return False
      return True