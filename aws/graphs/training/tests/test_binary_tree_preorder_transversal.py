from binary_tree_preorder_transversal import Solution, TreeNode
import unittest


class TestPreorder(unittest.TestCase):

  def test_1_preorder(self):
    root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
    result = [1,2,3]
    self.assertEquals(Solution().preorderTraversal(root), result)

  def test_2_preorder(self):
    root = TreeNode(3, TreeNode(1), TreeNode(2))
    result = [3,1,2]
    self.assertEquals(Solution().preorderTraversal(root), result)
