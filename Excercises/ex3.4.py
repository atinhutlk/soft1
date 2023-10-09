"""Write a program that asks the user to enter a year and notifies the user
whether the input year is a leap year. A year is a leap year if it is divisible by four.
However, years divisible by 100 are leap years only if they are also divisible by 400."""
a = int(input('Year: '))
if (a % 4 == 0) or (a % 100 == 0 and a % 400 == 0):
    print(f'{a} is a leap year')
else:
    print(f'{a} is not a leap year')