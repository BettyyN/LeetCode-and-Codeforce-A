class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size=len(nums)
        prefixpro={0:1}
        suffixpro={size-1:1}
        ans=[]
        for i in range(size-1):
            prefixpro[i+1]=prefixpro[i]*nums[i]
        for i in range(size-1,0,-1):
            suffixpro[i-1]=suffixpro[i]*nums[i]
        for i in range(size):
            ans.append(prefixpro[i]*suffixpro[i])
        return ans
            
            
        
