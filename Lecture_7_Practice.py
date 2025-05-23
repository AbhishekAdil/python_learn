# Create a new file "practice.txt" using python. Add the following data in it:
'''
Hi everyone
we are learning File I/O
using Java
I like programming in Java.
'''

with open("practice.txt", "w") as f:
    f.write("Hi everyone\nWE are learning File I/O")
    f.write("\nusing Java\nI like programming in Java.")

# 1) WAF that replace all occurrences of "Java" with "python" in above file.
# Step1) pahale read krna hai , fir value change krna hai
# Step2) fir overwrite kr dena hai

with open("practice.txt", "r") as f:
    data = f.read()                    # Data read kiya

new_data = data.replace("Java", "python")
print(new_data)                        # value change kiye

with open("practice.txt", "w") as f:
    f.write(new_data)                  # change value ko overwrite kr diya

# 2) Search if the word "learning" exists in the file or not
def check_for_word():
    with open("practice.txt", "r") as f:
        data = f.read()

        if(data.find("learning") != -1):     # -1 is the invalid index
            print("Found")                   # print found when there is a valid index
        else:
            print("Not found")    

check_for_word()

# or

def check_for_word():
    word = "learning"
    with open("practice.txt", "r") as f:
        data = f.read()
        if(word in data):
            print("FOUND")
        else:
            print("not found")

check_for_word()

# 3) WAF to find in which line of thr filr does the word "learning" occur first.
#   Print -1 if word not found

def check_for_line():
    word = "learning"
    data = True    # stopage condition (stop searching when all the lines are search)
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1

    return -1   

check_for_line()

# or

def check_for_word():
    with open("practice.txt", "r") as f:
        line1 = f.readline()   # for reading line 1
        if(line1.find("learning") != -1):     # -1 is the invalid index
            print("Found")                   # print found when there is a valid index
        else:
            print("-1")  

        line2 = f.readline()   # for reading line 1
        if(line2.find("learning") != -1):     # -1 is the invalid index
            print("Found")                   # print found when there is a valid index
        else:
            print("-1") 

        line3 = f.readline()   # for reading line 1
        if(line3.find("learning") != -1):     # -1 is the invalid index
            print("Found")                   # print found when there is a valid index
        else:
            print("-1") 

        line4 = f.readline()   # for reading line 1
        if(line4.find("learning") != -1):     # -1 is the invalid index
            print("Found")                   # print found when there is a valid index
        else:
            print("-1") 

check_for_word()

# 4) From a file containing numbers separated by comma, print the count of even numbers.

# Step 1) pahale individual number nikalana hoga
# step 2) parse / cast to int
count = 0
with open("practice_int.txt", "r") as f:
    data = f.read()
    print(data)

    # Step 1) pahale individual number nikalana hoga(without split() method)
    # basic 
    num = ""
    for i in range(len(data)):
        if(data[i] == ","):
            print(int(num))     # type casting
            num = ""
        else:
            num += data[i]

    # or with split() method
    nums = data.split(",")   
    for val in nums:
        if(int(val) % 2 == 0):      # type casting and check the number is even or not
            count += 1
print(count)