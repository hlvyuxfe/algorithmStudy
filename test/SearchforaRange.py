#Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.
#Your algorithm's runtime complexity must be in the order of O(log n).
#If the target is not found in the array, return [-1, -1].
#For example,
#Given [5, 7, 7, 8, 8, 10] and target value 8,
#return [3, 4].
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]
        #search for start
        left,right = 0,len(nums) - 1
        while left<right:
            mid = left+((right-left)>>1)
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid]<target:
                left = mid + 1
            else:
                right = mid
        if left==right and nums[left]==target:
            start = left
        else:
            return [-1,-1]
        #search for end
        left , right = start,len(nums) - 1
        while left < right:
            mid = left + ((right-left+1) >> 1)
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                left = mid
        end = left
        return [start, end]

        