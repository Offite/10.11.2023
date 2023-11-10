import math

class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def type(self):
        a = self.side1
        b = self.side2
        c = self.side3

        if a == b == c:
            return "равносторонний"
        elif a == b or a == c or b == c:
            return "равнобедренный"
        else:
            return "разносторонний"

    def area(self):
        s = self.semi_perimeter
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def semi_perimeter(self):
        return (self.side1 + self.side2 + self.side3) / 2