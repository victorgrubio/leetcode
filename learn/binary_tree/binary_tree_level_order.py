from collections import deque
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if not root:
            return result
        my_queue = deque()
        my_queue.append([root])
        while len(my_queue) > 0:
            iteration_result = []
            for value in my_queue.pop():
                if value == None:
                    continue
                iteration_result.append(value.val)
                my_queue.append([value.left, value.right])
            if iteration_result:
                result.append(iteration_result)
        return result