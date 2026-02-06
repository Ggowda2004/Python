#sets are mutable,unordered(no indexing or slicing), dynamic collections of unique elements(no duplicates allowed)
#elements must be immutable types (string, number, tuple), set itself is mutable

set0=set()  #empty set
set1={1,2,3,4,5}  #set with initial elements

# set comprehension
set_c={x for x in range(10) if x%2==0}  #set comprehension Set_c: {0, 2, 4, 6, 8}

print('-------------------------------------')
set1.add(6)  #adds element 6 to the set
set1.update([7,8,9])  #adds multiple elements to the set
set1.remove(3)  #removes element 3, raises KeyError if not found, **pop and clear** methods also available
set1.discard(10)  #removes element 10 if present, does nothing if not found
print("set1 after add/remove/discard:", set1)
print('-------------------------------------')

#lookup time in sets is O(1) on average
if 4 in set1:
    print("4 is present in set1")

print('-------------------------------------')

#set operations all return new sets
a={1,2,3,4}
b={3,4,5,6}
print("union:",a|b)
print("intersection:",a&b) #elements common to both sets
print("difference (a-b):",a-b)
print("symmetric difference:",a^b)#elements in a or b but not both

print('-------------------------------------')
#checks
c={1,2,3,4,5}
d={1,2,3}
print("c is superset of d:", c.issuperset(d))  #True
print("d is subset of c:", d.issubset(c))      #True
print("c and d are disjoint:", c.isdisjoint(d)) #False, as they have common elements

print('-------------------------------------')

#copying sets is done using .copy() method to create a shallow copy

#frozenset is an immutable version of set, elements cannot be added or removed after creation
fs=frozenset([1,2,3,4,5])

#end