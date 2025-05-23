# Funtions and Recursion

# functions ---> Block of statements that perform a specific task.
# ->Ek baar function likh diya to us function ko same task krwane ke liye baar baar call kr skte hai.
# remove redundant(same code ko baar baar likhna)

'''basic structure for function writing

def func_name(parameter1, parameter2, ...):      # function define
    # some work
    return val

func_name(arg1, arg2, ..)  # function call

Example:- 
def sum(a, b):      # function define
    s = a + b
    return s

print(sum(2, 3))    # function call
'''

def sum(a, b):      # passing parameters a and b
    sum = a + b     # work
    print(sum)      # in a function defining pahale print karenge uske baad return krenge(compulsary)
    return sum      

sum(2, 3)  

sum(2, 10)

sum(12, 17)

# or
# function defition 
def sum(a, b):  # parameters
    return a + b

add = sum(3, 7)  # function call  :  arguments
print(add)   # 10

# or

def sum(a, b):
    return a + b

print(sum(2, 4))   # 6

# Function for printing hello

def print_hello():   # function ke ander parameter dena completaly opltional hai. Bina parameter diye bhi function bana skte hai
    print("hello")   # value return krwana bhi completaly optional hai 

print_hello()   # hello
print_hello()   # hello
print_hello()   # hello
print_hello()   # hello
print_hello()   # hello

output = print_hello()
print(output)   # None --> kyoki to function return me kuch return nhi krna uska output None aata hai

# Function for calculating average of 3 numbers

def calc_avg(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg

calc_avg(1, 2, 3)   # 2.0

# or

def avg(a, b, c):
    avg = (a + b + c) / 3
    print(avg)
    return avg

avg (3, 6, 9)      #6.0
avg (9, 18 , 27)   #18.0

# Difference between print and return
'''
print() and return serve different purposes in Python.

print() is a function that displays output to the console, primarily used for debugging or showing 
information to the user. It doesn't affect the flow of the program execution beyond displaying the 
output.

return, on the other hand, is a statement used within a function to send a value back to the caller. 
When a return statement is encountered, the function execution stops, and the specified value is 
returned. This value can then be used in other parts of the program. If a function doesn't have a 
return statement, it implicitly returns None.

def add(x, y):
    print(f"The sum of {x} and {y} is")    # print statement
    return x + y                           # return statement

result = add(5, 3)                         # Output: The sum of 5 and 3 is
print(result)                              # Output: 8
'''

# Types of Functions 
'''
1) Built- in functions -> their work, and logic already assigned in python [Eg. print(), len(), type(), range()]
2) user defined functions -> function written by the programmers
'''

# Default parameters
# Assigning a default value to parameter, which is used when no argument is passed.
'''
def calc_prod(a=1, b=2):     # Assigning a default value to parameter
    print(a * b)
    return a * b

calc_prod()   # output - 2

# one value assign krenge 
def calc_prod(a, b=2):      # 2 is default argument for b
    print(a * b)
    return a * b

calc_prod(2)   # 2 is taken as value of a
# output - 4

# if we assign value of a and not b , it will dive us a error
#  
def calc_prod(a=3, b):     # 3 is default argument for a
    print(a * b)
    return a * b

calc_prod(2)   # 2 is not taken as value of b
# output - Error

# default values are given from the last
'''

# Recursion -> when a function calls itself repeatedly.
# Loop <--> Recursion (jo kaam loop me krte hai vo kaam recursion me bhi kr skte hai and vice versa)
'''
# print n to 1 backwards

def show(n):
    if(n == 0):    # stopping condition
        return     # control return
    print(n)
    show(n-1)   # function calla itself   # repeatedly decreases the value of n

show(n)
'''

# print n to 1 backwards
# recursive function
def show(n):
    if(n == 0):   # Base case -> to define the stopage of the recursion
        return     
    print(n)
    show(n-1)   # calling function in a function

show(5)     # 5, 4, 3, 2, 1

# how return looks like
# how recursion work
def show(n):
    if(n == 0):   
        return     
    print(n)
    show(n-1)
    print("End")   

show(3) 
'''
OUTPUT:
3
2
1
End
End
End
'''

# return n!(factorial)
# n! = (n - 1)! * n    # recurrence relation
# fact(n) = fact(n-1) * n
# fact(n-1) = fact(n-2) * (n-1)

def fact(n):
    if(n ==1 or n==0):
        return 1      # Because 0! and 1! is 1
    #else:
        #return fact(n-1) * n
    return fact(n-1) * n

print(fact(2)) #2
print(fact(4)) #24
print(fact(6)) #720 