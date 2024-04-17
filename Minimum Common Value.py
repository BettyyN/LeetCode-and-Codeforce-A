class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        pntr1=0
        pntr2=0
        x=0
        while pntr1<len(nums1) and pntr2<len(nums2):
            if nums1[pntr1]==nums2[pntr2]:
                x=nums1[pntr1]
                break
            elif nums1[pntr1]<nums2[pntr2]:
                pntr1+=1
            else:
                pntr2+=1
        if x==0:
            x=-1
        return x
