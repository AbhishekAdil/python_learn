# 1)Write a Program to input 2 numbers & print their sum

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

sum = a + b
print("Sum of the two numbers are: ", sum)

#OR

first = int(input("Enter First: "))
second = int(input("Enter Second: "))

print("Sum ", first + second)

# 2) WAP to input side of a square & print its area

side = int(input("Enter the side of the square: "))
area = side * side
print("Area of the Square: ", area )

#OR
side = int(input("Enter the side of the square: "))
print("Area: ", side ** 2)

# 3) WAP to input 2 floating point numbers & print thrie average

x = float(input("Enter First Number: "))
y = float(input("Enter Second Number: "))

avg = (x + y) / 2
print("Average of the numbers are: ", avg)

#OR
x = float(input("Enter First Number: "))
y = float(input("Enter Second Number: "))

print("Avg: ", (x+y)/2)

# 4)WAP to input 2 integer numbers, a and b. Print True if a is greater yhan or equal to b. If not Print False

a = int(input("First: "))
b = int(input("Second: "))

print(a >=b ) 