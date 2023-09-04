"""Write a program that asks the user how many dice to roll.
 The program rolls all the dice once and prints out the sum of the numbers. Use a for loop."""
import random
n = int(input('How many dice to roll: '))
ans = 0
for i in range(0, n):
    ans = ans + random.randint(1, 6)
print(f'Sum of the numbers: {ans}')
