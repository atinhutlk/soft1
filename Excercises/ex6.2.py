"""Modify the function above so that it gets the number of sides on the dice as a parameter.
 With the modified function you can for example roll a 21-sided role-playing dice.
 The difference to the last exercise is that the dice rolling in the main program continues
 until the program gets the maximum number on the dice, which is asked from the user at the beginning."""


import random


def rolling(num):
    number = random.randint(1, num)
    return number

sides = int(input('Number of side: '))
start = input('Press Enter to Start')
ans = 0
while start == '' and ans != sides:
    ans = rolling(sides)
    print(f'{ans}')
