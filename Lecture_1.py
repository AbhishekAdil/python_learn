# Introduction to python

# Input Output 
# variables
# data types
# operators

# Our First Program

# For printing Strings
print("Hello World")
print("my name is Abhishek Adil.")
print("My age is 22.")
print("My name is Abhishek Adil.", "My age is 22.")

# For Printing Integers
print(22)
print(35)
print(35+22)

# Variable
# Variable is a name given to a memory location in a program

# defining the variables as name, age and price 
# Right side ki value, left side me jake save ho rhi hai
# "=" is a assignment operator

name = "Abhi" #String
age = 22 #int
price = 25.99  #float

print("name") #double quotes ke andar jo bhi likhte hai, same to same print ho jata hai
print("age")

# for printing tha values of variables
print(name)
print(age)
print(price)

# Printing all the variables in the form of a sentence
print("My Name is : ", name)
print("My Age is : ", age)

# Assigning a variable to another Variable
age2 = age
print(age2)

# for printing the types(Data Types) of the variables

print(type(name)) # give the data type(class) of tha values stored in the variables
print(type(age))
print(type(price))

# Data Types
# Integer (+ve, -ve, 0)
# String (sentence or world in double Quotes, single quotes or Triple Quotes)
# Float 
# Boolean
# None

# String Example
name1 = 'Abhi'
name2 = "Abhi"
name3 = '''Abhi'''

print(name1)
print(name2)
print(name3)

# Boolean and None Example
age = 23
old = False
a = None

print(type(age)) # type() is also a function
print(type(old))
print(type(a))

# Keywords
# they are reserved words in python
# they have perticular meaning for use
"""
Keyword	        Description
and	            A logical operator
as	            To create an alias
assert	        For debugging
break	        To break out of a loop
class	        To define a class
continue     	To continue to the next iteration of a loop
def         	To define a function
del         	To delete an object
elif	        Used in conditional statements, same as else if
else	        Used in conditional statements
except	        Used with exceptions, what to do when an exception occurs
False	        Boolean value, result of comparison operations
finally	        Used with exceptions, a block of code that will be executed no matter if there is an exception or not
for	            To create a for loop
from	        To import specific parts of a module
global	        To declare a global variable
if	            To make a conditional statement
import	        To import a module
in	            To check if a value is present in a list, tuple, etc.
is	            To test if two variables are equal
lambda	        To create an anonymous function
None	        Represents a null value
nonlocal	    To declare a non-local variable
not	            A logical operator
or	            A logical operator
pass	        A null statement, a statement that will do nothing
raise	        To raise an exception
return	        To exit a function and return a value
True	        Boolean value, result of comparison operations
try	            To make a try...except statement
while	        To create a while loop
with	        Used to simplify exception handling
yield	        To return a list of values from a generator
"""
# Print the sum of Two Variables
a = 2
b = 5
sum = a + b
print(sum)

print(type(a))

# Add two numbers with user input

# x = input("Type a number: ")  # The input() function allows user input.
# y = input("Type another number: ")

# sum = int(x) + int(y)
# print("The sum is: ", sum)

# Comments in Python

# Single line comment

"""
Multi Line
Comment
"""
# multiple lines ko comments banane ke liye short cut - (ctrl + /)

# Types of Operators in Python
"""
Python operators are special symbols that perform operations on operands (values or variables). Here's a list of the common types of operators in Python:

Arithmetic operators:
Used for mathematical calculations.
+ (addition)
- (subtraction)
* (multiplication)
/ (division)
// (floor division - returns the integer part of the quotient)
% (modulus - returns the remainder of the division)
** (exponentiation)

Assignment operators:
Used to assign values to variables.
= (assign)
+= (add and assign)
-= (subtract and assign)
*= (multiply and assign)
/= (divide and assign)
//= (floor divide and assign)
%= (modulus and assign)
**= (exponentiate and assign)

Comparison operators:
Used to compare values.
== (equal to)
!= (not equal to)
> (greater than)
< (less than)
>= (greater than or equal to)
<= (less than or equal to)

Logical operators:
Used to combine or modify boolean expressions.
and (returns True if both operands are True)
or (returns True if at least one operand is True)
not (returns True if the operand is False, and False if the operand is True)

Identity operators:
Used to check if two variables refer to the same object in memory.
is (returns True if both operands are the same object)
is not (returns True if both operands are not the same object)

Membership operators:
Used to check if a value is present in a sequence (e.g., string, list, tuple).
in (returns True if the value is found in the sequence)
not in (returns True if the value is not found in the sequence)

Bitwise operators:
Used to perform operations on individual bits of binary numbers. 
& (AND)
| (OR)
^ (XOR)
~ (NOT)
<< (left shift)
>> (right shift)
"""

# Arithmetic operators
a = 5
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) # modulo- to find the reminder
print(a ** b) #power operator- a ki power b (a^b)

# Relation/ Comparision Operators - Give True or False Value
a = 50
b = 20

print (a == b) #False
print (a != b) #True    #!=(not equal to)
print (a >= b) #True
print (a > b) #True
print (a <= b) #False
print (a < b) #False

# Assignment Operators
num = 10
num = num + 10  # 10 + 10 => 20
print("num: ", num)

num += 10  # 20 + 10 = 30
print(num)

num -= 10 # 30 - 10 = 20
print(num)

num *= 5 # 20 * 5 = 100
print(num)

num /= 5 # 100 * 5 = 20
print(num)

# num %= 5 # 100 % 5 = 0
# print(num)

num **= 5 # 20 ** 5 = 320000
print(num)

#LOgical Operators - not, and and or
# work on boolean values
# not - return opposite value
print(not False)  # True
print(not True)  # False

a = 50
b = 30
print(not (a > b))   # False

# and - work on two operators, give true answer only when both are true.
val1 = True
val2 = True
print("Ans operator:", val1 and val2)   #True

val1 = True
val2 = False
print("Ans operator:", val1 and val2)   #False

# or - do me se koi ek bhi true hoga ,  to true value dega
val1 = True
val2 = False
print("Ans operator:", val1 or val2)    #True

val1 = False
val2 = False
print("Ans operator:", val1 or val2)    #False

# Exaple
a = 50
b = 30
print("OR operator:", (a == b) or (a > b)) # a == b => False , a > b => True, So False or True => True

a = 50
b = 30
print("AND operator:", (a == b) and (a > b)) # a == b => False , a > b => True, So False and True => False

# Type Conversion
# ek type ke variable ko dusre type ke variable me change krte hai 
# type int -----> type float

#Two types => 1) conversion 2) casting

# type conversion (interpreter Automatically kr deta hai)
a = 2 # type - int
b = 4.5 # type - float

sum = a + b # Python interpreter converts the int data type to float (float is superior than int)
# 2.0 + 4.5 = 6.5
print(sum)

# a = "2"   #String
# b = 4.5   # float
# sum = a + b
# print(sum) #Give a Error because we cannot add a string value under a float value

# Type Casting (manually changing the type of the variable)
# var = "string"
# int(var)  or float(var)

a = "2"   #String
b = 4.5   # float
a = int("2")
sum = a + b
print(type(a))
print(sum)

a = "2"   #String
b = 4.5   # float
a = float("2")
sum = a + b
print(type(a))
print(sum)

a = 3.14
a = str(a)
print(type(a))

a = "2"   #String
b = 4.5   # float
a = float(a)
sum = a + b
print(type(a))
print(sum)

# Inputs in Python
# input() statement is used to accept values(using keyboards) from user

# input() ----> result for input() is always string
# int(input())   -----> int
# float(input())  -----> float

name = input("Enter your Name: ")
print("Welcome ", name)

age = input("Enter your Age: ")
print("Your age is ", age)

val = input("Enter some value: ") 
print(type(val), val)  # "25", "99.99" 
# always give data type str(chahe int ya float hi kyo na enter kre)

# integer value ke liye
val = int(input("Enter some value: ")) #type casting kr diye 
print(type(val), val)

# float value ke liye
val = float(input("Enter some value: ")) #type casting kr diye 
print(type(val), val)

# Example of taking input in python
name = input("Enter Name: ")
age = int(input("Enter Age: "))
marks = float(input("Enter Marks: "))

print("Welcome ", name)
print("Your Age: ", age)
print("Your Marks: ", marks)
