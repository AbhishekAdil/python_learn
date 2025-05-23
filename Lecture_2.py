# STRINGS AND CONDITIONAL STATEMENT

# Strings - It is a data type that stores a sequence of characters
str1 = "This is String . I love to code in Python"
str2 = 'Apna'
str3 = """This is"""
print(str1)
# Escape Sequence Character ----> for formatting
# 1) \n ----> for next line

str4 = "This is my First line.\nThis is my second line"
print(str4)

# 2) \t ----> for a tab space
str5 = "This is my First line.\tThis is my second line"
print(str5)

#basic Operations on Strings

# concatenation ----> Adding two strings
print(str1+str2)

# lenght of string (len(str))   ----> to find the lenght of any string  
print(len(str1))

#Example

str1 = "Abhishek"
len1 = len(str1)
print(len1)

str2 = "Adil"
len2 = len(str2)
print(len2)

final_str = str1 + " " + str2 
print(final_str)
print(len(final_str))

# Indexing ----> help in access characters
# In indexing we can only access the character , can't manipulate them
str = "Abhishek Adil"
ch = str[2]
print(ch)

# OR 

print(str[0])

# Slicing ---> Accessing parts of a string( used in ML)
# str[ starting_idx : ending_idx ]  ( ending idx is not included )

str = "Abhishek Adil"
print(str[1:4])
print(str[0:8]) 
print(str[:8])  # [0:8]
print(str[9:14])
print(str[9:len(str)])
print(str[9:]) # [9:len(str)]

# Negative Index

str = "apple"
print(str[-3:-1])
print(str[-5:-2])

# String Function

# 1) str.endswith("substring")  ---> return true if string ends with the substring
str = "I am a coder"
print(str.endswith("er"))  

# 2) str.capitalize()  ---> capitalize 1st character
   # original string me koi change nhi krta 
   # new string banata hai
str = "i am a coder"
print(str.capitalize())  # i capitalize ho jayega 

print(str) # original string print hoga

# original string ko modify krne ke liye
str = "i am a coder"
str = str.capitalize()
print(str)\

# 3) Replace function,   str.replace(old, new)  ---> replaces all occurrences of old with new

str = "I am a coder"
print(str.replace("a", "o"))
print(str.replace("coder", "hero"))

# 4) str.find("word") ---> string me perticular word hai ya nhi check krta hai
   # agar krta hai to us word ke 1st occurrence ka 1st index return krega

str = "I am a coder"
print(str.find("o"))
print(str.find("coder"))

print(str.find("q")) # q is not in the string , so it return -1 

# 5) str.count(" ") ----> counts the occurrences of a substring

str = "I am a good coder, and I write good codes"
print(str.count("good"))  #return 2
print(str.count("o"))

# /
# /
# /
# /
# /
# /
# Conditional Statements
# indentation --> space for grouping the codes  -->{}
#if- elif- else(SYNTEX)

# 1) if(condition):
#       print(Statement)  # statement is print only when the condition if satisfied
# if() ko ham kitne bhi baar likh skte hai

age = 21

if(age >= 18):
   print("Can vote, and apply for driving license") # print only when the age is greater than or equal to 18
   print("and can drive")

if(True):  # statement are print every time
   print("Can vote, and apply for driving license") 
   print("and can drive")

# ham jitne baar chahe utne baar if() ka use kr skte hai

light = "green"

if(light == "red"):
   print("stop")
if(light == "green"):
   print("can go")
if(light == "yellow"):
   print("Look")

print("your progam is completed")

# 2)if-elif
# if(condition1):
#     Statement1
# elif(condition2):
#     Statement2
# elif() ko ham kitne bhi baar likh skte hai

light = "green"

if(light == "red"):
   print("stop")
elif(light == "green"):
   print("can go")
elif(light == "yellow"): # ham jitne baar chahe elif() function ka use kr skte hai, but conditional statement hamesha if() se start hona chahiye
   print("Look")

print("your progam is completed")


# Differece in if() and elif()
# if() ---> Always check for the condition, jitne baar if() hoga utne baar check krega

#elif() ---> Check when if() condition is false, agar if() condition True hoga to elif() execute hi nhi hoga

#Examples

# 1)
num = 5

if(num > 2):
   print("Number is greater than 2")
if(num > 3):
   print("Number is greater than 3") # Both the if() condition will execute

# 2)
num = 5

if(num > 2):
   print("Number is greater than 2")
elif(num > 3): # elif() bhi true hai, but ye execute nhi hoga
   print("Number is greater than 3") # elif() execute nhi hoga kyuki if() statement True hai


# 3) else:
#     StatementN
# else ---> only use one time and at the last
#      ---> isme koi condition check nhi hoti 
#      ---> else ke upar jitne bhi conditions hai agr vo sare false ho jate hai tab else execute hoga

# Example - 1
light = "blue"

if(light == "red"):
   print("stop")
elif(light == "green"):
   print("can go")
elif(light == "yellow"): 
   print("Look")
else:
   print("Light is Broken")

print("your progam is completed")

# Example - 2 (classic if-else example)

age = 22

if(age >= 18):
   print("can vote")
else:
   print("can't vote")

# Example - 3
# Question- create a grade system based on marks
#           marks >= 90, grade = "A"
#           90 > marks >= 80, grade = "B"
#           80 > marks >= 70, grade = "C"
#           70 > marks, grade = "D"

marks = int(input("Enter the Marks: "))

if(marks >= 90):
   grade = "A"
elif(marks >= 80 and marks < 90):
   grade = "B"
elif(marks >=70 and marks < 80):
   grade = "C"
else:
   grade = "D"

print("grade of the students-> ", grade)

# Nesting - means if() ke ander if() statement likhna

age = 22

if(age >= 18):
   if(age >= 80):
      print("cannot drive")
   else:
      print("can drive")
else:
   print("can't drive")
   