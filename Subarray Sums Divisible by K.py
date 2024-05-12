class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:        
        count = 0
        prefix_sum_remainder = {0: 1}
        prefix_sum = 0
        for num in nums:
            prefix_sum = (prefix_sum + num) % k
            prefix_sum = (prefix_sum + k) % k
            count += prefix_sum_remainder.get(prefix_sum, 0)
            prefix_sum_remainder[prefix_sum] = prefix_sum_remainder.get(prefix_sum, 0) + 1
        return count
        
