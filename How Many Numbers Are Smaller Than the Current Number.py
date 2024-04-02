class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        smallerNumCounter=[]
        
        for i in range(0,len(nums),1):
            count=0
            for j in range(0,len(nums),1):
                if j!=i and nums[j]<nums[i]:
                    count+=1
            smallerNumCounter.append(count)
            
        return smallerNumCounter
                
                
                
                
