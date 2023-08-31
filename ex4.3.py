"""Write a program that asks the user to enter numbers until they enter an empty string to quit.
 Finally, the program prints out the smallest and largest number from the numbers it received.
import random
num= int(input('Enter the number: '))
mainNum = random.randint(1, 100)
while num != mainNum:
    if num < mainNum:
        print('Too Low')
        num = int(input('Enter the number: '))
    if num > mainNum:
        print('Too High')
        num = int(input('Enter the number: '))
print(f'The number is: {mainNum}')
"""

n = int(input('Please type the number: '))
count = 1
while count != n:
    if n <= 0 :
        break
    else:
        ans = count * (count+1)
        count += 1
if n <= 0:
    print('Thanks and bye!')
else:
    print(f' the Fractional is {ans}')