student_data=[
    {"Name": "Ram",
     "roll_no":10,
     "age":20,
     "course":["Python", "java"]
     },
    {
        "Name": "Mohan",
        "roll_no": 2 ,
        "age" :22,
        "course": "Java"
    }
]

def add_new_student(name, roll_no, age,course):
    new_student={}
    new_student["Name"]=name
    new_student["roll_no"]=roll_no
    new_student["Age"]=age
    new_student["course"]=course
    student_data.append(new_student)
add_new_student("Shyam", 22, 18, "C++")
print(student_data)