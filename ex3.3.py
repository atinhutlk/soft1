"""Write a program that asks for the biological gender and hemoglobin value (g/l).
 The program the notifies the user if the hemoglobin value is low, normal or high.

A normal hemoglobin value for adult females is between 117-155 g/l.
A normal hemoglobin value for adult males is between 134-167 g/l."""
a = str(input('Your gender: '))
b = int(input('Your hemoglobin value: '))
if a == 'female':
    if b < 117:
        print('Low')
    elif b > 155:
        print('high')
    else:
        print('normal')
if a == 'male':
    if b < 134:
        print('Low')
    elif b > 167:
        print('high')
    else:
        print('normal')