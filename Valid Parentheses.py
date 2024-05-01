class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        c={'(':')','{':'}','[':']'}
        for i in  range(len(s)):
            if s[i] in c.keys():
                stack.append(s[i])
            else:
                if not stack:
                    return False
                else:
                    cs=stack.pop()
                    if s[i]!=c[cs]:
                        return False
        return stack==[]
                        
                
