# 1) Store following word meanings in a python dictionary:
'''
table : "a piece of furniture",
"list of facts and figures"
cat : "a small animal"
'''

dict = {
    "table" : ["a piece of furniture", "list of facts and figures"],
    "cat" : "a small animal" 
}
print(dict)


# 2) Question
'''You are given a list of subjects for students. Assume one classroom is requires for 1 subject.
How many classrooms are needed by all students.
"python", "java", "C++", "python" , "javascript", "java", "python", "java", "C++", "C"
'''
# create a set of the subjects
set_of_subjects = {"python", "java", "C++", "python" , "javascript", "java", "python", "java", "C++", "C"}
print("Number of classrooms needed : ", len(set_of_subjects))  # return Number of classrooms needed : 5
#len(set_of_subjects) --> gives number of all unique subjects

# 3) 
'''WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty
dictionary and Add one by one. Use Subject name as key and marks as value.
'''

marks = {}

x = int(input("enter phy : "))
marks.update({"phy" : x})

x = int(input("enter maths : "))
marks.update({"maths" : x})

x = int(input("enter chem : "))
marks.update({"chem" : x})

print(marks)
# Output
'''
enter phy : 66
enter maths : 44
enter chem : 88
{'phy': 66, 'maths': 44, 'chem': 88}
'''

# 4) Figure out a way to store 9 & 9.0  as seperate values in the set.
# (You can take help of built-in data types)
''' understand
values = {9, 9.0}
print(values)     #{9} python understand 9 and 9.0 as same

values = {9, 9.25}
print(values)     #{9, 9.25}

values = {9, 9.25, 8, 8.0}
print(values)     #{8, 9, 9.25}
'''
values = {9, "9.0"}
print(values)     # {9, '9.0'}

#or using built-in data types
# 9 --> int
# 9.0 --> float

values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)    # return {('float', 9.0), ('int', 9)}