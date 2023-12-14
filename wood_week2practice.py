# Derek Wood
# 2B
# December 14, 2023

# The program should tell the user the area of a choice shape with user inputs of the dimensions.

print("Area of Shapes Python Calculator")
print("----------------------------------")

print("Select an option")
print("1. Area of a square")
print("2. Area of a rectangle")
print("3. Area of a triangle")
print("4. Area of a circle")
print("5. Area of a trapezoid")

# This block of code makes it so the user HAS to input 1, 2, 3, 4, or 5, or the program will exit

import math

try:
    choice = int(input("Select your choice(1/2/3/4/5): "))
except ValueError:
    print("Invalid input!")
    exit()

def area_of_square():
    if choice == 1:
        side_length = float(input("Enter the side length of the square: "))
        if side_length < 0:
            print("Invalid input!")
        else:
            area = side_length * side_length
            print(f"Area: {area}")
        
def area_of_rectangle():
    if choice == 2:
        base = float(input("Enter the base of the rectangle: "))
        height = float(input("Enter the height length of the rectangle: "))
        if base < 0:
            print("Invalid input!")
        elif height < 0:
            print("Invalid input")
        else:
            area = base * height
            print(f"Area: {area}")      

def area_of_triangle():
    if choice == 3:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        if base < 0:
            print("Invalid Input")
        elif height < 0:
            print("Invalid Input")
        else:
            area = (base * height) // 2
            print(f"Area: {area}")

def area_of_circle():
    if choice == 4:
        radius = float(input("Enter the radius of the circle: "))
        if radius < 0:
            print("Invalid Input")
        else:
            area = math.pi * radius ** 2
            print(f"Area: {area}")
    
def area_of_trapezoid():
    if choice == 5:
        base1 = float(input("Enter the first base of the trapezoid: "))
        base2 = float(input("Enter the second base of the trapezoid: "))
        height = float(input("Enter the height of the trapezoid: "))
        if base1 < 0:
            print("Invalid Input")
        elif base2 < 0:
            print("Invalid Input")
        else:
            area = [(base1 + base2) * height] // 2
            print(f"Area: {area}")
while True:
    area_of_square()
    area_of_rectangle()
    area_of_triangle()
    area_of_circle()
    area_of_trapezoid()
    break