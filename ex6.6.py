"""Write a function that receives two parameters: the diameter of a round pizza in centimeters and the price
of the pizza in euros.
The function calculates and returns the unit price of the pizza per square meter.
The main program asks the user to enter the diameter and
price of two pizzas and tells the user which pizza provides better value for money (which of them has a lower unit price).
 You must use the function you wrote for calculating the unit prices."""

def calculateUP(diameter, price):
    radius = diameter/200
    area = 3.14159 * (radius ** 2)
    ans = price/radius
    return ans

diameter1 = float(input('Diameter of the 1st pizza: '))
price1 = float(input('Price of the 1st pizaa: '))
diameter2 = float(input('Diameter of the 2nd pizza: '))
price2 = float(input('Price of the 2nd pizaa: '))

pizza1 = calculateUP(diameter1,price1)
pizza2 = calculateUP(diameter2,price2)

if pizza1 < pizza2:
    print(f'The first pizza is the better deal')
else:
    print(f'The second pizza is the better deal')