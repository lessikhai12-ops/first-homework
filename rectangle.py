class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        if self.width == self.height:
         return "Yes"
        else:
            return "No"

    def resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height

rect = Rectangle(2,5)
print("Width:", rect.width)
print("Height:", rect.height)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())
print("Is it a square?", rect.is_square())

rect.resize(5,5)
print("\nParameters has been changed")
print("New Width:", rect.width)
print("New Height:", rect.height)
print("New Area:", rect.area())
print("New Perimeter:", rect.perimeter())
print("Is it a square now?", rect.is_square())



