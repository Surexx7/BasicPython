import statistics

def mean_median_mode(list1):
    return [statistics.mean(list1),statistics.median(list1),statistics.mode(list1)]

print(mean_median_mode([1,3,4,5,8,910]))


def mean_median_mode(list1):
    return statistics.mean(list1),statistics.median(list1),statistics.mode(list1)
print("Rnd of function")

a,b,c=(mean_median_mode([1,3,4,5,8,910]))
print(f"Mean is {a}\n median is {b}\n MOde is {c}")


#returning multiple return statement in single function

def add (a,b):
    if a==0 & b==0:
        return "You have entered zero for both variables"
    else:
        return a+b

var1=int(input("Enter the first number: "))
var2=int(input("Enter the second number: "))
print(add(var1,var2))




