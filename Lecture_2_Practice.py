# 1) WAP tp input user's first name and print its length

str = input("Enter Your First Name: ")
len = len(str)
print("Your First Name: ", str)
print("Lenght of your First Name: ", len)

# or

name = input("Enter Your Name: ")
print("lenght of your Name is: ", len(name))

# 2) WAP to find the occurrence of '$' in a String

str = "Hi, $I am the $ symbol $99.99"
print(str.count("$"))

# or 

name = "Hi, $I am the $ symbol $99.99"
print("The Occurrence of the string: ", name.count("$"))

# 3) WAP to check if a number entered by the user is odd or even

num = int(input("Enter a Number: "))

if(num % 2 == 0):  # % used for reminder
    print("Even")  # all the even numbers are divisible by 2
else:
    print("odd")

# OR 
num = int(input("Enter a number: "))
rem = num % 2

if(rem == 0):
    print("EVEN")
else:
    print("ODD")

# 4) WAP to find the gretest of 3 numbers entered by the user.

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

if(a >= b and a>= c):
    print("First Number is the greatest: ", a)
elif(b >= c):
    print("Second Number is the largest: ", b)
else:
    print("Third Number is the largest: ", c)

# 5) WAP to check if a number is a multiple of 7 or not

num = int(input("Enter a number: "))
rem = num % 7

if(rem == 0):
    print("Number is multiple of 7")
else:
    print("Number is not a multiple of 7")
