class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=0
        long = len(s)
        maxLong = len(set(s))
        for i in range(long):
            if i+l>long:
                return l
            for j in range(i+l+1,i+maxLong+1 if long>i+maxLong else long+1):# 
                if len(set(s[i:j]))==j-i:#not repeating
                    if j-i >l:
                        l = j-i
                        #break
                else:
                    break
        return l
