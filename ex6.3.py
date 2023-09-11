"""Write a function that gets the quantity of gasoline in American gallons and returns the number converted to litres.
Write a main program that asks for a volume in gallons from the user and converts the value to liters.
The conversion must be done by using the function. Conversions continue until the user inputs a negative value.
"""

def convert(gallon):
    gasoline = gallon*3.78541178
    return gasoline

number = float(input('Gallon: '))
while number > 0:
    print(f'{convert(number):.2f}')
    number = float(input('Gallon: '))
print(f'Thank you')