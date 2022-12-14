'''
https://leetcode.com/problems/path-sum/submissions/859335943/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        
        if root.val==sum and root.left is None and root.right==None:
            return True
        
        else:
            sum =sum - root.val
            return(self.hasPathSum(root.left,sum)or self.hasPathSum(root.right,sum))
