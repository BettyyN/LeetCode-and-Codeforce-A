n,k=list(map(int, input().split()))
nums=list(map(int, input().split()))
nums=sorted(nums)
are_equal = all(nums[i] == nums[0] for i in range(1, k ))
if nums[k-1]==nums[k]:
    print(-1)
elif are_equal and nums[k-1]!=nums[k]:
    print(nums[k-1])
else:
    a=nums[k-1]+1
    print(a)
