import math


n=int(input("Enter a number: "))

def prime(number):
    is_prime=True
    if number==1:
        is_prime=False
    for i in range(2,math.ceil(number/2)+1):
        if number%i==0:
            is_prime=False
    if is_prime==True:
        print("It is prime number ")
    else:
        print("It is not a prime number")

prime(number=n)
