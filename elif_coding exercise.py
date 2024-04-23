height=int(input("What is your height?"))
if (height>=3):
    print("You can ride...")
    age=int(input("What is your age?"))
    if (age <=12):
        print("Pay Rs 100")
    elif(age<=18):
        print("Pay Rs 300")
    else:
        print("pay rs 500")
else:
    print("You cannot ride")

print("Bye....")

