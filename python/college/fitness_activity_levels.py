# Problem 1: Categorize clients by daily step counts
def categorize_steps(steps):
    levels = {'Athlete': 0, 'Very Active': 0, 'Active': 0, 'Moderate': 0, 'Low': 0, 'Inactive': 0}
    for step in steps:
        if step >= 15000:
            levels['Athlete'] += 1
        elif 10000 <= step <= 14999:
            levels['Very Active'] += 1
        elif 7000 <= step <= 9999:
            levels['Active'] += 1
        elif 5000 <= step <= 6999:
            levels['Moderate'] += 1
        elif 1 <= step <= 4999:
            levels['Low'] += 1
        else:
            levels['Inactive'] += 1
            
    for level, count in levels.items():
        print(f"{level} = {count}")

steps = list(map(int, input().split()))
categorize_steps(steps)