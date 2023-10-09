"""Write a program that asks the user to enter numbers until they enter an empty string to quit.
 Finally, the program prints out the smallest and largest number from the numbers it received.
 """
user_input = input('Enter a number: ')
if user_input != "":
    smallest = None
    largest = None
    while user_input != "":
        number = int(user_input)
        if smallest is None or number < smallest:
            smallest = number
        if largest is None or number > largest:
            largest = number
        user_input = input('Enter a number : ')
    print(f'The smallest number is {smallest}')
    print(f'The largest number is {largest}')
else:
    print('No numbers were given')