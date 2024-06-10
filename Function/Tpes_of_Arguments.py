def greet(name,depart):
    print(f"Hi {name}")
    print(f"Are you from {depart} department?\n ")

#i.Position argument
greet("Suresh", "Csit")

#ii. Keyword argument

greet(name="suresh", depart="Csit")
greet(depart="csit", name="Suresh")


#iii. Default argument

def greet1(name, dept="BCA"):
    print(f"Hi { name}")
    print(f"Are you from {dept} department?")
greet1("suresh")

#Note= Always default argument should follow non-default argument


#IV.  Arbitarory Argument

def add (*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print(f"Sum is {sum}")
add(3,5,10,20)

