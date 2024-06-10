#program to find maximum number from a set of numbers.

numbers= input("Enter the numbers using space: ")
splited_number=numbers.split()
count =0
for num in splited_number:
    count=count+ 1
for i in range(count):
    splited_number[i]=int(splited_number[i])

max_number=splited_number[0]
for i in splited_number:
    if i>max_number:
        max_number=i
print("The maximum number from the list is: ", max_number)
