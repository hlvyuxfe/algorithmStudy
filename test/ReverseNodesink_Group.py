#Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
#You may not alter the values in the nodes, only nodes itself may be changed.
#Only constant memory is allowed.
#For example,
#Given this linked list: 1->2->3->4->5
#For k = 2, you should return: 2->1->4->3->5
#For k = 3, you should return: 3->2->1->4->5
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
def reversek(head,k):
    i=0
    newHead = temp = head.next
    head.next = None
    while i<k:
        backup = temp.next
        temp.next = head.next
        head.next=temp
        temp=backup
        i+=1
    newHead.next = backup
    return newHead

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k==1 or not head:
            return head
        temp = listHead = ListNode(None)
        listHead.next = head
        i,head=0,temp
        while temp!=None:
            i+=1
            temp = temp.next
            if i==k and temp!=None:
                i=0
                head=reversek(head,k)
                temp = head
        if i<=k:
            return listHead.next
        

