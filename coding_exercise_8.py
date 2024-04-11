size=input("Enter the size of pizza (S/M/L): ")
bill=0
if (size=="S" or size== "s"):
    bill=100
    print("The price of small pizza is 100")
elif(size=="M" or size=="m"):
    bill=200
    print("The price of medium pizza is 200")
elif(size=="L" or size=="l"):
    bill=300
    print("The price of large pizza is 300")
else:
    print("Invalid Input")
    exit()
pepperon=str(input("Do you want to add pepperon(Y/N): "))
if (pepperon=="Y" or pepperon=="y" and size=="s" or pepperon=="S"):
    bill=bill+30
elif (pepperon=="y" or pepperon=="Y" and size=="m" or size=="M" ):
    bill=bill+50
elif(pepperon=="y" or pepperon=="Y" and size=="l" or size=="L"):
     bill=bill+50
elif(pepperon=="n" or pepperon=="N"):
    bill=bill+0
else:
    print("Invalid input")
exit()
#print(f"Your total bill is {bill}")

cheese=str(input("Do you want extra cheese?[Y/N]: "))
if (cheese=="Y" or cheese=="y"):
    bill=bill+20
    print(f"The total bill is {bill}")
else:
    bill=bill+0
    print(f"The final bill is {bill}")


