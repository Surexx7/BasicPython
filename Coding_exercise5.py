#To find out many many days, weeks, months, we left if we live until 90 years old.
#assumptions:
#1 years= 365 days
#1 years= 52 weeks
#1 year= 12 months

age=int(input("Enter your current age: "))
left_age=90-age
a=left_age*356
b=left_age*52
c=left_age*12
print(f"You have {a} days, {b} weeks and {c} months left")

