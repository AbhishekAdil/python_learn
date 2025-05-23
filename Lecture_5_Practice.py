#using for loop
# 1) Print the elememnt of the following list using a loop:
#    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for num in list:
    print(num)
''' output
1
4
9
16
25
36
49
64
81
100
'''

# 2) search for a number x in this tuple using loop: (linear search)
#   [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)

x = 49

idx = 0
for el in tup:
    if(x == el):
        print("number found at index", idx)
    idx += 1

'''output
number found at index 6
number found at index 10
'''

# ek baar number mile fir break krna hai 

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)

x = 49

idx = 0
for el in tup:
    if(x == el):
        print("number found at index", idx)
        break
    idx += 1

'''output
number found at index 6
'''

# 3) print numbers from 1 to 100 by using for and range()
for i in range(1, 101):
    print(i)

# 4) print numbers from 100 to 1 using for and range()
for i in range(100, 0, -1):    # step size can be negative (-1)
    print(i)

# print a multiplication table of a number n.
n = int(input("Enter a number:" ))

for i in range(1, 11):
    print(n * i)
'''OUTPUT
Enter a number:4
4
8
12
16
20
24
28
32
36
40
'''

# 5) WAP tp find the sum of first n natural numbers.(using while)

# using while loop
n = int(input("Enter a natural number: "))

sum = 0
i = 1
while i <= n:
    sum += i     # i ki value sum me add hote ja rahi hai
    i += 1

print("Total sum = ", sum)

# using for loop
n = int(input("Enter a natural number: "))

sum = 0
for i in range(1, n+1):
    sum += i

print("Total sum = ", sum)

# 6) WAP tp find the factorial of first n numbers. (using for)

n = int(input("Enter a natural number: "))
fac = 1     # for factorial we initialise our variable with 1

for i in range(1, n+1):
    fac = fac * i

print("Factorial of the number: ", fac)

# using while loop

 
n = int(input("Enter a Number: "))
fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1

print("Factorial: ",fact)