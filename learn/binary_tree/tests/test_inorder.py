from binary_tree_preorder_transversal import TreeNode
from binary_tree_inorder_transversal import Solution
import unittest



class TestInorder(unittest.TestCase):

  def test_1(self):
    root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
    result = [1,3,2]
    self.assertEquals(Solution().inorderTransversal(root), result)
