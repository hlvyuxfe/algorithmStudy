import unittest
from RemoveNthNodeFromEndofList import Solution, ListNode

def printListNode(l):
    while l!= None:
        print ('%d '% l.val,end="")
        l=l.next
    print('\n')

def createListNode(l):
    listNode=ListNode(None)
    temp = listNode
    for i in l:
        temp.next = ListNode(i)
        temp = temp.next
    return listNode.next

class Test_RemoveNthNodeFromEndofList(unittest.TestCase):

    def test_removeNthFromEnd(self):
        printListNode(Solution().removeNthFromEnd(createListNode([1,2,3,4,5]),1))
        printListNode(Solution().removeNthFromEnd(createListNode([1,2,3,4,5]),2))
        printListNode(Solution().removeNthFromEnd(createListNode([1,2,3,4,5]),3))
        printListNode(Solution().removeNthFromEnd(createListNode([1,2,3,4,5]),4))
        printListNode(Solution().removeNthFromEnd(createListNode([1,2,3,4,5]),5))
        printListNode(Solution().removeNthFromEnd(createListNode([1,2]),1))
        printListNode(Solution().removeNthFromEnd(createListNode([1,2]),2))
        printListNode(Solution().removeNthFromEnd(createListNode([1]),1))
        printListNode(Solution().removeNthFromEnd(createListNode([]),1))

if __name__ == '__main__':
    unittest.main()
