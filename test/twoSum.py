class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict={}
        for index,item in enumerate(nums):
            dict[item]=index
        for index,item in enumerate(nums):
            if target-item in dict and index!=dict[target-item]:
                return [index,dict[target-item]]
