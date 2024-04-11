print("\t\t\t\t\t\t\t\t\t\t\t\t\tLOVE CALCULATOR")

name1=str(input("Enter the name of boy: "))
name2=str(input("Enter the name of girl: "))
A=name1.lower()
B=name2.lower()
name=A+B
a=name.count("t")
b=name.count("r")
c=name.count("u")
d=name.count("e")
sum1=str(a+b+c+d)
a1=name.count("l")
b1=name.count("o")
c1=name.count("v")
d1=name.count("e")
sum2=str(a1+b1+c1+d1)
total1=(sum1+sum2)
total=int(total1)
if(total<10 or total>90):
    print("Your total love score is: ",total)
    print("You are orange and mango")
elif(total>=40 and total<=50):
    print("Your total love score is: ",total)
    print("WOW!! You can stay together...")
else:
    print("Your total love score is:",total)

