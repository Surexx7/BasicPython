weight=float(input("Enter the weight: "))
height=float(input("Enter the height: "))
bmi=round(weight/height**2)

if(bmi<=18):
  print(f"Your BMI is {bmi} and you are under age")
elif(bmi<=25):
   print(f"Your BMI is {bmi} and you are Normal age")
elif(bmi<=30):
   print(f"Your BMI is {bmi} and your are Over weight")
elif(bmi<=35):
    print(f"Your BMI is {bmi} and you are Obese" )
else:
    print(f"Your BMI is {bmi} and you are clinacally Obsue")
