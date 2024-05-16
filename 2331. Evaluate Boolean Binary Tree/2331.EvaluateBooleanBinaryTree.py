# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def evaluateTree(self, root):
        if root.val == 0 or root.val == 1:
            return root.val
        result = []
        return traverse(root, result)[-1]


def traverse(cur, result):
    if cur.left is not None:
        traverse(cur.left, result)
    if cur.right is not None:
        traverse(cur.right, result)
    if cur.val == 2:
        result.append(cur.left.val or cur.right.val)
        cur.val = cur.left.val or cur.right.val
    if cur.val == 3:
        result.append(cur.left.val and cur.right.val)
        cur.val = cur.left.val and cur.right.val
    return result
