from __future__ import print_function
import unittest
from SwapNodesinPairs import Solution,ListNode

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

class Test_SwapNodesinPairs(unittest.TestCase):
    def test_swapPairs(self):
        printListNode(Solution().swapPairs(createListNode([1,2,3,4])))
        printListNode(Solution().swapPairs(createListNode([1,2,3,4,5])))
        printListNode(Solution().swapPairs(createListNode([1,2,3,4,5,6])))
        printListNode(Solution().swapPairs(createListNode([1])))
        printListNode(Solution().swapPairs(createListNode([1,2])))
        printListNode(Solution().swapPairs(createListNode([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])))

if __name__ == '__main__':
    unittest.main()
