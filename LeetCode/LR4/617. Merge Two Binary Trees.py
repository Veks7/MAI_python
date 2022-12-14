'''
https://leetcode.com/problems/merge-two-binary-trees/submissions/859336919/
'''
class Solution:
    def mergeTrees(self, temp1: TreeNode, temp2: TreeNode) -> TreeNode:
        if not temp1:
            return temp2
        if not temp2:
            return temp1
        temp1.val += temp2.val
        temp1.left = self.mergeTrees(temp1.left, temp2.left)
        temp1.right = self.mergeTrees(temp1.right, temp2.right)
        return temp1
