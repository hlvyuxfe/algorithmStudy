class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            isNegative =1 
            x=-x
        else:
             isNegative =0 
        q =[]
        while x:
            q.append(x%10)
            x=x//10
        result=0
        for i in q:
            result =result*10+i
        if result>2147483647 or result<-2147483648:
            result=0
        return -result if isNegative else result
