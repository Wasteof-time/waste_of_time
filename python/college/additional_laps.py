# Problem 4: Calculate additional ideal laps
speed = int(input())
laps_completed = int(input())
remaining_time = int(input())
additional_laps = (speed * remaining_time) - laps_completed
print(f"{max(0.0, additional_laps):.1f}")