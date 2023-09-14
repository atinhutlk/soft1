"""Write a function that gets a list of integers as a parameter.
The function returns the sum of all the numbers in the list.
For testing, write a main program where you create a list, call the function, and print out the value it returned.
"""


def sumoflist(array):
    ans = 0
    for i in range(len(array)):
        ans += array[i]
    return ans

numlist = []
while True:
    number =input('Enter number or Enter to Run the program: ')
    if number == '':
        break
    else:
        number = int(number)
        numlist.append(number)
result = sumoflist(numlist)
print(f'Sum of the number: {result}')
