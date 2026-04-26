# Problem 3: Find runner with lowest average time
n = int(input())
min_avg = float('inf')
min_index = 0
for i in range(n):
    times = list(map(int, input().split()))
    avg = sum(times) / len(times)
    if avg < min_avg:
        min_avg = avg
        min_index = i
print(min_index)