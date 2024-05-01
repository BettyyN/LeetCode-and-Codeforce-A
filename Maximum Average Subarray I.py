class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sums=sum(nums[:k])
        avg=sums/k
        for i in range(k,len(nums)):
            sums=sums+nums[i]-nums[i-k]
            avvg=sums/k
            avg=max(avg,avvg)
        return avg
       
        
        
