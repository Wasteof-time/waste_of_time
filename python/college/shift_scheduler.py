# Problem 10: Schedule employees for morning and evening shifts
names = [name.strip() for name in input().split(',')]
for i in range(0, len(names), 2):
    print(names[i])
for i in range(1, len(names), 2):
    print(names[i])