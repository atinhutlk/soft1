"""Write a program that asks the user to enter a mass in medieval units: talents (leiviskä),
pounds (naula), and lots (luoti).
 The program converts the input to full kilograms and grams and outputs the result to the user:

One talent is 20 pounds.
One pound is 32 lots.
One lot is 13,3 grams."""

a = float(input("Enter talent: "))
b = float(input("Enter pounds : "))
c = float(input("Enter lots : "))
d = (a*20*32+b*32+c)*13.3
print(f"Kilograms: {d//1000:.0f} and grams: {d%1000:.2f}")

