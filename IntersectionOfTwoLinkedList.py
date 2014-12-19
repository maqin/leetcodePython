# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA==None or headB==None:
            return None
        l1 = headA
        l2 = headB
        len1 = 1
        len2 = 1
        while l1.next!=None:
            len1 += 1
            l1 = l1.next
        while l2.next!=None:
            len2 += 1
            l2 = l2.next
        if l1!=l2:
            return None
        step = 0
        l1 = headA
        l2 = headB
        if len1>len2:
            step = len1 - len2
            while step>0:
                l1 = l1.next
                step -= 1
        else:
            step = len2 - len1
            while step>0:
                l2 = l2.next
                step -= 1
        while l1!=l2:
            l1 = l1.next
            l2 = l2.next
        return l1
