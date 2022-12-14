'''
https://leetcode.com/problems/validate-binary-search-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, prev =  [], None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev is not None and root is not None and root.val <= prev.val:
                return False
            prev, root = root, root.right
        return True
