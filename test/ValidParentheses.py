class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        table={')':'(',']':'[','}':'{'}
        for i in s:
            if i in ('(','[','{'):
                stack.append(i)
            elif(len(stack)==0):
                return False
            elif(stack[-1] == table[i]):
                stack.pop()
            else:
                return False
        if not(stack):
            return True
        else:
            return False
