class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix={0:1}
        sums=0
        res=0
        for i in nums:
            sums += i
            nums=sums-k
            if nums in prefix:
                res+=prefix[nums]
            prefix[sums]=1+prefix.get(sums,0)
        return res
        
