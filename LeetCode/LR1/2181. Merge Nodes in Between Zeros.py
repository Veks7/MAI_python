'''
2181. Merge Nodes in Between Zeros
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        temp = head
        while temp:
            if temp.val == 0:
                res = 0
                sec = temp
                temp = temp.next
                while temp.val != 0:
                    res += temp.val
                    temp = temp.next
                sec.val = res
                if temp.next :
                    sec.next = temp
                else:
                    sec.next = None
                    break
        return head
