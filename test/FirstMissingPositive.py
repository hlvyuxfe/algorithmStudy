#Given an unsorted integer array, find the first missing positive integer.
#For example,
#Given [1,2,0] return 3,
#and [3,4,-1,1] return 2.
#Your algorithm should run in O(n) time and uses constant space.
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = len(nums)
        for i in range(k):
            while(nums[i] > 0 and nums[i]!=i+1 and nums[i] < k+1):
                if nums[i] == nums[nums[i] - 1]:
                    break
                temp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp
        for i in range(k):
            if nums[i] != i+1:
                return i+1
        return k+1
