def max_alternating_sum(t, test_cases):
    results = []
    for i in range(t):
        n = test_cases[i][0]
        a = test_cases[i][1]
        
        max_sum = 0
        current_max = a[0]
        
        for j in range(1, n):
            if (a[j] > 0 and current_max > 0) or (a[j] < 0 and current_max < 0):
                current_max = max(current_max, a[j])
            else:
                max_sum += current_max
                current_max = a[j]
        
        max_sum += current_max
        results.append(max_sum)
    
    return results

t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

results = max_alternating_sum(t, test_cases)
for result in results:
    print(result)
