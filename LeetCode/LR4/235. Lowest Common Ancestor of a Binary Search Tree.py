'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/submissions/859335242/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        c = root
        
        while c:
            if p.val < c.val and q.val < c.val:
                c = c.left
            elif p.val > c.val and q.val > c.val:
                c = c.right
            else:
                return c
