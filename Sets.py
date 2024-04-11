#List cannot have duplicate data
#Sets data are unorder
#Indexing is not allowed in sets because sets items are unordered
#Items cannot be changed but can be removed or inserted.

set1={10, 56, 89, 90, "Suresh", True}
print(set1)

#creating empty sets
set2=set()
print(type(set2))

#Adding new Elements in sets

set1.add(100)
print(set1)

set1.remove(89)
print(set1)
print(set1.pop())
set1.add((1,2,3))
print(set1)

set1.clear()
print(set1)

