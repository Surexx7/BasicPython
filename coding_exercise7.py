height=int(input("What is your height?"))
photo=50
if (height>=3):
    print("You can ride...")
    age=int(input("What is your age?"))
    if (age <=12):
        ans=int(input("Do you want to click picture: Press 1 for 'YES' and 2 for 'NO' "))
        if(ans==1):
            print("Pay Rs 100+50=",100+photo)
        else:
            print("Pay Rs 100")
    elif(age<=18):
        ans = int(input("Do you want to click picture: Press 1 for 'YES' and 2 for 'NO' "))
        if (ans == 1):
            print("Pay Rs 300+50= ", 300 + photo)
        else:
            print("Pay RS 300")
    else:
         ans = int(input("Do you want to click picture: Press 1 for 'YES' and 2 for 'NO' "))
         if (ans == 1):
            print("Pay Rs 500+50=", 500 + photo)
         else:
            print("Pay Rs 550")
else:
    print("You csnnot ride")

print("Bye....")

