# Given the root of a binary tree, return the preorder traversal of its nodes' values.
# In-order traversal is to traverse the left subtree first. Then visit the root. Finally, traverse the right subtree.


from typing import List

class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if not root:
            return result
        
        result += self.postorderTraversal(root.left)
        result += self.postorderTraversal(root.right)
        result += [root.val]
        return result
