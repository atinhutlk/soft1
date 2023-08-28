"""
Write a program that asks the user for the length and width of a rectangle.
The program then prints out the perimeter and area of the rectangle.
The perimeter of a rectangle is the sum of the lengths of each four sides.
"""

a = float(input('Length :'))
b = float(input('Width :'))
perimeter = (a+b)*2
print(f"The perimeter : {perimeter:.2f}")