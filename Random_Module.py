import random
#a=random.randint(1,3) //both 1 and 3 are included

#a=random.randrange(1,6)  #1 is included but not 6

a=random.uniform(1,4)

#Dice
list=[1,2,3,4,5,6]
a=random.choice(list)
print(a)


l=[2,-5,66,5,7,10]
random.shuffle(l)
print(l)

