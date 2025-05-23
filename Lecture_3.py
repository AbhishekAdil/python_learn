#List and Tuples

# List - A list is a data structure (list is a built-in data type in python)

'''    - list in Python is a versatile, ordered, and mutable (changeable) 
         data structure used to store a collection of items. 
         Lists are defined by enclosing comma-separated items within square brackets []. 
         They can contain elements of different data types, including numbers, strings,
         and even other lists.'''

# A built- in data type that stores set of values
# It can store elements of different types(integer, float, string, etc.)

# my_list = [1, "hello", 3.14, True]

''' Lists are indexed, starting from 0 for the first element, 
 and can also be accessed using negative indices, where -1 refers to the last element. '''

# print(my_list[0])  # Output: 1
# print(my_list[-1]) # Output: True

marks1 = 94.4
marsk2 = 87.5
marks3 = 95.2
marks4 = 66.1
marks5 = 45.1

marks = [94.4, 87.5, 95.2, 66.4, 45.1]
print(marks)
print(type(marks))

# Properties of List(almost same as String)

# 1) can access list value through indexing
print(marks[0])
print(marks[1])

# 2) lenght of the list
print(len(marks))

# 3) In array we can only store data of same type, 
#    but in python's list we can store data of different data types in one list.
student = ["Abhi", 22, "Bhilai"]
print(student)

#### Difference in String and List

# Strings --> Strings are immutable(unchangeable) in python
'''
str = "hello"
print(str[0])  #Allowed
str[0] = "y"   # not allowed
'''

# List --> Lists are mutable(changeable) in python 
# 4) Lists are mutable(changeable) in python

student = ["Abhi", 22, "Bhilai"]
student[0] = "Adil"  # allowed
print(student)       # return ['Adil', 22, 'Bhilai']

# 5) In Lists we can only access the values within the index
student = ["Abhi", 22, "Bhilai"]
print(student[5]) # cannot access the index 5 

# List Slicing (sublist)
# --->Similar to String Slicing

# list_name[starting_idx : ending_idx]  # ending_idx is not included
'''
   marks = [87, 64, 33, 95, 76]
1) marks[1:4] is [64,33,95]
2) marks[ :4] is same as marks[0:4]
3) marks[1: ] is same as marks[ 1: len(marks)]
4) marks[ -3: -1] is [33,95]
'''
marks = [85, 94, 76, 63, 48]
print(marks[1:4])  # return [94, 76, 63]
print(marks[:4])   # return [85, 94, 76, 63]
print(marks[1:])   # return [94, 76, 63, 48]
print(marks[1:len(marks)])  # return [94, 76, 63, 48]
# Negative index
print(marks[-3:-1]) # return [76, 63]

#list methods
'''
Common list operations include: (List Method)

Adding elements:     append(), insert(), extend()
Removing elements:   remove(), pop(), del
Accessing elements:  using index []
Modifying elements:  using index []
Slicing:             extracting a portion of the list using [:]
Searching:           using the in keyword
Sorting:             sort()
Reversing:           reverse()

Example:
list = [2, 1, 3]  (given)

list.append(4)             # adds one element at the end  [2, 1, 3, 4]
list.sort()                # sorts in ascending order     [1, 2, 3]
list.sort(reverse = True)  # sort in descending order     [3, 2, 1]
list.reverse()             # reverses list                [3, 1, 2]
list.insert(idx, el)       # insert element at index
'''

list = [2, 1, 3]

list.append(4)   # called mutating the list
print(list)

list.sort()
print(list)    # sorts in ascending order

list.sort(reverse = True)     # sort in descending order
print(list)

# sorting not only apply on number, it can apply on strings also
string_list = ["Banana", "Litchi", "Mango", "Apple"]
string_list.sort()
print(string_list)

string_list.sort(reverse = True)
print(string_list)   

string_list.append("Orange")
print(string_list)     

# reverses list

string_list = ["Banana", "Litchi", "Mango", "Apple"]
string_list.reverse()
print(string_list)      #return ['Apple', 'Mango', 'Litchi', 'Banana']

list = [2, 1, 3]
list.reverse()
print(list)     #return [3, 1, 2]

# insert method ---> list.insert(index_number, element_value)   # insert element at index

list = [2, 1, 3]
list.insert(2, 4)  # insert a element at a perticular index number
print(list)   #return [2, 1, 4, 3]

'''
list = [2, 1, 3, 1]

list.remove(1)   #removes first occurrence of element  [2, 3, 1]

list.pop(index_number)   #removes element at index
'''

list = [2, 1, 3, 1]
list.remove(1)  
print(list)          # return [2, 3, 1]

list = [2, 1, 3, 1]
list.pop(1)          # removing the value of index 1
print(list)          # return [2, 3, 1]

# Tuples in python
# A built - in data type that lets us create immutable sequences of values

tup = (2, 1, 3, 1)
print(type(tup))    # return  <class 'tuple'>

# Access element of tuple using index
print(tup[0])     #return  2
print(tup[1])     #return  1

tup[0] = 5  # Not allowd in tuples, because they are immutable, So we can not assign a value

# Different types of tuple
tup = ()    # empty tuple
print(tup)              # return  ()
print(type(tup))        # return <class 'tuple'>

tup = (1, )   # tuple with single element , Comma lagana important hai
print(tup)            # return  (1, )
print(type(tup))      # return <class 'tuple'>

'''
What if...

tup = (1) , python ise bas ek interger value samjhega 
print(tup)          # return  1
print(type(tup))    # return <class 'int'>

tup = (1.0) , python ise bas ek float value samjhega 
print(tup)          # return  1.0
print(type(tup))    # return <class 'float'>

tup = ("hello") , python ise bas ek string value samjhega 
print(tup)          # return  hello
print(type(tup))    # return <class 'string'>

'''

# for tuple values comma is important

tup = ("hello", )   # python ise bas ek interger value samjhega 
print(tup)          # return ('hello', )
print(type(tup))    # return <class 'tuple'>

# tuple with multiple values
tup = (2, 1, 3, 4)
print(tup)
print(type(tup))

# or

tup = (2, 1, 3, 4,)
print(tup)
print(type(tup))

# Slicing of tuple
# same as lists

tup = (2, 1, 3, 4,)
print(tup[1:3])      #return (1, 3)

# Tuple Methods
'''
tup = (2, 1, 3, 1)

1) tup.index( el )    # return index of first occurrence
Eg)  print(tup.index(1))    # return   1  (index of first occurrence)

2) tup.count(el)      # counts total occurrences
Eg)  print(tup.count(1))    # return   2
'''

# 1) Index Method --->  return index of first occurrence

tup = (2, 1, 3, 4,)
print(tup.index(2))   # return 0

# 2) Count Method --->  counts total occurrences

tup = (2, 1, 3, 4,)
print(tup.count(2))   # return 1

tup = (2, 1, 3, 4, 2, 2)
print(tup.count(2))   # return 3