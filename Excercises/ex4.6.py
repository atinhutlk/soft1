import random

num_points = int(input("Enter the number of random points to generate: "))
inside_circle = 0
point_number = 0

while point_number < num_points:
    x = random.randint(-1, 1)
    y = random.randint(-1, 1)

    if x ** 2 + y ** 2 < 1:
        inside_circle += 1

    point_number += 1

approx_pi = 4 * inside_circle / num_points
print(f"Approximation of π using {num_points} random points: {approx_pi}")
