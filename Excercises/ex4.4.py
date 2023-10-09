"""Write a game where the computer draws a random integer between 1 and 10.
 The user tries to guess the number until they guess the right number.
  After each guess the program prints out a text: Too high, Too low or Correct.
 Notice that the computer must not change the number between guesses."""
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
