class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = []
        i=j=0
        while i <len(nums1) and j <len(nums2):
            if nums1[i]<nums2[j]:
                nums3.append(nums1[i])
                i+=1
            else:
                nums3.append(nums2[j])
                j+=1
        nums3.extend(nums1[i:]) if i!=len(nums1) else nums3.extend(nums2[j:])
        return nums3[(len(nums1)+len(nums2))//2] if (len(nums1)+len(nums2))%2 ==1 else \
    (nums3[(len(nums1)+len(nums2))//2]+nums3[(len(nums1)+len(nums2))//2-1])/2
