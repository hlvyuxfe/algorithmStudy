class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        value = start = negaFlag=0
        while str[start] == ' 'or str[start] == '\t':
            start +=1
        if str[start]=='+':
            start+=1
        elif str[start]=='-':
            negaFlag=1
            start+=1
        elif str[start]<'0' and str[start]>'9':
            return 0
        while start<len(str) and str[start]>='0'and str[start]<='9':
            value=value*10+int(str[start])
            start+=1
        value =value if negaFlag==0 else -value
        if value>0x7FFFFFFF:
            value=0x7FFFFFFF
        if value < -0x80000000:
            value = -0x80000000
        return value
