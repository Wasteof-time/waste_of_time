# Problem 2: Calculate total shipping cost
n = int(input())
total_cost = 0.0
for _ in range(n):
    weight, rate_per_kg = map(float, input().split())
    total_cost += weight * rate_per_kg
print(f"{total_cost:.2f}")