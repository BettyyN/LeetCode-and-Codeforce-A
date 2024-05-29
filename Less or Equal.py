n, k = map(int, input().split())
sequence = list(map(int, input().split()))
sequence.sort()

left = 1
right = 10**9

while left <= right:
    mid = (left + right) // 2
    count = 0
    
    for num in sequence:
        if num <= mid:
            count += 1
    
    if count <= k:
        left = mid + 1
    else:
        right = mid - 1

if right > 0:
    print(right)
else:
    print(-1)
