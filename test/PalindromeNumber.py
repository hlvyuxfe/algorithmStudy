class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        if x<0 or x%10 == 0:
            return False
        r=0
        while(x):
            r = r*10+x%10
            if r == x:
                return True
            x = x//10
            if r == x:
                return True
        return False
