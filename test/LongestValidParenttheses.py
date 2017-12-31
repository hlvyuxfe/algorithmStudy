#Given a string containing just the characters '(' and ')', 
#find the length of the longest valid (well-formed) parentheses substring.
#For "(()", the longest valid parentheses substring is "()", which has length = 2.
#Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        PositionLongthDict = {}
        stack = []
        for index,parenthese in enumerate(s):
            if parenthese=='(':
                stack.append(index)
            else:
                if len(stack)!=0:
                    start = stack.pop()
                    longth = index-start+1
                    if start-1 in PositionLongthDict:
                        PositionLongthDict[index] = PositionLongthDict[start-1]+longth
                    else:
                        PositionLongthDict[index] = +longth
        if len(PositionLongthDict)>0:
            return sorted(PositionLongthDict.items(), key=lambda d:d[1], reverse = True)[0][1]
        else:
            return 0