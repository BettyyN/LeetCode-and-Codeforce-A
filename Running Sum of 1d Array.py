class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        runningsum=[]
        x=0
        for num in nums:
            x+=num
            runningsum.append(x);
        return runningsum
