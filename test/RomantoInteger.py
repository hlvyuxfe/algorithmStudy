class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        r=0
        last=0
        for i in s[::-1]:
            temp =table[i]
            if temp < last:
                r = r - temp
            else:
                r = r + temp
            last = temp
        return r
