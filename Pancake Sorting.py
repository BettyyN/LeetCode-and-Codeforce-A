class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result=[]
        size=len(arr)
        for i in range(size):
                maxV=max(arr[:size-i])
                index_max=arr.index(maxV)+1
                arr[:index_max]=reversed(arr[:index_max])
                result.append(index_max)
                arr[:size-i]=reversed(arr[:size-i])
                result.append(size-i)
        return result
            
            
        
        
        
