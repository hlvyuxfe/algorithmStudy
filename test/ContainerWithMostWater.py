class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i,j = 0,len(height)-1
        maxv = min(height[i],height[j])*j
        while i<j:
            temp=1
            if height[i]<height[j]:
                 while i+temp<j and height[i+temp]<=height[i]:
                     temp+=1
                 i+=temp
            else:
                 while j-temp>i and height[j-temp]<=height[j]:
                     temp+=1
                 j-=temp
            maxv = maxv if min(height[i],height[j])*(j-i) <=maxv else min(height[i],height[j])*(j-i)
        return maxv
