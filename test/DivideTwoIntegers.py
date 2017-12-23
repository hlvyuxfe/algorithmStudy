#Divide two integers without using multiplication, division and mod operator.
#If it is overflow, return MAX_INT.
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        remainder,quotient=0,0
        if divisor==0:
            return (1<<31)-1
        if (dividend>0 and divisor>0) or (dividend<0 and divisor<0):
            flag = 1
        else:
            flag = 0
        dividend,divisor = abs(dividend),abs(divisor)
        for bit in range(31,-1,-1):
            temp =(1<<bit &dividend)>>bit
            remainder = (remainder<<1)+temp
            if remainder>=divisor:
               quotient+= 1<<bit
               remainder -= divisor
        if not flag:
            quotient=-quotient
        if quotient>(1<<31)-1 or quotient<-(1<<31):
            return (1<<31)-1
        return quotient
