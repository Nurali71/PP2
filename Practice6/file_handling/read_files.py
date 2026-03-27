# The open() function returns a file object, which has a read() method for reading the content of the file:

# Using the with statement
with open("demofile.txt", "r") as f:
    print(f.read())

# Close Files
f = open("demofile.txt")
print(f.readline())
f.close() 

# Read Only Parts of the File
with open("demofile.txt") as f:
  print(f.read(5))

# Read Lines
# You can return one line by using the readline() method:
# By calling readline() two times, you can read the two first lines:
with open("demofile.txt") as f:
  print(f.readline()) 
