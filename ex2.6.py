"""Write a program that draws two random combinations of numbers for a combination lock:
a 3-digit code where each number is between 0 and 9.
a 4-digit code where each number is between 1 and 6."""
import random

print(f'{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}')
print(f'{random.randint(1,6)}{random.randint(1,6)}{random.randint(1,6)}{random.randint(1,6)}')
