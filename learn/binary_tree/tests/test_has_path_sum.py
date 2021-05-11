from has_path_sum import Solution, TreeNode
import unittest


class TestHasPathSum(unittest.TestCase):

  def test_1(self):
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    result = 4
    self.assertEquals(Solution().hasPathSum(root, result), True)