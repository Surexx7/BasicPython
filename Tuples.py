#Tuple are immutable
tuple1=(10, 1, -10, 15, 20, 'Suresh', True, 10,10, 12, 10)
print(tuple1)

#slicing
print(tuple1[1:4])
print(tuple1[::2])

#Nested tuples

tuple2=( 5, 90, 56)
tuple3=(tuple1, tuple2)
print(tuple3)
tuple3=tuple1 + tuple2
print(tuple3)

print(min(tuple2))

print(tuple1.count(10))


#Converting List into tuples

list1=[1,3,4,5,67,5]
print(tuple(list1))

print(list(tuple1))

tuple5=(10,4)*5
print(tuple5)







