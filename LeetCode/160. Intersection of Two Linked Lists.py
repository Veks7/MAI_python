# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        first = headA 
        second = headB

        while first is not second:
            if first is None:
                first = headB 
            else:
                first=first.next
            if second is None:
                second = headA 
            else:
                second=second.next

        return first
