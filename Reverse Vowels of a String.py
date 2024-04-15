class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel=set("aeiouAEIOU")
        string_=list(s)
        size=len(string_)
        left=0
        right=size-1
        while left<right:
            if string_[left] in vowel and string_[right] in vowel:
                string_[left],string_[right]=string_[right],string_[left]
                left+=1
                right-=1
            elif string_[right] not in vowel:
                right-=1
            elif string_[left] not in vowel:
                left+=1
        return ''.join(string_)
        
