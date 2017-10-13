# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp=l3 = ListNode(None)
        c=0
        while l1!=None or l2!=None or c!=0:
            if l1!=None and l2 !=None:
                l3.next,c = (ListNode(l1.val+l2.val+c),0) if l1.val+l2.val+c <10 else (ListNode(l1.val+l2.val+c - 10) ,1)
                l1 ,l2,l3= l1.next,l2.next,l3.next
            elif l1!=None and l2==None:
                l3.next,c = (ListNode(l1.val+c),0) if l1.val+c <10 else (ListNode(l1.val+c - 10) ,1)
                l1,l3=l1.next,l3.next
            elif l1==None and l2!=None:
                l3.next,c = (ListNode(l2.val+c),0) if l2.val+c <10 else (ListNode(l2.val+c - 10) ,1)
                l2,l3= l2.next,l3.next
            else:
                l3.next ,c=ListNode(c),0
        return temp.next
