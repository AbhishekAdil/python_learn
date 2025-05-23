# file input/output
# Python can be used to perform operations on a file.(read and write data)
'''
Major Opearations:
1) Open a file
2) Read a file
3) Write something in the file
4) Close the file
5) at last delete the file
'''

'''
Types of all files.
1) Text File(Data store in tha form of characters) : .txt, .docx, .log etc.
2) Binary Files(non text files) : .mp4, .mov, .png , .jpeg etc.

# All the files are stored in Bits(0,1) in the memory
'''

# Open, read, and close file:-
# We have to open a file before reading or writing.
'''
f = open("file_name", "mode")   ; mode -> r:read mode or w: write mode  (by default read mode)
# file_name -> if file is not in the same folder, we have to write the complete path of the file

data = f.read()   # for read the data of the file

f.close()         # close the opened file
'''

f = open("demo.txt", "r")      # r-> read mode

data = f.read()
print(data)        #I am Abhishek
                   #learing python
print(type(data))  #<class 'str'>

f.close()     

# Different modes in file i/o
'''
File input/output (I/O) operations in Python involve reading data from and writing data to files. 
The open() function is central to these operations, taking two primary arguments: the file name and 
the mode. The mode specifies the operation to be performed on the file.

'r' (Read):
This is the default mode. It opens the file for reading. If the file does not exist, 
it raises an error.

'w' (Write):
It opens the file for writing. If the file exists, it overwrites the content. 
If the file does not exist, it creates a new file.

'a' (Append):
It opens the file for appending. If the file exists, new data is written at the end. 
If the file does not exist, it creates a new file.

'x' (Exclusive Creation):
It creates a new file. If the file already exists, it raises an error.

'b' (Binary):
This mode is used for binary files like images or audio. 
It can be combined with other modes like 'rb' (read binary) or 'wb' (write binary). 

't' (Text):
This is the default mode for text files. It can be combined with other modes like 'rt' (read text) 
or 'wt' (write text).

'+':
This mode allows both reading and writing. For example, 'r+' opens the file for reading and writing, 
while 'w+' opens it for writing and reading (truncating the file first). 
'a+' opens the file for appending and reading.


These modes can be combined to specify the desired operation and file type. 
For example, 'rb' opens a file for reading in binary mode, while 'wt' opens a file for writing in 
text mode.
'''

# Reading a file
'''
data = f.read()   # read entire file
data = f.readline() # read one line at a time
'''

# For reading perticulat characters

f = open("demo.txt", "r")      

data = f.read(5)   # for printing only 5 characters from the starting
print(data)        # I am

f.close()

# for reading a single line

f = open("demo.txt", "r")      

line1 = f.readline()   # for reading line 1
print(line1)           # I am Abhishek(give space beacause of  default /n for the line change)

line2 = f.readline()   # for reading line 2
print(line2)           # learing python

f.close()

# Ek baar data read ho jaye to firse usko read nhi krwa skte (in the same execution)

f = open("demo.txt", "r")  

data = f.read()
print(data)
''' output
I am Abhishek
learing python
'''

line1 = f.readline()   
print(line1)           # show blank spaces , beacause data is already read above
                       # ek baar read krne ke baad file khali ho jati hai
line2 = f.readline()   
print(line2)           # show blank spaces

f.close()

# Writing to a file
'''
f = open("demo.txt", "w")
f.write("this is a new line")  # overwrites the entire file

f = open("demo.txt", "a")      # append
f.write("this is a new line")  # adds to the file
'''
# overwrite in the file

f = open("demo.txt", "w")
data = f.write("this is a new line")
# this will change the whole text of the file to 'this is a new line'
#onli givr ---> this is a new line
f.close()

# add text add the end 

f = open("demo.txt", "a")
data = f.write("\nthis is a new line")
# this will give:
'''I am Abhishek
learing python
this is a new line'''
f.close()

# if file is not exist and we call is for write(w) or append(a), it automatically creates the file
# for write
f = open("sample.txt", "w")
f.close()        # it creates the file name as sample.txt

# same goes for append
f = open("sample.txt", "a")
f.close() 

# to overwrite the file from starting 
f = open("demo.txt", "r+")
f.write("abc")          # abc will write at the starting of tha file
print(f.read())         # print the updated file with abc
f.close()   

# file ko pahale pura blank krke read ya write krne ke liye

f = open("demo.txt", "w+")
print(f.read())        # print blank
f.write("abc")         # abc bs write hoga
f.close() 

# file ko read krke end me data add krenge

f = open("demo.txt", "a+")
print(f.read())        # print blank
f.write("abc")         # abc end me add ho jayega
f.close()

'''
r+  --> read + overwite existing data (pointer at start) ; no truncate

w+  --> read + overwrite  ; truncate

a+  --> read + append (pointer at end)  ; no truncate
'''

# with Syntax
'''
with open("demo.txt", "a") as f:
    data = f.read()
'''

#simple code for opening , reading and closing a file

with open("demo.txt", "r") as f:
    data = f.read()
    print(data)
    #f.close()    
# closing is not important in with syntax, it automatically do it

# for write
with open("demo.txt", "w") as f:
    f.write("new data")

# Deleting a File:- using the os module
''' Module(like a code library) is a file written by another programmer that generally has a function we can use.
import os
os.remove(filename)
'''

import os
os.remove("sample.txt")   # sample.txt file is deleted