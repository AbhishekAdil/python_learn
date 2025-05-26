# OOPs (part - 2)

# del keyword -> used to delete object properties or object itself
'''
del s1.name     # delete attribute
del s1          # delete object
'''

class Student:
    def __init__(self, name):      # constructor
        self.name = name

s1 = Student("Abhishek")
print(s1.name)

del s1.name   # deleting attribute
del s1        # deleting object

# Private(like) attributes & methods
'''
Conceptual implementations in Python

Private attributes & methods are meant to be used only within the class and are 
not accessible from outside the class.

OOPs have 2 ypes of methods or attribute
1)Public - can access outside the class
2)Private - cannot access outside the class(to hide sensitive information)
'''
# public 
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.acc_pass = acc_pass

acc1 = Account("12345", "abcde")

print(acc1.acc_no)
print(acc1.acc_pass)
#output
#12345
#abcde

# Private  
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass  # to make a attribute private write double underscore(__) before the attribute

acc1 = Account("12345", "abcde")

print(acc1.acc_no)
print(acc1.__acc_pass)     # __acc_pass is a private attribute
#output
#12345
#AttributeError: 'Account' object has no attribute '__acc_pass'


# Private (but can access through different way)
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass  
   
    def reset_pass(self):         # reset_pass can access the __acc_pass because it is inside the class
        print(self.__acc_pass)

acc1 = Account("12345", "abcde")

print(acc1.acc_no)
print(acc1.reset_pass())

#12345
#abcde
#None


# Making attribute and functions private

class Person:
    __name = "anonumous"    # here name attribute is private

    def __hello(self):      # here hello method is private, cannot access by the object
        print("Hello person!")

    def welcom(self):       # welcome can access both attribute and methods, because it is inside the class
        self.__hello()

p1 = Person()

print(p1.welcom())     # we can access welcome not __hello
#output
#Hello person!
#None

# Inheritance
'''
When one class(child/derived) derives the properties and methods of another class(parent/base).

class Car:
    .....

class ToyotaCar(Car):
    .....

Here ToyotaCar inherite the properties(attributes and methods) of Cars.

parent/base class -> jisse properties li jati hai
child/derived class -> jo properties leta hai
'''

class Car:
    color = "Black"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):            # Car class is inheritated here
    def __init__(self, name):
        self.name = name 

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.name)       # attribute of ToyotaCar
print(car1.start())    # method of Car class is inheritate in ToyotaCar
print(car1.color)      # attribute of Car

# OUTPUT
#fortuner
#car started..
#None
#Black



# Inheritance in OOP allows properties and methods to be passed from parent to child classes
'''
Types of inheritance
1) Single - level Inheritance -> one base(parent) class and one derived(child) class

2) Multi-level Inheritance -> Multilevel Inheritance in Python is a type of Inheritance in which a 
class inherits from a class, which itself inherits from another class.

3) Multiple Inheritance -> Multiple inheritance in Python is a feature that allows a class to inherit 
attributes and methods from multiple parent classes. This means a class can inherit and combine 
functionalities from different classes, creating a more versatile and reusable code structure.
'''

'''
Example of Sigle - level Inheritance:-

class Car:
    color = "Black"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):            # Car class is inheritated here
    def __init__(self, name):
        self.name = name 

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.name)       # attribute of ToyotaCar
print(car1.start())    # method of Car class is inheritate in ToyotaCar
print(car1.color)      # attribute of Car
'''

'''
Example of Multi - level Inheritance:-

class Grandparent:
    def grandparent_method(self):
        return "Method from Grandparent"

class Parent(Grandparent):
    def parent_method(self):
        return "Method from Parent"

class Child(Parent):
    def child_method(self):
        return "Method from Child"

# Creating an object of the Child class
child_object = Child()

# Accessing methods from all levels of the inheritance chain

print(child_object.grandparent_method()) # Output: Method from Grandparent
print(child_object.parent_method())      # Output: Method from Parent
print(child_object.child_method())       # Output: Method from Child

'''

# Multi - level Inheritance (Car ---> ToyotaCar ---> Fortuner)

class Car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):            # Car class is inheritated here
    def __init__(self, brand):
        self.name = brand

class Fortuner(ToyotaCar):      # Fortuner inheritated ToyotaCar, which Interitate properties from Cars
    def __init__(self, types):
        self.types = types

car1 = Fortuner("diesel")
car1.start()           # inherite from Car class

car2 = ToyotaCar("fortuner")
print(car2.name)

'''
Example of Multiple Inheritance:-

class BaseClass1:
    def method_1(self):
        print("Method from BaseClass1")

class BaseClass2:
    def method_2(self):
        print("Method from BaseClass2")

class DerivedClass(BaseClass1, BaseClass2):
    def method_3(self):
        print("Method from DerivedClass")

# Creating an instance of the derived class
instance = DerivedClass()

# Calling methods from both base classes and the derived class

instance.method_1()  # Output: Method from BaseClass1
instance.method_2()  # Output: Method from BaseClass2
instance.method_3()  # Output: Method from DerivedClass
'''

# Multiple inheritance

class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A, B):
    varC = "Welcome to class C"

c1 = C()

print(c1.varC)    # Welcome to class C
print(c1.varB)    # Welcome to class B
print(c1.varA)    # Welcome to class A


# Super Method -> super() method is used to access methods of the parent class.
# super means parent

class Car:
    def __init__(self, type):     # constructor
        self.type = type

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):           
    def __init__(self, name, type):
        super().__init__(type)   # access type from the Car
        self.name = name
        super().start()

car1 = ToyotaCar("prius", "Electric")
print(car1.type)
print(car1.name)

#OUTPUT
# car started..
# Electric
# prius

'''
class method:

A class method is bound to the class & receives the class as an implicit first argument.

Note - static method can't access or modify class state & generally used for utility.

class Student:
    @classmethod   #decorator
    def college(cls):
        pass
'''

class Person:
    name = "anonymous"

    def changeName(self, name):
        self.name = name

p1 = Person()
p1.changeName("Abhi")
print(p1.name)           # Abhi
print(Person.name)       # anonymous(access name attribute from the class)
# Name is not change in the class , it only created a new attribute as name and enter name as Abhi

# To change the name attribute in the class 
# method 1)
class Person:
    name = "anonymous"

    def changeName(self, name):
        Person.name = name        # it not crete a new attributr as name  

p1 = Person()
p1.changeName("Abhi")
print(p1.name)           # Abhi
print(Person.name)       # Abhi

# method 2)
class Person:
    name = "anonymous"

    def changeName(self, name):
        #Person.name = name 
        self.__class__.name = name    

p1 = Person()
p1.changeName("Abhi")
print(p1.name)           # Abhi
print(Person.name)       # Abhi

# to access the class directly in the function (use @classmethod)

class Person:
    name = "anonymous"

    # def changeName(self, name):
    #     #Person.name = name 
    #     self.__class__.name = name 

    @classmethod      # decorator
    def changeName(cls, name):  # cls -> refering to the class(first implicit argumnet for class)
        cls.name = name        # it directly make changes in the class attribute name    

p1 = Person()
p1.changeName("Abhi")
print(p1.name)           # Abhi
print(Person.name)       # Abhi


# Property
# We use @property decorator on any method in the class to use the method as a property

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math 
        self.percentage = str((self.phy + self.chem + self.math)/3) + "%"

stu1 = Student(98, 99, 97)
print(stu1.percentage)     # 98.0%
# Suppose we have changed marks of phy to 86

stu1.phy = 86
print(stu1.phy)          # 86
print(stu1.percentage)   # 98.0%
# here our percentage is not change when we change the marks



# To change the percentage when we change the marks
# For the cases when we can't give a fixed value to attribute

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math 
        self.percentage = str((self.phy + self.chem + self.math)/3) + "%"

    def calcPercentage(self):
        self.percentage = str((self.phy + self.chem + self.math)/3) + "%"

stu1 = Student(98, 99, 97)
print(stu1.percentage)     # 98.0%
# Suppose we have changed marks of phy to 86

stu1.phy = 86
print(stu1.phy)          # 86
stu1.calcPercentage()
print(stu1.percentage)   # 94.0%    (percentage changed as marks changes)



# To do the above task, we have a different method called @property

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math 
 

    @property     # decorator  (Jo bhi parameter change hoga, vo change yaha reflect hoke aa raha hoga)
    def percentage(self):         #Here percentage is a function but acts as a attribute
        return str((self.phy + self.chem + self.math)/3) + "%"

stu1 = Student(98, 99, 97)
print(stu1.percentage)     # 98.0%
# Suppose we have changed marks of phy to 86

stu1.phy = 86
print(stu1.percentage)   # 94.0%    (percentage changed as marks changes)

# Other Important decorators are -> @gatter and @setter


# Polymorphism
'''
Polymorphism, derived from the Greek words "poly" (many) and "morph" (form), describes the ability of
a single function, method, or object to take on multiple forms or behaviors. In Python, polymorphism 
is a core concept in object-oriented programming (OOP) that allows for flexibility and code 
reusability. It enables a single interface to represent different underlying forms or types.

Polymorphism is achieved through various mechanisms:

Duck Typing:
Python's dynamic typing system allows objects to be treated based on their behavior (methods and 
attributes) rather than their specific type. If it walks like a duck and quacks like a duck, then it 
must be a duck.

Method Overriding:
When a subclass defines a method with the same name as a method in its superclass, it overrides the 
superclass's method. This allows objects of different classes to respond differently to the same 
method call.

Operator Overloading:
Python allows operators to be redefined for user-defined classes, enabling them to work with 
different types and perform different actions based on the context.

# Example:

class Animal:
    def speak(self):
        return "Generic animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    return animal.speak()

dog = Dog()
cat = Cat()

print(animal_sound(dog)) # Output: Woof!
print(animal_sound(cat)) # Output: Meow!

In this example, the animal_sound function can accept objects of different classes (Dog and Cat) and 
produce different outputs based on the actual type of the object, demonstrating polymorphism through 
method overriding
'''

# Polymorphism : Operator Overloading
# when the same operator is allowed to have different meaning according to the context
'''
Operators and Dunder function

a + b  # addition        a.__add__(b)

a - b  # subtraction     a.__sub__(b)

a * b  # multiplication  a.__mul____(b)

a / b  # division        a.__trudiv____(b)

a % b  # reminder        a.__mod____(b)
'''

# operator overloading 
print(1 + 2)                  # addition       # 3
print(type(1))                # <class 'int'>

print("apna" + "college")     # concatenate    # apnacollege
print(type("apna"))           # <class 'str'>

print([1, 2, 3] + [4, 5, 6])  # merge          # [1, 2, 3, 4, 5, 6]
print(type([1, 2, 3]))        # <class 'list'>

# we are going to create a class to create complex numbers

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumbers(self):
        print(self.real,"i +", self.img,"j")

    # creating a add function to add complex numbers
    def add(self, num2):       # self = num1
        newReal = self.real + num2.real
        newImg = self.img + num2.img 
        return Complex(newReal, newImg)

num1 = Complex(1, 3)
num1.showNumbers()     # 1 i + 3 j

num2 = Complex(4, 6)
num2.showNumbers()     # 4 i + 6 j

num3 = num1.add(num2)
num3.showNumbers()    # 5 i + 9 j

# num3 = num1 + num2  
#num3.showNumbers()    
#Give me an error because + is not define for adding complex for

# to make this( num3 = num1 + num2) work, we use dunder function of addition(__add__) in the defition 
# of complex number addition

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumbers(self):
        print(self.real,"i +", self.img,"j")

    # creating a add function to add complex numbers using add dunder function(__add__)
    def __add__(self, num2):       # self = num1
        newReal = self.real + num2.real
        newImg = self.img + num2.img 
        return Complex(newReal, newImg)
    
    # for subtraction
    def __sub__(self, num2):       # self = num1
        newReal = self.real - num2.real
        newImg = self.img - num2.img 
        return Complex(newReal, newImg)

num1 = Complex(1, 3)
num1.showNumbers()     # 1 i + 3 j

num2 = Complex(4, 6)
num2.showNumbers()     # 4 i + 6 j

num3 = num1 + num2  
num3.showNumbers()     # Give 5 i + 9 j

num4 = num1 - num2
num4.showNumbers()     # -3 i + -3 j