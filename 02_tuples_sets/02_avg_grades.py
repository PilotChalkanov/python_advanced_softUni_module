import math
n = int(input())

student_list = {}
students = []
def avarage_grade(grades):
    grades = [float(grade) for grade in grades]
    avg_grade = sum(grades)/len(grades)
    return avg_grade

for _ in range(n):
    name,grade = input().split()
    if name in student_list.keys():
        student_list[name].append(grade)
    else:
        student_list[name] = []
        student_list[name].append(grade)

for k,v in student_list.items():
    print(f"{k} -> {' '.join(v)} (avg: {avarage_grade(v):.2f})")



