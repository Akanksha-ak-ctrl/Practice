from abc import ABC, abstractmethod

# Abstract class representing a Shape
class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Concrete subclass representing a Circle
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Concrete subclass representing a Rectangle
class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Function to display information about a shape
def display_shape_info(shape):
    print("Shape color:", shape.color)
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())

# Creating objects of Circle and Rectangle
circle = Circle("Red", 5)
rectangle = Rectangle("Blue", 4, 6)

# Displaying information about the shapes
print("Circle:")
display_shape_info(circle)
print("\nRectangle:")
display_shape_info(rectangle)
