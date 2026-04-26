# Problem 8: Sort students by score and find top scorer
n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append((name, int(score)))
pass_mark = int(input())
students.sort(key=lambda x: (-x[1], x[0]))
print(' '.join(student[0] for student in students))
print(sum(1 for _, score in students if score >= pass_mark))
print(students[0][0] if students else "No students")