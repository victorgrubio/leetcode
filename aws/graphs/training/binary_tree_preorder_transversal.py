# Given the root of a binary tree, return the preorder traversal of its nodes' values.
# Pre-order traversal is to visit the root first. Then traverse the left subtree.

from typing import List

class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recursive solution
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if not root:
            return result
        
        result += [root.val]
        result += self.preorderTraversal(root.left)
        result += self.preorderTraversal(root.right)
        return result
