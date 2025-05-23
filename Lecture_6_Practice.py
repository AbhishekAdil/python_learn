# 1) WAP tp print the length of a list.(list is the parameter)

cities = ["delhi", "gurgaon", "noida", "pune", "mumbai", "chennai"]
heroes = ["thor", "ironman", "captain america", "shaktiman"]

def print_len(list):
    print(len(list))

print_len(cities)   # 6
print_len(heroes)   # 4

# 2) WAP to print the elements of a list in a single line.(list is the parameter)

cities = ["delhi", "gurgaon", "noida", "pune", "mumbai", "chennai"]

def print_list(list):
    for item in list:
        print(item, end=" ")   # use end to give space between the items

print_list(cities)
print()    # delhi gurgaon noida pune mumbai chennai 

'''
cities = ["delhi", "gurgaon", "noida", "pune", "mumbai", "chennai"]

def print_list(list):
    for item in list:
        print(item)

print_list(cities)

OUTPUT:
delhi
gurgaon
noida
pune
mumbai
chennai
'''

# 3) WAP to find the factorial of n.(n is the parameter)

def fact(n):
    fact = 1     # for factorial we initialise our variable with 1
    for i in range(1, n+1):
        fact *= i
    print("Factorial of the number: ", fact)
    return fact
    
fact(5)   # 120
fact(4)   # 24

# or usning while loop
def fact(n):
    i = 1
    fac = 1     # for factorial we initialise our variable with 1
    while i <= n:
        fac *= i
        i += 1
    print("Factorial of the number: ", fac)
    return fac
    
fact(4)

# 4) WAP to convert USD to INR

def convert(usd_val):
    inr = usd_val * 83     # 1 usd = 83 INR
    print(usd_val, "USD =", inr, "INR")

convert(2)    # 2 USD = 166 INR
convert(3)    # 3 USD = 249 INR

# WAP to identify the number is even or odd

def identify(n):
    if(n % 2 == 0):
        print("EVEN")
    else:
        print("ODD")

identify(6)
identify(9)
identify(15)
identify(22)

# Write a recursive function to calculate the sum of the first n natural numbers.

def sum(n):
    if(n == 0):
        return 0
    else:
        return sum(n - 1) + n
print(sum(4))    # 10
print(sum(6))    # 21

# Write a recursive function to print all elements in a list.
# Hint : use list & index as parameters.

# index value change ho rhi hai

def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits = ["mango", "apple", "litchi", "banana"]

print_list(fruits)

'''
OUTPUT
mango
apple
litchi
banana
'''