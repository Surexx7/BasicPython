#while condition:
    #statement(s)


count=1
while count<=5:
    print(count)
    count = count + 1
print("Out from Loop")


count=1
while count<=5:
    print(count)
    count +=1
    if count==3:
        break
else:
    print("In else block")

print("out of loop")



