# Alexander Powell
# ajpowell@email.wm.edu
# (804) 564-6153
# Proj1.py

# This program performs calculations of area, perimeter, volume, and surface
# area of a triangle and a cone.  It first prompts the user to enter values for 
# the radius and height of a triangle.  Using those values and the formulae 
# below, it calculates the area and perimeter of the right triangle created from
# those two values as well as the volume and surface area of the cone created by
# rotating that right triangle around the axis that is the side (height) of
# the triangle.  

# Import necessary libraries and prompt user to enter values
import math

radius = float(input("What is the radius of the triangle? "))
print(radius)
height = float(input("What is the height of the triangle? "))
print(height)

# Formulae for right triangle and cone
perimeter = radius + height + math.sqrt(radius ** 2 + height ** 2)
area = (radius * height) / 2

surface_area = math.pi * radius * (radius + math.sqrt(radius ** 2 + height ** 2))
volume = (math.pi * (radius ** 2) * height) / 3

# Print Results
print()
print("-----------------------------------------")
print()
print("{:>25} {:}   {:>10.3f}".format("The triangle's radius","=",radius))
print("{:>25} {:}   {:>10.3f}".format("The triangle's height","=",height))
print("{:>25} {:}   {:>10.3f}".format("The triangle's area","=",area))
print("{:>25} {:}   {:>10.3f}".format("The triangle's perimeter","=",perimeter))
print("{:>25} {:}   {:>10.3f}".format("The cone's volume","=",volume))
print("{:>25} {:}   {:>10.3f}".format("The cone's surface area","=",surface_area))
print()
print("-----------------------------------------")
print()
print("Thank you for using this program.")