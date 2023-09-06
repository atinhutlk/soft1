"""Write a program that asks the user to enter numbers until they input an empty string to quit.
At the end, the program prints out the five greatest numbers sorted in descending order.
Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument."""

arr = []

while True:
    number = input('Enter number (or press Enter to quit): ')

    if number == '':
        break
    else:
        number = int(number)
        arr.append(number)
arr.sort(reverse=True)

print('The five greatest numbers are:')
for i in range(0, 5):
    print(arr[i])
