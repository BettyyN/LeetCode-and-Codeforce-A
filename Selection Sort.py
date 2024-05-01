
class Solution: 
    def select(self, arr, i):
        mini = arr[i]
        for j in range(i+1, n):
            if arr[j] < mini:
                mini = j
        return mini
        # code here 
    def selectionSort(self, arr,n):
        for i in range(n):
            minindex=self.select(i,arr)
            arr[i], arr[minindex] = arr[minindex], arr[i]
        return arr
