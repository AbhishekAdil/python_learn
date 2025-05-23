# LOOPS -> Loops are used to repeat instructions.

# print "Hello" 5 times
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")

# while Loops
'''
while condition:
    # some work

while True :
    print("Hello")   # print Hello infinite times
'''

# printing "hello" 5 times using while loop

count = 1    # Here count is Iterator
while count<= 5:   # Iteration
    print("hello")
    count += 1     # incresing(update) count by 1 (count = count + 1)

print(count)   # 6  <-- 6 pe aake code terminate ho gaya

# To Print the Iterator too
i = 1
while i <= 100000:
    print("abhishek", i)
    i += 1         # Last value -> abhishek 100000

# print numbers from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1    # i = i + 1
print("Loop Ended")
'''
output:
1
2
3
4
5
Loop Ended
'''

# reverse 5 to 1
i = 5
while i >= 1:
    print(i)
    i -= 1     # i = i - 1
print("Loop ended")
'''
output:
5
4
3
2
1
Loop ended
'''

# while loop practice

# 1) Print numbers from 1 to 100.
i = 1
while i <= 100:  
    print(i)
    i += 1 

# 2) print numbers from 100 to 1.
i = 100
while i >= 1:  # stoping condition
    print(i)
    i -= 1 

# 3) Print the multiplication table of a number n.
'''
Concept
let, n = 3   
Table of 3 ---> 3, 6, 9, 12, 15, 18, 21, 24, 27, 30
3 ---> 3 * 1
6 ---> 3 * 2
9 ---> 3 * 3
12 ---> 3 * 4
.
.
.
30 ---> 3 * 10     (n * i)
'''
#multiplication table
n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(n * i)
    i += 1

'''OUTPUT
Enter a number: 5
5
10
15
20
25
30
35
40
45
50
'''

# 4) Print the elements of the following list using a loop:
#    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
''' Concept
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0                       # in a list, index is changing
while idx < len(list)         # lenght of a string = 10
print---> list[idx]
          list[0]
          list[1]......
'''
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# here index value is changing
idx = 0   # beacause index starting from 0
while idx < len(list):
    print(list[idx])    # list[0], list[1], list[2]......
    idx += 1   

# traverse --> kisi bhi list ya tuple ke ek ek item ke upar travel krte hai use traverse bolte hai

# Example 
heroes = ["ironman", "thor", "superman", "batman"]

idx = 0
while idx < len(heroes):
    print(heroes[idx])
    idx += 1

# 5) Search for a number x in this tuple using loop:
#    (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
'''
For searching a element in a tuple or list(or anything)
1) we have to create a variable 
2 ) equat with tha elements
3) print that element which is equal to the variable
'''

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = int(input("Enter a number from tuple: "))

idx = 0  # initialisation
while idx < len(tup):     # loop tab tak chalega jaha tak uska lenght
    if(tup[idx] == x):
        print("Found at idx: ", idx)
    else:
        print("Finding...")    
    idx += 1    
'''
Output:
Enter a number from tuple: 36
Finding...
Finding...
Finding...
Finding...
Finding...
Found at idx:  5
Finding...
Finding...
Finding...
Finding...
'''

# tuple have repeated values
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36, 64)

x = int(input("Enter a number from tuple: "))

idx = 0  # initialisation
while idx < len(tup):
    if(tup[idx] == x):
        print("Found at idx: ", idx)
    else:
        print("Finding...")
    idx += 1
'''
output:
Enter a number from tuple: 64
Finding...
Finding...
Finding...
Finding...
Finding...
Finding...
Finding...
Found at idx:  7
Finding...
Finding...
Finding...
Found at idx:  11
'''

# Break and Continue (in while loop)

# Break : used to terminate the loop when encountered
i = 1
while i <= 5:
    print(i)
    if(i == 3):    
        break      # jaise hi i ki value 3 hogi , loop terminate ho jayega
    i += 1
print("End of loop")
'''
Output:
1
2
3
End of loop
'''

# Example of break

# terminate the loop when it encountered the entered number
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36, 64)

x = int(input("Enter a number from tuple: "))

idx = 0  # initialisation
while idx < len(tup):
    if(tup[idx] == x):
        print("Found at idx: ", idx)
        break
    else:
        print("Finding...")
    idx += 1
print("End of loop")
'''
Output:
Enter a number from tuple: 64
Finding...
Finding...
Finding...
Finding...
Finding...
Finding...
Finding...
Found at idx:  7
End of loop
'''

# Continue : terminates execution in the current iteration & continues of the loop with the next iteration

i = 0
while i<= 5:
    if(i == 3):  
        i += 1    #
        continue  # acts as skip
    print(i)
    i += 1        

'''
Output:  (3 print nhi hoga)
0
1
2
4
5
'''

# print only odd numbers between 1 to 10
i = 1
while i <= 10:
    if(i % 2 == 0):
        i += 1
        continue
    print(i)    
    i += 1     

# print only even numbers between 1 to 10
i = 1
while i <= 10:
    if(i % 2 != 0):
        i += 1
        continue
    print(i)    
    i += 1 

# for loop --> used for sequential traversal. For traversing list, string, tuples etc.

# for Loops
'''
for el in list:
    # some work

# Example

list = [1, 2, 3]
for el in list:
    print(el)
'''  

# for Loop with else
'''
for el in list:
    # some work
else:
    # work when loop ends

# Example

list = [1, 2, 3]
for el in list:
    print(el)
else:
    print('END)
'''
# Simple for loop example
# 1) 
nums = [1, 2, 3, 4, 5]

for val in nums:      # ek ek krke sare value 'val' variable me aa jayenge
    print(val)
''' output:
1
2
3
4
5
'''

# 2)
vaggies = ["potato", "brijal", "ladyfinger", "cucumber"]

for val in vaggies:
    print(val)
''' output:
potato
brijal
ladyfinger
cucumber
'''
# Iterate krne ke liye(kisi value to update kr rhe hai ya hamare pass stopping condition hai) --> while loop 
# traverse krne ke liye --> for loop

# 3)In tuple

tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)

for num in tup:
    print(num)

''' output:
1
2
3
4
5
6
7
8
9
'''

# 4) In string

str = "Abhishek"

for char in str:
    print(char)

''' output:
A
b
h
i
s
h
e
k
'''

#for Loop with else

# Example 1)
str = "Abhishek"

for char in str:
    print(char)
else:            # aise kaam jinhe hum apne loop ke end tak krwana chahte hai unhe else me likhenge
    print("END")
''' output:
A
b
h
i
s
h
e
k
END
'''

# Example 2)
str = "Abhishek"

for char in str:
    if(char == 'i'):
        print("i found")
        break          # yaha par loop break ho jayega or iske aage loop ke code execute nhi honge
    print(char)
else:           
    print("END")

''' output:
A
b
h
i found
'''

# Example 3)
str = "Abhishek"

for char in str:
    if(char == 'i'):
        print("i found")
        break          # yaha par loop break ho jayega or iske aage loop ke code execute nhi honge
    print(char)
          
print("END")   # loop ke bahar hai

''' output:
A
b
h
i found
END
'''

# range() --> 
'''Range function returns a sequence of numbers, stating from 0 by default, and increment by
1 (by default), and stops before a specified number

range(start?, stop, step?)

start --> starting value(by default 0)
stop --> stoping point
step --> step size(by default 1)

for el in range(5):   # 5 -> stop
    print(el)         # 0, 1, 2, 3, 4

for el in range(1, 5):  # 1 -> start, 5 -> stop
    print(el)           # 1, 2, 3, 4

for el in range(1, 5, 2)   # 1 -> start, 5 -> stop, 2 -> step size
    print(el)              #
'''

print(range(5))    # range(0, 5)

seq = range(5)
print(seq[0])   # 0
print(seq[1])   # 1
print(seq[2])   # 2
print(seq[3])   # 3
print(seq[4])   # 4
print(seq[5])    # error


# apply loop on the sequence with range

seq = range(5)     # By default start from 0
for i in seq:
    print(i)
'''
OUTPUT
0
1
2
3
4
'''
# or

for i in range(5):    # range(stop)  
    print(i)     # Give same output as above

for i in range(2, 10):    # range(start, stop)
    print(i)              # start-> included, stop-> not included
'''OUTPUT
2
3
4
5
6
7
8
9
'''

for i in range(2, 10, 2):    # range(start, stop, step)   # step -> by default 1
    print(i) 
'''OUTPUT
2
4
6
8
'''

# print all even numbers between 1 to 100
for i in range(2, 100, 2):    
    print(i)

# print all odd numbers between 1 to 100
for i in range(1, 100, 2):    
    print(i)

# pass Statement(NULL Statement)
# pass is a null statement that does nothing. It is used as a placeholder for future code.
'''
for el in range(10)
    pass
'''
'''
for i  in range(5):
    # empty

print("some useful work")     ## give error because we can not empty a loop

'''

# to overcome this we use pass statement
for i  in range(5):
    pass                # It is used as a placeholder for future code.

print("some useful work")    # return some useful work

# we can also use pass statement in if-else
if i > 5:
    pass

