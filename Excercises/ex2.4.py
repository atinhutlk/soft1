"""Write a program that asks the user for three integer numbers
The program prints out the sum, product, and average of the numbers."""
a = float(input("Number 1: "))
b = float(input("Number 2: "))
c = float(input("Number 3: "))
print(f"Sum: {(a+b+c):.2f}")
print(f"Product: {(a*b*c):.2f}")
print(f"Average: {(a+b+c)/3:.2f}")