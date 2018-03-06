#Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.
#Note:
#The length of both num1 and num2 is < 110.
#Both num1 and num2 contains only digits 0-9.
#Both num1 and num2 does not contain any leading zero.
#You must not use any built-in BigInteger library or convert the inputs to integer directly.
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        numa = [int(i) for i in num1[::-1]]#reverse
        numb = [int(i) for i in num2[::-1]]#reverse
        products = []#reverse product
        for i in numb:
            if i == 0:
                products.append([0])
            elif i==1:
                products.append(numa.copy())
            else:
                tempProduct, carry= [],0
                for j in numa:
                    pro = i * j +carry
                    pos = pro % 10
                    carry = pro//10
                    tempProduct.append(pos)
                if carry !=0:
                    tempProduct.append(carry)
                products.append(tempProduct)
        #print(products)
        result = products[0]
        for i in range(1,len(products)):
            carry = 0
            for j in range(0,len(products[i])):
                if i+j<len(result):
                    sum = result[i+j] + products[i][j] + carry
                    result[i+j] = sum%10
                    carry = sum //10
                else:
                    sum = products[i][j] + carry
                    result.append(sum % 10)
                    carry = sum // 10
            if carry !=0:
                result.append(carry)
        while len(result)>1 and result[-1]==0:
            result.pop()
        return ''.join([str(i) for i in result[::-1]])