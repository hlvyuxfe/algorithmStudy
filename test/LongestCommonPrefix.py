class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if (not len(strs))or(not len(strs[0])):
            return ''
        long=1
        while long<=len(strs[0]):
            for i in strs:
                if not(i.startswith(strs[0][0:long])):
                    return strs[0][0:long-1]
            long+=1
        return strs[0]
