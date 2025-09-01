import math

def calculate_circle_area(radius):
    """
    Обчислює площу кола за заданим радіусом.

    Args:
        radius (float): Радіус кола.

    Returns:
         float: Площа кола.
    """
    return (radius ** 2) * math.pi

radius = float(input("Circle radius:"))
area = calculate_circle_area(radius)

print(f"The area of the circle with radius {radius} is: {area:.2f}")

