'''
https://leetcode.com/problems/balanced-binary-tree/description/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        def bal(node):
            if not node:
                return 0
            left_p = bal(node.left) + 1
            right_p = bal(node.right) + 1
            if abs(left_p - right_p) >= 2:
                return float('inf')
            else:
                return max(left_p, right_p)
        
        return bal(root) != float('inf')
