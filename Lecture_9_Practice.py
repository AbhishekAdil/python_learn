# 1) Define a Circle class to create a circle with radius r using the constructor
#    Define an Area() method of the class which calculates the area of the circle
#    Define a Perimeter() method of the class which allows you to calculate the perimeter of the ciecle.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius

c1 = Circle(21)

print(c1.area())         # 1386.0
print(c1.perimeter())    # 132.0


# 2) Define a Employee class with attributes role, deparment & salary. 
#    This class also has a showDetails() method.
'''
class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role =", self.role)
        print("dept =", self.dept)
        print("salary =", self.salary)

e1 = Employee("Accountant", "Finance", "60,000")
e1.showDetails()
'''
#    Create an Engineer class that inherits properties from employee and 
#    has additional attributes : name and age

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role =", self.role)
        print("dept =", self.dept)
        print("salary =", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75,000")

    def showMe(self):
        print("My name = ", self.name)
        print("age =", self.age)

engg1 = Engineer("Elon", 40)
engg1.showMe()
engg1.showDetails()

# 3) Create a class called Order which stores item and its price.
#    Use Dunder function __gt__ (greater than) to convey that:
#          order1 > order2 if price of order1 > order2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, ord2):     # self = ord1
        return self.price > ord2.price
    
ord1 = Order("chips", 20)
ord2 = Order("tea", 15)

print(ord1 > ord2)      # True
