""" Write a function that gets a list of integers as a parameter.
The function returns a second list that is otherwise the same as the original list except that all uneven numbers have been removed.
 For testing, write a main program where you create a list, call the function, and then print out both the original as well as the cut-down list."""

def removeOdd(lst):
    i = 0
    while i < len(lst):
        if lst[i] % 2 != 0:
            lst.pop(i)
        else:
            i += 1

numlist = []

while True:
    number =input('Enter number or Enter to Run: ')
    if number == '':
        break
    else:
        number = int(number)
        numlist.append(number)

print(f'The Original list : ', numlist)
removeOdd(numlist)
print(f'The New List: ', numlist)
