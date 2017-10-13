class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        table={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        if len(digits)==0:
            return []
        result=['']
        for i in xrange(len(digits)):
            for j in result:
                if len(j) == i:
                    for z in table[digits[i]]:
                        result.append(j+z)
        return [i for i in result if len(i)==len(digits)]
