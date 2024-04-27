class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1        
        res = 0
        start = 0
        counter = {}
        for i in range(len(s)):           
            if s[i] not in counter:
                counter[s[i]] = i
            else:
                res = max(res, i - start)
                start = max(start, counter[s[i]] + 1)
                counter[s[i]] = i
        res = max(res, len(s) - start)
        
        return res
