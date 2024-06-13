student_marks={
    "Suresh":92,
    "Harry":78,
    "Shanti": 56,
    "Bhabi": 41,
    "Lokesh": 99,
    "Ram": 34
}
student_grades={}
for student in student_marks:
    marks=student_marks[student]
    if marks >90:
        student_grades[student]="A+"
    elif marks>80:
        student_grades[student]="A"
    elif marks>70:
        student_grades[student]="B+"
    elif marks>60:
        student_grades[student]="B"
    elif marks>50:
        student_grades[student]="c+"
    else:
        student_grades[student]="Fail"

print(student_grades)


