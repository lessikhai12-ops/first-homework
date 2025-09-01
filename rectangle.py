class Rectangle:
    """Клас для представлення прямокутника."""

    def __init__(self, width, height):
        """Ініціалізує прямокутник з заданою шириною та висотою."""
        self.width = width
        self.height = height

    def area(self):
        """Повертає площу прямокутника."""
        return self.width * self.height

    def perimeter(self):
        """Повертає периметр прямокутника."""
        return 2 * (self.width + self.height)

    def is_square(self):
        """
        Перевіряє, чи є прямокутник квадратом.

        Returns:
          bool: True, якщо прямокутник квадрат, інакше False.
        """
        return self.width == self.height

    def resize(self, new_width, new_height):
        """
        Змінює розміри прямокутника.

            Args:
                new_width (float): Нова ширина.
                new_height (float): Нова висота.
                """
        self.width = new_width
        self.height = new_height


rect = Rectangle(2, 5)
print("Width:", rect.width)
print("Height:", rect.height)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())
print("Square?", rect.is_square())

rect.resize(5, 5)
print("\nParameters have been changed")
print("New Width:", rect.width)
print("New Height:", rect.height)
print("New Area:", rect.area())
print("New Perimeter:", rect.perimeter())
print("Square?", rect.is_square())



