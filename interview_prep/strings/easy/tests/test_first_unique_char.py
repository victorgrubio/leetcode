from first_unique_char import Solution
import unittest


class TestFirstUniqueChar(unittest.TestCase):

  def test_first_unique_char_no_reps(self):
    s = "leetcode"
    result = 0
    self.assertEquals(Solution().firstUniqChar(s), result)

  def test_char_reps(self):
    s = "loveleetcode"
    result = 2
    self.assertEquals(Solution().firstUniqChar(s), result)

  def test_no_unique(self):
    s = "aabb"
    result = -1
    self.assertEquals(Solution().firstUniqChar(s), result)