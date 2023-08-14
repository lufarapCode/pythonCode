"""from pyodide.http import pyfetch
import pandas as pd

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt"

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())


await download(filename, "Example1.txt")"""

from msilib.schema import File


example1 = "a.txt"
file1 = open(example1, "r")

#print(file1.name)
#print(file1.mode)

FileContent = file1.read()
#print(FileContent)

#print(type(FileContent))

# A Better Way to Open a File

with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)


# Verify if the file is closed

file1.closed

# See the content of file

print(FileContent)

with open(example1, "r") as file1:
    print(file1.read(4))

with open(example1, "r") as file1:
    print(file1.read(4))
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))

# Read one line

with open(example1, "r") as file1:
    print("first line: " + file1.readline())

# We can also pass an argument to  readline()  to specify the number of charecters
# we want to read. However, unlike  read(),  readline() can only read one line at most.

with open(example1, "r") as file1:
    print("A: " + file1.readline(20)) # does not read past the end of line
    print("B: " + file1.read(20)) # Returns the next 20 chars


# Iterate through the lines

with open(example1,"r") as file1:
        i = 0
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1

# Read all lines and save as a list

with open(example1, "r") as file1:
    FileasList = file1.readlines()
    print (FileasList[3])
file1.closed


print("**************************************************")
exmp2 = 'ejemplo2.txt'

with open(exmp2, 'w') as writefile:
    writefile.write("This is line W")



with open(exmp2, 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")

Lines = ["This is line A\n", "This is line B\n", "This is line Ca\n"]

with open('Example2.txt', 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)

with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())


# Appending Files¶
# We can write to files without losing any of the existing 
# data as follows by setting the mode argument to append: a. you can append a new line as follows:

with open('Example2.txt', 'a') as testwritefile:
    testwritefile.write("This is line C\n")
    testwritefile.write("This is line D\n")
    testwritefile.write("This is line E\n")

with open('ejemplo  .txt', 'a+') as testwritefile:
    testwritefile.write("This is line E\n")
    print(testwritefile.read())

"""
Most of the file methods we've looked at work in a certain location in the file. .write()  writes at a certain
 location in the file. .read() reads at a certain location in the file and so on. You can think of this as moving your pointer around in the notepad to make changes at specific location.

Opening the file in w is akin to opening the .txt file, moving your cursor to the beginning of the text file,
 writing new text and deleting everything that follows. Whereas opening the file in a is similiar to opening the .txt 
 file, moving your cursor to the very end and then adding the new pieces of text.
It is often very useful to know where the 'cursor' is in a file and be able to control it. The following methods 
allow us to do precisely this -

.tell() - returns the current position in bytes
.seek(offset,from) - changes the position by 'offset' bytes with respect to 'from'. From can take the value of 0,1,2 corresponding to beginning, relative to current position and end

Now lets revisit a+
"""

with open('Example3.txt', 'a+') as testwritefile:
    print("Initial Location: {}".format(testwritefile.tell()))
    
    data = testwritefile.read()
    if (not data):  #empty strings return false in python
            print('Read nothing') 
    else: 
            print(testwritefile.read())
            
    testwritefile.seek(0,0) # move 0 bytes from beginning.
    
    print("\nNew Location : {}".format(testwritefile.tell()))
    data = testwritefile.read()
    if (not data): 
            print('Read nothing') 
    else: 
            print(data)
    
    print("Location after read: {}".format(testwritefile.tell()) )

with open('Example3.txt', 'r+') as testwritefile:
    data = testwritefile.readlines()
    testwritefile.seek(0,0) #write at beginning of file
   
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("finished\n")
    #Uncomment the line below
    #testwritefile.truncate()
    testwritefile.seek(0,0)
    print(testwritefile.read())

"""
Copy a File






Let's copy the file Example2.txt to the file Example3.txt:
"""
    
with open('Example2.txt','r') as readfile:
    with open('Example3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)

# Verify if the copy is successfully executed

with open('Example3.txt','r') as testwritefile:
    print(testwritefile.read())