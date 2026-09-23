class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"{self.width} x {self.height}"

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


rectangle = Rectangle(10, 5)

print(rectangle)              # 10 x 5
print(rectangle.area())       # 50
print(rectangle.perimeter())  # 30
