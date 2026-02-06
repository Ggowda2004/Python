#Strings are Ordered, Indexed(allows slicing but return a new string) iterable but not Mutable(immutable)
#strings store reference to the memory location of the string value, not the actual value itself.(like list, tuple, set, dict)
#concatenation is slower than list append as strings are immutable

str1="Hello"
z=str1[0] #returns 'H'
z2=str1[1:4] #returns 'ell'

samp_str="HELLO world "
print("-----------------------------------------------")
#Common String Methods
print(samp_str.lower()) #hello world
print(samp_str.upper()) #HELLO WORLD
print(samp_str.capitalize()) #Hello world
print(samp_str.title()) #Hello World
print(samp_str.count('l')) #3
new_3=samp_str.replace("world","there") #replaces all occurrences of 'world' with 'there'
f="a a a b"
s=f.replace("a","c",1) #replaces first 1 occurrences of 'a' with 'c'
print(s) #c a a b

new_1=samp_str.strip() #removes leading and trailing whitespace, can also remove specific characters passed as argument, we can also use *** lstrip() and rstrip() ***

print("-----------------------------------------------")

#slpit() method
new_2=samp_str.split() #splits string into list of words based on whitespace, can also split based on specific delimiter passed as argument
print(new_2) #['HELLO', 'world']
x="hello"
y=list(x) #splits into individual characters, wew can also pass any argument to split based on that
print(y) #['h', 'e', 'l', 'l', 'o']

print("-----------------------------------------------")
#join() method
list1=["1","2","3"]
joinned="-".join(list1) #joins list of strings into a single string with specified separator
print(joinned) #1-2-3(new string, if "" then 123)

print("-----------------------------------------------")
#find() method
index=samp_str.find("world") #returns the index of the first occurrence of 'world' in the string, returns -1 if not found
print(index)#6

print("-----------------------------------------------")
#startswith() and endswith() methods
print(samp_str.startswith("HELLO")) #True

print("-----------------------------------------------")
#testing somethings
s='kmgg'
a=list(s)
print(a==a[::-1]) #checks if the list is a palindrome
rev_s=s[::-1]
print(s==rev_s) #checks if the string is a palindrome
