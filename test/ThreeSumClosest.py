class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        if nums[-1]+nums[-2]+nums[-3]<=target:
            return nums[-1]+nums[-2]+nums[-3]
        elif nums[0]+nums[1]+nums[2]>=target:
            return nums[0]+nums[1]+nums[2]
        closest={}
        for i in xrange(len(nums)-2):
            newtarget = target-nums[i]
            if nums[-1]+nums[-2]<newtarget:
                closest[abs(newtarget-nums[-1]-nums[-2])]=nums[-1]+nums[-2]+nums[i]
                continue
            elif nums[i+1]+nums[i+2]>newtarget:
                closest[abs(newtarget-nums[i+1]-nums[i+2])]=nums[i+1]+nums[i+2]+nums[i]
                continue
            elif nums[-1]+nums[-2]==newtarget or nums[i+1]+nums[i+2]==newtarget:
                return target
            l,r=i+1,len(nums)-1
            thisclosest=(abs(newtarget-nums[l]-nums[r]),nums[i]+nums[l]+nums[r])
            while l<r:
                if nums[l]+nums[r]>newtarget:
                    while nums[l]+nums[r]>newtarget:
                        r-=1
                    delta = abs(newtarget-nums[l]-nums[r+1])
                    if delta<thisclosest[0]:
                        thisclosest=(delta,nums[i]+nums[l]+nums[r+1]) 
                elif nums[l]+nums[r]<newtarget:
                    while nums[l]+nums[r]<newtarget:
                        l+=1
                    delta = abs(newtarget-nums[l-1]-nums[r])
                    if delta<thisclosest[0]:
                        thisclosest=(delta,nums[i]+nums[l-1]+nums[r]) 
                else:
                    #print(nums[i],nums[l],nums[r])
                    return target
            closest[thisclosest[0]]=thisclosest[1]
        return closest[min(closest.keys())]
        
