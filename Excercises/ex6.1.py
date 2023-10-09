"""Write a function that returns a random dice roll between 1 and 6. The function should not have any parameters.
Write a main program that rolls the dice until the result is 6. The main program should print out the result of each
roll."""

import random


def rolling():
    number = random.randint(1, 6)
    return number


start = input('Press Enter to Start')
ans = 0
while start == '' and ans != 6:
    ans = rolling()
    print(f'{ans}')
