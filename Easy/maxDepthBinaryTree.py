# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # tail recursion
    def maxDepth(self, root: TreeNode) -> int:
        return self.maxD(root, 1)

    def maxD(self, root: TreeNode, h: int) -> int:
        # base case
        if root == None:
            return 0
        # leaf node
        if root.left == None and root.right == None:
            return h
        # max of left and right children
        return max(self.maxD(root.left, h + 1), self.maxD(root.right, h + 1))