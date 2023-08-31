"""Write a program that asks the user to enter numbers until they enter an empty string to quit.
 Finally, the program prints out the smallest and largest number from the numbers it received.
 """
smallest = None
largest = None
while True:
    number = input('Enter number: ')
    if number == "":
        break
    if smallest is None or number < smallest:
        smallest = number
    if largest is None or number > largest:
        largest = number
print(f'The smallest number is {smallest}')
print(f'The largest number is {largest}')
