#Given a linked list, swap every two adjacent nodes and return its head.
#For example,
#Given 1->2->3->4, you should return the list as 2->1->4->3.
#Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next==None:
            return head
        listHead=ListNode(None)
        listHead.next = head
        backup=head.next
        while listHead.next!=None and listHead.next.next!=None:
            temp= listHead.next
            tempnext=temp.next
            temp.next=tempnext.next
            tempnext.next=temp
            listHead.next=tempnext
            listHead=temp
        return backup