"""
Given the root of a binary tree and an integer targetSum, 
return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        currentSum = 0
        return self.is_equal_sum(root, targetSum, currentSum)

    def is_equal_sum(self, root, targetSum, currentSum):
        # Is a leaf node
        if not root:
            return False
        currentSum += root.val
        if (not root.left and not root.right):
            return currentSum == targetSum
        return self.is_equal_sum(root.left, targetSum, currentSum) or \
            self.is_equal_sum(root.right, targetSum, currentSum)