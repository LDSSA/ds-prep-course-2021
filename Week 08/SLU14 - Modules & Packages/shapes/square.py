
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.height*self.width

    def get_perimeter(self):
        return 2*self.height + 2*self.width



class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)


def return_me_true_is_square_false_otherwise(width, height):
    if width == height:
        return True
    else:
        False


side = 20

if __name__ == "__main__":
    square = Square(side)
    print("Area is {} and perimeter is {}".format(square.get_area(), square.get_perimeter()))



