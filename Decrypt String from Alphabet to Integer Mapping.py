class Solution:
    def freqAlphabets(self, s: str) -> str:
        lowercase = []
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                char_code = int(s[i:i + 2])
                i += 3  
            else:
                char_code = int(s[i])
                i += 1
            lowercase.append(string.ascii_lowercase[char_code - 1])
        return ''.join(lowercase)
                
                
                
        
