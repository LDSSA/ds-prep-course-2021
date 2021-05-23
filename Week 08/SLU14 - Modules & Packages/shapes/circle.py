import math

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi*math.sqrt(self.radius)

    def get_perimeter(self):
        return 2*math.pi*self.radius

if __name__ == "__main__":
    obj_circle = Circle(20)
    print("Area is {} and perimeter is {}".format(obj_circle.get_area(), obj_circle.get_perimeter()))
