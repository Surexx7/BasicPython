#print 1 to 100
# if divisible by 3 -> Fizz
#if divisible by 5 -> Buzz
#if divisible by 3 and 5 -> FizzBuzz


num=range(1,101,1)
for i in num:
    if (i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz")
    elif (i%3)==0:
        print("Fizz")
    elif(i%5)==0:
        print("Buzz")
    else:
        print(i)
