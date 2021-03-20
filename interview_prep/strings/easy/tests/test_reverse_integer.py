import unittest
from reverse_integer import Solution


class TestReverseInteger(unittest.TestCase):

  def test_reverse_integer(self):
    init_value = 321
    final_value = 123
    self.assertEquals(Solution().reverse(init_value), final_value)
  
  def test_reverse_negative_integer(self):
    init_value = -123
    final_value = -321
    self.assertEquals(Solution().reverse(init_value), final_value)
  
  def test_reverse_exceeding_boundaries(self):
    init_value = 1534236469
    final_value = 0
    self.assertEquals(Solution().reverse(init_value), final_value)