import random

name=input("Enter the list of names seperated by commas: ")
splited_name=name.split(",")
print(f"The list of names are: {splited_name}")
# list=random.choice(splited_name)
# print(f"{list} will pay the bill...")

length=len(splited_name)
random_choice=random.randint(0, length-1)
print(splited_name[random_choice])


