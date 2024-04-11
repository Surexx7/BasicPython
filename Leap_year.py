year= int(input("Enter the year: "))
if (year%4!=0):
    print(f"Year {year} is not a leap year...")
else:
    if (year%100!=0):
        print(f"Year {year} is a leap year...")
    else:
        if(year%400==0):
            print(f"Year {year} is a leap year...")
        else:
            print(f"Year {year} is not a leap year... ")



