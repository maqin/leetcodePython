# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head==None:
            return None
        start = head
        while start!=None:
            n = start.next
            r = RandomListNode(start.label)
            start.next = r
            r.next = n
            start = n
        start = head
        while start!=None:
            if start.random!=None:
                start.next.random = start.random.next
            start = start.next.next
        start = head
        res = head.next
        while start!=None:
            n = start.next.next
            if n!=None:
                start.next.next = n.next
            start.next = n
            start = n
        return res
            
        
