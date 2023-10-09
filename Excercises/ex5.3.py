"""Write a program that asks the user for an integer and tells if the number is a prime number.
Prime numbers are number that are only divisible by one or the number itself.

For example, 13 is a prime number as it can only be divided by 1 or 13 so that the result is an integer.
On the other hand, 21 is not a prime number as it is divisible by 3 and 7."""
import math
number = int(input('Enter the number: '))
count = 0
for i in range(1, number+1):
    if number % i == 0:
        count += 1
if count == 2:
    print(f'{number} is a Prime number')
else:
    print(f'{number} is not a Prime number')