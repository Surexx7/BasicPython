numbers=[10,0,-1,7,6,90,-67,100,45,45]
names=["Suresh Shahi", "Krishna", "Ram"]
mix_list=[1, "suresh", True, 10.10]
print(numbers)
print(names)
print(mix_list)
print(numbers[2])
print(names[2])
print(len(numbers))
print(numbers[-1])

#Slicing

print(numbers[0:2])
print(numbers[:5])
print(numbers[4:])
print(numbers[0:5:2])
print(numbers[0:7:3])
print(numbers[0::3])


numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

print(min(numbers))
print(max(numbers))


num1=[12,23,45,67]
print("Before appending:",num1)
num1.append(15)
print("After appending:",num1)

num1.insert(1,15)
print(num1)

num1.extend(numbers)
print(num1)

n1=[1,2,3,4,5]
n1.extend([6,7])
print(n1)

#Replacing the numbers

n1[1]=55
print(n1)

n1[1:4]=55,56,57
print(n1)

#removing
n2=[1,2,3,4,5,6,7,8,9,10,8,8]
n2.remove(2)
print(n2)
n2.pop(1)
print(n2)

print(n2.count(8))




