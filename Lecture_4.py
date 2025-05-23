# Dictionary and Set

# Dictinary in Python (Built-in data stucture)
# Dictionaries are used to store data values in Key : value pairs
# They are unordered, mutable(changeable) and don't allow duplicate keys.

# Unordered --> because there is no index in it , like String, listand tuple have

'''
dict = {
    "name" = "Abhi",           # storing a string 
    "cgpa" = 9.6,              # storing a float value
    "marks" = [98, 97, 95]     # storing a list
    }                          # we can store data of any type in a single dictionary
'''

info = {
    "key" : "value",
    "name" : "Abhishek",
    "Learning" : "coding", # string
    "age" : 22,
    "is_adult" : True,     # Boolean Value
    "marks" : 94.4,        # float
    "subjects" : ["python", "C", "Java"],     # list value
    "topics" : ("dict", "sets")                      # tuple value
}
# keys may be a string, int, float, boolean, list
print(info)
print(type(info))    # return <class 'dict'>

# to access the values of a dictionary
# print(dict["key"])

print(info["name"])        # return Abhishek
print(info["topics"])      # return ("dict", "sets")
print(info["subjects"])    # return ["python", "C", "Java"]
print(info["age"])         # return 22

print(info["surname"])    # Error , because no key as surname exist

# to change the value of a key
# dict["key"] = new_value

dict = {
    "name" : "Abhishek"
}
# changing the value of a key
dict["name"] = "Raja"    #overwrite on same key  
print(dict)

# Adding new  value
dict["surname"] = "Adil"
print(dict)

# Creating a Empty dictionary

null_dict = {}
print(null_dict)    # return {}

# Adding values in null dictionary

null_dict["name"] = "Abhishek"
print(null_dict)    # return  {'name' : 'Abhishek'}

#### Nested Dictinaries ####
'''
student = {
    "name" : "Abhishek",
    "score" : {
        "chem" : 98,
        "phy" : 97,
        "maths" : 95
        }
    }

student["score"]["math"]   # to access the value  
'''

student = {
    "name" : "Abhishek",
    "score" : {
        "chem" : 98,
        "phy" : 97,
        "maths" : 95
        }
    }

print(student)         # return {'name': 'Abhishek', 'score': {'chem': 98, 'phy': 97, 'maths': 95}}
print(student["score"])           # return {'chem': 98, 'phy': 97, 'maths': 95}
print(student["score"]["chem"])   # return 98

# Dictionary Methods

student = {
    "name" : "Abhishek",
    "score" : {
        "chem" : 98,
        "phy" : 97,
        "maths" : 95
        }
    }

# 1) myDict.keys()     # returns all keys

print(student.keys())     # return dict_keys(['name', 'score']) 
# does not print sub dictionaries keys

# Converting dict_keys into list
# by typecasting

print(list(student.keys()))  # return ['name', 'score']

# To find the total number of key value pair

print(len(student))     # return 2
# or
print(len(list(student.keys())))  # return 2

# 2) myDict.values()   # returns all values

student = {
    "name" : "Abhishek",
    "score" : {
        "chem" : 98,
        "phy" : 97,
        "maths" : 95
        }
    }

print(student.values())    # return dict_values(['Abhishek', {'chem': 98, 'phy': 97, 'maths': 95}])
# in list
print(list(student.values()))  # return ['Abhishek', {'chem': 98, 'phy': 97, 'maths': 95}]

# 3) myDict.items()   # return all (key, val) pairs as tuples

student = {
    "name" : "Abhishek",
    "score" : {
        "chem" : 98,
        "phy" : 97,
        "maths" : 95
        }
    }

print(student.items())
# return   dict_items([('name', 'Abhishek'), ('score', {'chem': 98, 'phy': 97, 'maths': 95})])

# typecast in list
print(list(student.items()))
# return [('name', 'Abhishek'), ('score', {'chem': 98, 'phy': 97, 'maths': 95})]   ---> list

# access the values of dictionary in pairs

pairs = list(student.items())
print(pairs[0])    # return ('name', 'Abhishek')
print(pairs[1])    # return ('score', {'chem': 98, 'phy': 97, 'maths': 95})

# 4) myDict.get("key")  # returns the key according to value
# dict["key"]  , both gives the same value

student = {
    "name" : "Abhishek",
    "score" : {
        "chem" : 98,
        "phy" : 97,
        "maths" : 95
        }
    }

print(student["name"])       # return Abhishek
print(student.get("name"))   # return Abhishek

# but but but
print(student["name2"])       # return error  , and code after the error will not execute
print(student.get("name2"))   # return no error --> give None

# 5) myDict.update(newDict)   # insert the specified items to the dictionary

student = {
    "name" : "Abhishek",
    "score" : {
        "chem" : 98,
        "phy" : 97,
        "maths" : 95
        }
    }

student.update({"city" : "delhi"})
print(student)  
# return {'name': 'Abhishek', 'score': {'chem': 98, 'phy': 97, 'maths': 95}, 'city': 'delhi'}

# or create new dictionary and then update 

new_dict = {"city" : "delhi"}
student.update(new_dict)
print(student)
# return {'name': 'Abhishek', 'score': {'chem': 98, 'phy': 97, 'maths': 95}, 'city': 'delhi'}

# updating multiple values
new_dict = {"city" : "delhi", "age" : 22}
student.update(new_dict)
print(student)
# return {'name': 'Abhishek', 'score': {'chem': 98, 'phy': 97, 'maths': 95}, 'city': 'delhi', 'age': 22}

# updating the dictionary with existing key but change the its value
new_dict = {"name" : "adil", "age" : 22}
student.update(new_dict)
print(student)
# return {'name': 'adil', 'score': {'chem': 98, 'phy': 97, 'maths': 95}, 'age': 22}
# dictionary same key dubara nhi banata , already existind key me hi new values ko store kr deta hai

# Set in Python

# set is the collection of the unordered items.
# each element in the set must be unique & immutable

collection = {1, 2, 3, 4}   # set
print(collection)           # return {1, 2, 3, 4}
print(type(collection))     # terurn <class 'set'>

collection = {1, 2, 3, 4, "hello", "world"}   # set with string values
print(collection)           # return {1, 2, 3, 4, 'world', 'hello'}


# repeated elements stored only once.
collection = {1, 2, 2, 2, "hello", "world", "world"}    # set with duplicate values
print (collection)          # return {1, 2, 'world', 'hello'}    , not give any error
# set ignores the duplicate values 
# set ka koi order nhi hota

# lenght of set
collection = {1, 2, 2, 2, "hello", "world", "world"}
print(len(collection))   # return 4 
# lenght also ignores the repeated values

# creating a empty set

collection = {}  # it is a syntax of a empty dictionary
print(type(collection))   # return <class 'dict'>

# For a empty set 
collection = set()     # empty set syntax
print(type(collection))   # return <class 'set'>

# Set Methods
'''
# set is mutable(set changeable hai)
# but elements of set is immutable(set ke elements change nhi ho skte)

set = { }
set.add(el)      # adds an element
set.remove(el)   # removes the element
set.clear()      # empties the set
set.pop()        # removes a random value

set.union(set2)  # combines both set values & returns new
set.intersection(set2)  # combines common values & return new
'''
# 1) add method

collection = set()

collection.add(1)
collection.add(2)
collection.add(2)

print(collection)   # return {1, 2}

# Adding Different types of values in set

collection = set()

collection.add(1)
collection.add(2)
collection.add("Abhishek")      # string
collection.add((1, 2 ,3))       # tuple
'''
collection.add([1, 2 ,3])       # list  
# we can not store a list in set, because it can change with time 
# Give error
TypeError : unhashable type: 'list'

unhashable type means
immutable ----> have fixed hash value because it not changes with time
mutable ---> don't have fixed hash value because it changes with time
'''
print(collection)  # return  {1, 2, (1, 2, 3), 'Abhishek'}

# 2) remove method

collection = set()

collection.add(1)
collection.add(2)
collection.add(2)

collection.remove(1)

print(collection)  # return {2}

# 3) clear method ---> empties the set

collection = set()

collection.add(1)
collection.add(2)
collection.add("Abhishek")      # string
collection.add((1, 2 ,3))       # tuple

collection.clear()
print(collection)   # return set()
print(len(collection))  # return 0

# 4) pop method ---> removes a random value

collection = {"hello", "abhishek", "world", "coding", "python"}

print(collection.pop())   # pop random value from the collection

# 5) union method --->  set.union(set2)
# combines both set values and return new set

set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.union(set2))   # return {1, 2, 3, 4}  
# creates a new set, does not effect the original sets
print(set1)  # {1, 2, 3}
print(set2)  # {2, 3, 4}

# 6) intersection method ----> combines common values & return new set
# set.intersect(set2)

set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.intersection(set2))   # {2, 3}