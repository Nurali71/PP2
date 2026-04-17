#To create a class, use the keyword class:
class MyClass:
  x = 5
#Create an object named p1, and print the value of x:
p1 = MyClass()
print(p1.x)
#Multiple Objects
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)
#The pass Statement
#class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.
class Person:
  pass


