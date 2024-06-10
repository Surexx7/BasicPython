# in for else loop else is executed only if for loop is executed sucessufully or compeletly.

tuple1=(1, 34, 3, 56, 5)
for i in tuple1:
    print(i)
else:
    print("Sucessfully completed")



tuple1=(1, 34, 3, 56, 5)
for i in tuple1:
    print(i)
    if i==56:
        break
else:
    print("Sucessfully completed")
print("Out of for/else")