 #Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head==None:
            return None
        point = []
        while head!=None:
            point.append(head)
            head=head.next
        if n ==len(point):
            return point[0].next
        point[-n-1].next=point[-n].next
        return point[0]