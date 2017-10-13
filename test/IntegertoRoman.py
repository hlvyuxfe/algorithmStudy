class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        table=[['I','V'],['X','L'],['C','D'],['M']]
        roman=['','','','']
        i=0
        while num>0:
            temp = num%10
            if temp < 4:
                roman[3-i] = table[i][0]*temp
            elif temp==4:
                roman[3-i] = table[i][0]+table[i][1]
            elif temp < 9:
                roman[3-i] = table[i][1]+table[i][0]*(temp-5)
            else:
                roman[3-i] = table[i][0]+table[i+1][0]
            num = num//10
            i+=1
        return ''.join(roman)