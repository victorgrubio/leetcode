"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """ Top down solution
    public boolean isSymmetric(TreeNode root) {
        return isMirror(root, root);
    }

    public boolean isMirror(TreeNode t1, TreeNode t2) {
        if (t1 == null && t2 == null) return true;
        if (t1 == null || t2 == null) return false;
        return (t1.val == t2.val)
            && isMirror(t1.right, t2.left)
            && isMirror(t1.left, t2.right);
    }
    """
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.is_mirror(root, root)
    def is_mirror(self, t1: TreeNode, t2: TreeNode) -> bool: 
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        return ( t1.val == t2.val) and self.is_mirror(t1.right, t2.left) and self.is_mirror(t1.left, t2.right)