# Write a Python program to convert degree to radian.
import math
n=float(input())
radian=n*(math.pi/180)
print(f"{radian:.6f}")
# Write a Python program to calculate the area of a trapezoid.
import math
high=float(input())
base_1=float(input())
base_2=float(input())
area=(base_1+base_2)*high/2
print(f"{area:.1f}")
# Write a Python program to calculate the area of regular polygon.
import math
side=int(input())
lenght=float(input())
area=(side*lenght**2)/(4*math.tan(math.pi/side))
print(f"{area}")
# Write a Python program to calculate the area of a parallelogram.
import math
a=float(input())
h=float(input())
area=a*h
print(f"{area}")