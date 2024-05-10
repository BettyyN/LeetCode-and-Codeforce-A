n,m=map(int,input().split())
arr1=list(map(int, input().split()))
arr2=list(map(int, input().split()))
count=0
ans=[]
for i in range(len(arr2)):
    while count<len(arr1) and arr2[i]>arr1[count]:
        count+=1
    ans.append(count)
print(*ans)
