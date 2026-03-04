#list is ordered(indexing, slicing) and mutable, dynamic size(increase in based on size *1.1 or ~1.5), list can contain duplicate elements , it stores reference to the objects in memory(and object or value is stored in heap), list is defined using square brackets [] and elements are separated by commas 
list0=[]
lis1=[0]*5 #creates a list of size 5 with all elements as 0


#slicing
a= [1,2,3,4,5,6,7,8,9]
new_a=a[1:5:1]
print("new_a:", new_a)
rev_a=a[::-1] #for reversing a list


# list comprehension examples:
list1=[1,2,3,4,5]
squares=[x**2 for x in range(1,11)]
evens=[x for x in range(10) if x%2==0]
pairs=[(i,j) for i in range(2) for j in range(3)] # break cannot be used inside list comprehensions
print("List1:", list1)
print("Squares:", squares)
print("Evens:", evens)
print("Pairs:", pairs)

#list comprehesion full usage
sample1=[1,2,1,2,3,4,2,2,3,4,4,2,2,1]
ansoelist=['Even' if x%2==0 else 'Odd' for x in sample1]
print(ansoelist)


#list methods
list2=[1,2,3]
list2.append(4) #adds element at the end
list2.insert(1,5) #inserts 1 at position 5
list2.pop()#remove last element and returns it
list2.remove(1) #removes first occurence of 1, raises ValueError if not found
# to remove element at a specific index we can use pop(index) or del list2[index]
list2.extend([6,7,8]) #extends list by appending elements at the end or merge 2 lists
list2.sort() #sorts the list in ascending order inplace**
list2.sort(reverse=True) #sorts the list in descending order inplace**
list2.reverse() #reverses the list inplace** or we can use slicing list2[::-1] to reverse a list but it creates a new list

new_lis=[1,3,1,2,1,2]
other=sorted(new_lis) #returns a new sorted list without modifying the original list
other.count(1) #returns the number of occurrences of 1 in the list
other.index(2) #returns the index of the first occurrence of 2 in the list


#list unpacking
a,b,c=[1,2,3] #unpacking list into variables
print("a:", a)
#end