# Definition for singly-linked list.
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
from heapq import heapify,heappop,heappush
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        i=0
        while i < len(lists):
            if not lists[i]:
                del lists[i]
                continue
            i+=1
        if len(lists)==0:
            return None
        if len(lists)==1:
            return lists[0]
        listHead=[(i.val,index) for index,i in enumerate(lists)]
        heapify(listHead)
        listNode=ListNode(None)
        temp = listNode
        while(len(listHead))>1:
            Node = heappop(listHead)
            temp.next = lists[Node[1]]
            temp=temp.next
            lists[Node[1]]= lists[Node[1]].next
            if lists[Node[1]]!=None:
                heappush(listHead,(lists[Node[1]].val,Node[1]))
        temp.next =lists[listHead[0][1]]
        return listNode.next
