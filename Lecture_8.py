# OOPS --> To map with real world scenarios , we started using objects in code.
#       --> This is called object oriented programming.

'''
Procedural --> line - by - line code ko likhna(same kaam ke liye baar - baar)

function --> for reuseability of code and reduce redundancy.

OOP --> objects + classes
       objects are under classes
'''

# Class and Object in python
'''
Class ia a blueprint for creating objects.

# creating class
# class name capital latter se start hota hai

class Student:         # Student -> class name
    name = "Abhi"      # All the information related to the Student(class)

# creating object(instance of class)
# Actual thing

s1 = Student()     # s1 = object variable  ; () --> to call the constructor
print(s1.name)     # Abhi
'''
# Example 1
# class
class Student:
    name = "Abhi"

# object
s1 = Student()
print(s1.name)   # Abhi

s2 = Student()
print(s2.name)   # Abhi

# Example 2   
class Car:
    color = "blue"
    brand = "mercedes"

car1 = Car()
print(car1.color)   # blue
print(car1.brand)   # mersedes

# __init__ function (Constructor function) -> Execute at the time of object creation
'''
All classes have a function called __init__() which is always executed when the object is being initiated.

# creating class

class Student:
    def __init__(self, fullname):    # self -> current object variable
        self.name = fullname

# creating object

s1 = Student("Abhi)
print(s1.name)

NOTE -> THe self parameter refers to the current object(instance) of the class, 
and is used to access variables that belongs to the class.
'''

class Student:
    name = "karan"
    def __init__(self):
        print(self)
        print("Adding new student in Database...")

s1 = Student()
print(s1)
print(s1.name)
'''
<__main__.Student object at 0x000001879D8A6A50>
Adding new student in Database...
<__main__.Student object at 0x000001879D8A6A50>
karan

print(self) = print(s1)     (self = s1(first object variable))
'''

# to give different student, different - different names

class Student:
    #name = "karan"
    def __init__(self, fullname):
        self.name = fullname       # name variable created (in name value of fullname added)
        # with the help of self operator we can store diff - diff variable or data
        print("Adding new student in Database...")

s1 = Student("karan")     # the value we pass here comes under fullname 
print(s1.name)     
# Adding new student in Database...
# karan   (here s1=self)

s2 = Student("Abhishek")
print(s2.name)
# Adding new student in Database...     (Constructor har naye object ke sath call hota hai )
# Abhishek   (here s2=self)

# with the help of self operator we can store diff - diff variable or data
# Attributes  --> data , vaviable

# Crete two or more variable

class Student:
    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks      
        print("Adding new student in Database...")

s1 = Student("karan", 97)     
print(s1.name, s1.marks)     

s2 = Student("Abhishek", 88)
print(s2.name, s2.marks)
'''OUTPUT
Adding new student in Database...
karan 97
Adding new student in Database...
Abhishek 88
'''

'''
Types of constructors

1) Default constructors
def __init__(self):
    pass
    
2) Parameterized constructors
def __init__(self, name, marks):
    self.name = name 
    self.marks = marks      
    print("Adding new student in Database...")     
'''

# Class and Instance Attributes
# Class.attr
# obj.attr

class Student:
    college_name = "ABC college"    # common for all students, store only 1 time in the memory
    def __init__(self, name, marks):
        self.name = name            # different for all student, store many time
        self.marks = marks          # different for all student, store many time
        print("Adding new student in Database...")

s1 = Student("karan", 97)     
print(s1.name, s1.marks)     

s2 = Student("Abhishek", 88)
print(s2.name, s2.marks)

# to print the college name
print(Student.college_name)     # Class.attr
print(s2.college_name)          # obj.attr

# When we have same name of class attribute and object attribute, value of object attribute will be print
# object attribute > class attribute
class Student:
    college_name = "ABC college"    
    name = "anyone"     # class attribute
    def __init__(self, name, marks):
        self.name = name     # object attribute       
        self.marks = marks          
        print("Adding new student in Database...")

s1 = Student("karan", 97)     
print(s1.name)    # object attribute > class attribute
# same name hai to object ko hi priority milegi
'''output
Adding new student in Database...
karan     
'''

# Methods(class ke andar function likhne ko hi methods bolte hai)
# Method are functions that belongs to objects.
'''
# creating class

class Student:
    # defining constructor
    def __init__(self, fullname):
        self.name = fullname

    # defining method
    def hello(self):           # hello is tha name of our method
        print("hello", self.name)

# creating object

s1 = Student("karan")
s1.hello()

'''
# Not using self in the method

class Student:
    college_name = "ABC college"    

    def __init__(self, name, marks):
        self.name = name     # object attribute       
        self.marks = marks   

    def welcome(self):        # It is compulsary to pass our first parameter in the method
        print("welcome students")

s1 = Student("karan", 97)     
s1.welcome()       # welcome students

# Using self in the method

class Student:
    college_name = "ABC college"    

    def __init__(self, name, marks):
        self.name = name     # object attribute       
        self.marks = marks   

    def welcome(self):        # It is compulsary to pass our first parameter in the method
        print("welcome students,", self.name)

    def get_marks(self):
        return self.marks


s1 = Student("karan", 97)     
s1.welcome()       # welcome students, karan 
print(s1.get_marks())   # 97

# Static Methods
# Methods that don't use the self parameter(work at class level)
# -> ese methods jinke liye self ki jarurat nhi hoti usko class level me lane ke liye use krte hai
# self if for objects , not for the class 
'''
class Student:
    @staticmethod     # decorator
    def college():
        print("ABC college")

@statismethod -> for changing the behaviour of normal function to a static function 
              -> to convert a normal function into a static function

* Decoratos allow us to wrap another function in order to extend the behaviour of the wrapped function,
without permanently modifying it.
or
ek function hai jo ki decorator hai , vo parameter me bhi function lega and output me bhi function dega
'''
class Student:
    @staticmethod     # decorator
    def college():
        print("ABC college")
s1 = Student()
s1.college()         # ABC college

'''
Important:

4 pillers of oops
1)Abstraction   | 2)Encapsulation   | 3)Inheritance   | 4)Polymorphism

1) Abstraction: 
hinding the implementation details of a class and only showing the essential features to the user.

2) Encapsulation:
wrapping data and function into a single unit(object).

3) Inheritance:


4) Polymorphism:


'''
# Abstraction: 
# hinding the implementation details of a class and only showing the essential features to the user.

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
        # means car abhi start nhi huyi hai

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started..")

car1 = Car()
car1.start()     # car started..  (car start hone se pahale kya ka hua vo user ko show nhi hua)

# Encapsulation
# wrapping data and function into a single unit(object).
# jo abhi tak krte aaye hai vhi hai . 
# data(attribute) + function -----> unit(object)

