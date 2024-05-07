class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastoccurance={}
        a=[]
        start=0
        end=0
        for i in range(len(s)):
            lastoccurance[s[i]]=i
        while start < len(s):
            end = lastoccurance[s[start]]
            current = start
            while current < end:
                end = max(end, lastoccurance[s[current]])
                current += 1
            a.append(end-start+1)
            start=end+1
        return a
        
