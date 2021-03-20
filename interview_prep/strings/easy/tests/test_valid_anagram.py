from valid_anagram import Solution
import unittest


class TestValidAnagram(unittest.TestCase):

  def test_valid_anagram(self):
    s = "car"
    t = "rac"
    self.assertTrue(Solution().isAnagram(s,t))

  def test_not_valid_anagram(self):
    s = "car"
    t = "rat"
    self.assertFalse(Solution().isAnagram(s,t))

  def test_not_equal_strings(self):
    s = "car"
    t = "ra"
    self.assertFalse(Solution().isAnagram(s,t))
    