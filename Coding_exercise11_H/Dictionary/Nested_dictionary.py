#dictionary within a dictionary is called nested dictionary

student_data={
    "Ram":{"roll_no":10, "age":20, "course":"Python"},
    "Mohan":{"roll_no": 2 , "age" :22, "course": "Java"}
}
print(student_data["Mohan"])
print(student_data["Mohan"]["roll_no"])
student_data["Mohan"]["phone_no"]=9854
print(student_data["Mohan"])
del student_data["Mohan"]["phone_no"]
print(student_data["Mohan"])
print(student_data["Mohan"].pop("course"))
print(student_data["Mohan"])


#nesting a list in dictionary
travel_data={
    "Gujrat":["Dwarkadhish", "Somnath"," Statue of unity"],
    "Kathmandu":["Pashupatinath" "Patan", "Teaxs"]
}
print(travel_data)

#dictionary within a list

student_data=[
    {"Name": "Ram",
     "roll_no":10,
     "age":20,
     "course":["Python", "java"]
     },
    {
        "Name": "Mohan",  "roll_no": 2 , "age" :22, "course": "Java"}
]
print(student_data)
print(student_data[0])

