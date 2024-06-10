#Program to calculate average height from a list of heights

heights=input("Enters the heights seperated by space: ")
splited_height=heights.split()
count=0
for height in splited_height:
    count=count+1
print(count)
for i in range(count):
    splited_height[i]=int(splited_height[i])
print(splited_height)

sum=0
for j in splited_height:
    sum=sum+j
print("The average height is:",sum/count)





