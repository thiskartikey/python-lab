from abc import ABC, abstractmethod

class BaseShape(ABC):
    @abstractmethod
    def area(self):
        pass


class Vector2D(BaseShape):
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

    def area(self):
        return abs(self.coord_x * self.coord_y)

    def __add__(self, other):
        return Vector2D(self.coord_x + other.coord_x, self.coord_y + other.coord_y)

    def __eq__(self, other):
        return self.coord_x == other.coord_x and self.coord_y == other.coord_y

    def __lt__(self, other):
        return self.area() < other.area()

    def __str__(self):
        return f"({self.coord_x}, {self.coord_y})"


vec1 = Vector2D(3, 4)
vec2 = Vector2D(2, 5)
vec3 = vec1 + vec2

print("Vector 1:", vec1)
print("Vector 2:", vec2)
print("Addition:", vec3)
print("Area of Vector 1:", vec1.area())
print("Area of Vector 2:", vec2.area())
print("Are vectors equal?", vec1 == vec2)
print("Is Vector 1 smaller?", vec1 < vec2)
