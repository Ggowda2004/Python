#Python tuples are ordered, immutable sequences used for fixed collections of data and safe data grouping. multiple values(even different data types) in a single variable, allow duplicate4
#slightly faster than lists for certain operations due to their immutability.

t1=(1, 2, 3, 4, 5)
t2=(1, "hello", 3.14, True)
t0=(1,)#single element tuple , is necessary

#Accessing elements(ordered)
print(t1[0])#1
print(t2[1])#"hello"

print("----------------------------------------")
#packing and unpacking
t3=1, 2, 3, 4, 5 #packing
a, b, c, d, e = t3 #unpacking
print(a, b, c, d, e)#1 2 3 4 5

a,*b=t3
print(a,b)#1 [2, 3, 4, 5]
print("----------------------------------------")

#Tuple methods
t4=(1, 2, 3, 2, 4, 2,3)
print(t4.count(2))#3
print(t4.index(3))#2

print("----------------------------------------")
#Immutability
#t4[0]=10 #TypeError: 'tuple' object does not support item

#However, we can concatenate tuples to create new ones
t5=t1 + t4

#extending tuples
t6=t1 + (6, 7, 8)

#end