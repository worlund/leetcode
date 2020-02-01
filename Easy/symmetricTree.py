# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # recurs = self.isSymmetric_rec(root)
        iterat = self.isSymmetric_it(root)

        return iterat

    def isSymmetric_rec(self, root: TreeNode) -> bool:
        if not root:
            return True

        def mirror(t1, t2) -> bool:
            if t1 == None and t2 == None:
                return True
            if t1 == None or t2 == None:
                return False
            return t1.val == t2.val and mirror(t1.left, t2.right) and mirror(t1.right, t2.left)

        return mirror(root.left, root.right)

    def isSymmetric_it(self, root: TreeNode) -> bool:
        if not root:
            return True

        q = deque([root])

        while q:
            level = []
            for _ in range(len(q)):
                curr = q.popleft()
                if curr != None:
                    level.append(curr.left)
                    level.append(curr.right)
            i, j = 0, len(level) - 1
            while i <= j:
                if level[i] and level[j]:
                    if level[i].val != level[j].val:
                        return False
                if (level[i] and not level[j]) or (level[j] and not level[i]):
                    return False
                i += 1
                j -= 1
            q.extend(level)

        return True