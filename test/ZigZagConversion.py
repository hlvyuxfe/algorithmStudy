class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows ==1:
            return s
        temp=[None]*numRows
        for i in range(numRows):
            temp[i]=[]
        delta =1
        num=0
        for i in range(len(s)):
            temp[num].append(s[i])
            if num ==0:
                delta =1
            elif num ==numRows-1:
                delta =-1
            num =num+delta
        for i in range(numRows):
            temp[i] = ''.join(temp[i])
        return ''.join(temp)
