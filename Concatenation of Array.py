class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        n=len(nums)
        x=1
        while x<=2:
            for num in nums:
                ans.append(num)
            x+=1;
        return ans 
