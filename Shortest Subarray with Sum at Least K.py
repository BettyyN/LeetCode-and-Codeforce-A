class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefixSum = [0]
        for num in nums:
            prefixSum.append(prefixSum[-1] + num)        
        answer = len(nums) + 1  
        queue = deque()        
        for i, summ in enumerate(prefixSum):
            while queue and summ - prefixSum[queue[0]] >= k:
                answer = min(answer, i - queue.popleft())
            while queue and summ <= prefixSum[queue[-1]]:
                queue.pop()
            queue.append(i)        
        if answer <= len(nums):  
            return answer
        return -1
