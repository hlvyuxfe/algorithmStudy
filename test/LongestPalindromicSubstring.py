class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        resultTable = [None]*len(s)
        for i in range(len(s)):
            resultTable[i]=[None]*len(s)
        longest,start,end = 1,0,0
        for j in range(len(s)):#按从左向右，从下向上
            for i in range(j,-1,-1):#从j到0,i<=j
                if i ==j:
                    resultTable[i][j] = 1
                elif s[i]==s[j]:
                    if i+1==j:
                        resultTable[i][j]=2
                    else:
                        resultTable[i][j]=resultTable[i+1][j-1]+2 if resultTable[i+1][j-1]!=-1 else -1#-1 非回文子串
                    if resultTable[i][j]>longest:
                        longest,start,end= resultTable[i][j],i,j
                else:
                    resultTable[i][j] = -1
        return s[start:end+1]