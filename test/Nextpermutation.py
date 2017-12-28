#Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
#The replacement must be in-place, do not allocate extra memory.
#Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
#1,2,3 → 1,3,2
#3,2,1 → 1,2,3
#1,1,5 → 1,5,1
class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1:
            return
        i = len(nums)-1
        while i!=0 and nums[i] <= nums[i-1]:
            i-=1
        if i==0:
            nums.sort()
            return
        insertPoint = i-1
        insertValue = nums[insertPoint]
        while i<len(nums) and nums[i] > insertValue:
            i+=1
        breakPoint = i-1
        nums[insertPoint] = nums[breakPoint]
        nums[breakPoint] = insertValue
        i , j = insertPoint+1,len(nums)-1
        while i<j:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i,j = i+1,j-1
        return 