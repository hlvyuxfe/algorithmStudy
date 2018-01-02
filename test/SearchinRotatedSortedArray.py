#Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#You are given a target value to search. If found in the array return its index, otherwise return -1.
#You may assume no duplicate exists in the array.
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==0:
            return -1
        pivotPoint =0
        while pivotPoint+1<len(nums) and nums[pivotPoint] < nums[pivotPoint+1]:
            pivotPoint+=1
        if pivotPoint==len(nums)-1:
            return searchinInterval(nums,0,pivotPoint,target)
        elif target< nums[0]:
            return searchinInterval(nums,pivotPoint+1,len(nums)-1,target)
        else:
            return searchinInterval(nums,0,pivotPoint,target)

def searchinInterval(nums,start,end,target):
    if start>end:
        return -1
    if target<nums[(start+end)//2]:
        return searchinInterval(nums,start,(start+end)//2-1,target)
    elif target > nums[(start+end)//2]:
        return searchinInterval(nums,(start+end)//2+1,end,target)
    else:
        return (start+end)//2


