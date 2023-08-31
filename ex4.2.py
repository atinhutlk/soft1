"""Write a program that converts inches to centimeters until the user inputs a negative value
 Then the program ends.
"""
n = float(input('Enter Inches: '))
while n >= 0:
    print(f'{n} in Centimeter is: {n*2.54}')
    n = float(input('Enter Inches: '))
print(f'Wrong input')