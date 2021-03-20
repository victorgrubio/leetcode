from unittest import result
from reverse_string import Solution
import unittest


class TestReverseString(unittest.TestCase):

  def test_reverse_string(self):
    s = ["h","e","l","l","o"]
    result = ["o","l","l","e","h"]
    Solution().reverseString(s)
    self.assertEquals(s,result)