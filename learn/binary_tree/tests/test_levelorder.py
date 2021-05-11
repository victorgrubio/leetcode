from binary_tree_preorder_transversal import TreeNode
from binary_tree_level_order import Solution
import unittest



class TestInorder(unittest.TestCase):

  def test_1(self):
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)) )
    result = [[3],[9,20],[15,7]]
    self.assertEquals(Solution().levelOrder(root), result)
  
  def test_2(self):
    root = TreeNode(1)
    result = [[1]]
    self.assertEquals(Solution().levelOrder(root), result)

  def test_3(self):
    root = TreeNode(1, TreeNode(2, 4, None), TreeNode(3, None, 5))
    result = [[1],[2,3],[4,5]]
    self.assertEquals(Solution().levelOrder(root), result)