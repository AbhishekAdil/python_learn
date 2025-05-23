# 1) WAP to ask the user to enter names of their 3 favorite movies & store them in a list.

a = input("Enter your first favorite Movie: ") 
b = input("Enter your second favorite Movie: ")
c = input("Enter your third favorite Movie: ")

list = [a, b, c]
print(list)

# or

movies = [] # create a empty list

# using multiple variable
mov1 = input("enter 1st movie: ")
mov2 = input("enter 2nd movie: ")
mov3 = input("enter 3rd movie: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

# or

movies = [] # create a empty list

# using single variable
mov = input("enter 1st movie: ")
movies.append(mov)
mov = input("enter 2nd movie: ")
movies.append(mov)
mov = input("enter 3rd movie: ")
movies.append(mov)

print(movies)

# or
movies = []

# no variable
movies.append(input("enter 1st movie: "))
movies.append(input("enter 2nd movie: "))
movies.append(input("enter 3rd movie: "))

print(movies)


# 2) WAP to check if a list contains a palindrome of elements or not.
# (HINT : use copy() method)
# palindrome  [1, 2, 3, 2, 1]  or  [1, "abc", "abc", 1]
'''
method ---> Step1) Make a copy of the list
            Step2) Reverse the copied list
            Step3) check if the reversed and the origianl lists are same
'''
# example 1
list1 = [1, 2, 1]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("Palindrome")
else:
    print("not pelindrome")
# return Palindrome

#example 2
list1 = ["m", "a", "a", "m"]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("Palindrome")
else:
    print("not pelindrome")
# return Palindrome


#example 3
list2 = [1, 2, 3]

copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list2 == list2):
    print("Palindrome")
else:
    print("not pelindrome")
# return not palindrome

# example 4
list1 = ["m", "a", "a", "m", "p"]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("Palindrome")
else:
    print("not pelindrome")
# return not palindrome

# 3) WAP to count the number of students with the "A" grade in the following tuple.
#    ["C", "D", "A", "A", "B", "B", "A"]

tup = ("C", "D", "A", "A", "B", "B", "A")
print("Number of students with the A grade is: ", tup.count("A"))

# 4) Store the above value in a list & sort them from "A" to "D". 

list = ["C", "D", "A", "A", "B", "B", "A"]
list.sort()
print("sorted tuple: ", list)