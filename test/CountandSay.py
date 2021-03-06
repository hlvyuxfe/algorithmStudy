#The count-and-say sequence is the sequence of integers with the first five terms as following:
#1.     1
#2.     11
#3.     21
#4.     1211
#5.     111221
#1 is read off as "one 1" or 11.
#11 is read off as "two 1s" or 21.
#21 is read off as "one 2, then one 1" or 1211.
#Given an integer n, generate the nth term of the count-and-say sequence.
#Note: Each term of the sequence of integers will be represented as a string.
#Example 1:
#Input: 1
#Output: "1"
#Example 2:
#Input: 4
#Output: "1211"
class Solution:
    dic = {1:"1"}
    maxnum =1
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n > self.maxnum:
            temp = self.maxnum
            while temp < n:
                sequence = ''
                lastSequence = self.dic[temp]
                lastchar,count = lastSequence[0],1
                for i in range(1,len(lastSequence)):
                    if lastSequence[i] == lastchar:
                        count +=1
                    else:
                        sequence = sequence+str(count)+str(lastchar)
                        lastchar,count = lastSequence[i],1
                sequence = sequence+str(count)+str(lastchar)
                self.dic[temp+1] = sequence
                temp +=1
        self.maxnum = n
        return self.dic[n]