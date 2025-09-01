from math import *
def calculate_circle_area(radius):
    return (radius**2)*pi

radius = float(input("Circle radius:"))
area = calculate_circle_area(radius)

print(f"The area of the circle with radius {radius} is: {area:.2f}")

