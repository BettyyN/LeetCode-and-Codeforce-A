class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        MOD = 10**9 + 7
        n = len(arr)
        
        # Arrays to store the indices of previous and next smaller elements
        prev_smaller = [-1] * n
        next_smaller = [n] * n
        
        # Monotonic stack to find previous smaller elements
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                prev_smaller[i] = stack[-1]
            stack.append(i)
        
        # Monotonic stack to find next smaller elements
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                next_smaller[stack.pop()] = i
            stack.append(i)
        
        # Calculate the sum of minimums of all subarrays
        result = 0
        for i in range(n):
            left_count = i - prev_smaller[i]
            right_count = next_smaller[i] - i
            result = (result + arr[i] * left_count * right_count) % MOD
        
        return result;
        
