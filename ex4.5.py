"""Write a program that asks the user for a username and password.
 If either or both are incorrect, the program ask the user to enter the username and password again.
 This continues until the login information is correct or wrong credentials have been entered five times.
 If the information is correct, the program prints out Welcome.
 After five failed attempts the program prints out Access denied.
 The correct username is python and password rules."""

username = input('Username: ')
password = input('Password: ')
count = 0
while True:
    if username == str('python') and password == str('rules'):
        print('Welcome!')
        break
    if count == 5:
        print('Access denied')
        break
    if username != str('python') or password != str('rules'):
        count += 1
        username = input('Username: ')
        password = input('Password: ')
