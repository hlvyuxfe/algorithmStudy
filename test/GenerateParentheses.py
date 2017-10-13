class Solution(object):
    table={0:{''},1:{'()'}}
    def addFromLast(self,n):
        self.table[n]=set()
        for i in self.table[n-1]:
            temp = list(i)
            for j in range(len(temp)):
                if temp[j]==')':
                    copy=temp[:]
                    copy.insert(j,'(')
                    copy.insert(j+1,')')
                    self.table[n].add(''.join(copy))
                    copy=temp[:]
                    copy.insert(j+1,'(')
                    copy.insert(j+2,')')
                    self.table[n].add(''.join(copy))

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n<=1:
            return list(self.table[n])
        temp =n
        while temp not in self.table:
            temp-=1
        while temp<n:
            temp+=1
            self.addFromLast(temp)
        return list(self.table[n])