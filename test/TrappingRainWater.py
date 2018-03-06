#Given n non-negative integers representing an elevation map where the width of each bar is 1, 
#compute how much water it is able to trap after raining.
#For example, 
#Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
#The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
#In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water = 0
        left, right = 0,len(height)-1
        while (left<right):
            top  = height[left] if height[left] < height[right] else height[right]
            if height[left] < height[right]:
                while(left < right and height[left] <= top):
                    water  = water + top - height[left]
                    left += 1
            else:
                while(right > left and height[right] <= top):
                    water  = water + top - height[right]
                    right -= 1
        return water

                

            