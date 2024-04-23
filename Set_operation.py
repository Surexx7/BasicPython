set1={1,2,3,4,5}
set2={4,5,6,7,8,9}
set3={9,10,11,12}

#union
union= set1.union(set2)
print(union)

union1= set1|set2
print(union1)

union3= set1.union(set2,set3)  #we can pass touple also ie set1.union((12,6,8))

#OR
union4= set1|set2|set3

#set1.update(set2)


#intersection
inter= set1.intersection(set2)
print(inter)
print(set1 & set2 & set3)
print(set1.intersection_update(set2))

#difference
print(set1.difference(set3))  #we can pass touple
print(set1-set2)

#Symmetric difference
#-> It prints the value of both set but will not print the repeated value in both set
print(set1.symmetric_difference(set2))

