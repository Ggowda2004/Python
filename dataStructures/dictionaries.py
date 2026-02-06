#Dictionaries are used to store data values in key:value pairs, no duplicate keys allowed.(assigning same key, overwrites previous value)
#keys must be immutable types (string, number, tuple), values can be of any type.
#Dictionaries are unordered(access is by key), mutable,dynamic collections. (no indexing or slicing)

dict1={"name":"John", "age":30, "city":"New York"}
dict1["sex"]="male"  #adding new key:value pair
dict1["age"]=31      #updating existing key's value
dict_c={x:x*2 for x in range(10)}  #dictionary comprehension

print('------------------------------------')
#methods
#to remove
dict1.pop("city")          #removes key:value pair with specified key or key error if not found
dict1.popitem()            #removes and returns last inserted key:value pair
dict1.clear()            #removes all key:value pairs

#-----------------------------------------------------------#
d={"a":1, "b":2}
d2=d.copy()               #creates a shallow copy of the dictionary, changes to d2 affect d only if values are mutable types
n_d={"a":["1","2"], "b":"2"}
n_d2=n_d.copy()   #shallow copy, changes to n_d2['a'] will affect n_d['a'] as list is mutable and both have reference to same list object
#so we can use deepcopy to avoid this
import copy
n_d3=copy.deepcopy(n_d)  #deep copy, changes to n_d3 will not affect n_d
#-----------------------------------------------------------#



val1=d.get("a")               #returns value for specified key or None if not found
#or val1=d.get("a", default_value) to return default_value if key not found


#.keys and .values are view objects that reflect changes made to the dictionary and can be converted to list or set
keys_list=d.keys()           #returns a view object of all keys 
#to use as list
keys_as_list=list(keys_list)
values_list=d.values()       #returns a view object of all values

for k,v in d.items():    #returns a view object of all key:value pairs
    print(k,v)


print('------------------------------------')
emptyd={}               #creating empty dictionary
list1=["x","y","z"]
for i,key in enumerate(list1):
    emptyd[key]=i*10      #adding key:value pairs dynamically
print(emptyd)


#dict has in operator to check for presence of key only
#d['a'] returns value for key 'a' or raises KeyError if not found, we can use d.get('a') to return None instead of error if key not found
d.get('a')#better



#***most important usage to count occurrences of items***
sample_list=["apple","banana","orange","apple","orange","banana","apple"]
count_dict={}
for i in sample_list:
    count_dict[i]=count_dict.get(i,0)+1  #if key not found, get returns 0, so we add 1 to it
print(count_dict)
#output: {'apple': 3, 'banana': 2, 'orange': 2}