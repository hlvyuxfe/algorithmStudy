#Implement strStr().
#Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack==needle:
            return 0
        if not needle:
            return 0
        length = len(haystack)
        i=0
        while i<length and len(needle)<=len(haystack[i:]):
            if haystack[i]==needle[0]:
                j=1
                while j<len(needle) and haystack[i+j] == needle[j]:
                    j+=1
                if j==len(needle):
                    return i
            i+=1
        return -1
        