class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result=[]
        for i in range(len(nums)-3):
            if i==0 or nums[i]!=nums[i-1]:
                for j in range(i+1,len(nums)-2):
                    if nums[j]!=nums[j-1] or j==i+1:
                        newtarget = target - nums[i]-nums[j]
                        l,r=j+1,len(nums)-1
                        while l<r:
                            if newtarget-nums[l]-nums[r]==0:
                                result.append([nums[i],nums[j],nums[l],nums[r]])
                                l+=1
                                r-=1
                                while l<r and nums[l] == nums[l-1]:
                                    l+=1
                                while l<r and nums[r] ==nums[r+1]:
                                    r-=1
                            elif newtarget-nums[l]-nums[r]>0:
                                l+=1
                            else:
                                r-=1
        return result

