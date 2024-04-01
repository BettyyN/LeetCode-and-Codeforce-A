class Solution:
    def similarPairs(self, words: List[str]) -> int:
        number_of_pair=0
        n=len(words)
        for i in range(n):
            for j in range(i+1,n):
                if set(words[i])==set(words[j]):
                     number_of_pair+=1
        return  number_of_pair
