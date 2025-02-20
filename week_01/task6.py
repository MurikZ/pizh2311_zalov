class Rectangle:
    def __init__(self, width, height):
        self.__w = Rectangle.__test(width)
        self.__h = Rectangle.__test(height)
        print(self)

    def set_width(self, width):
        self.__w = Rectangle.__test(width)

    def set_height(self, height):
        self.__h = Rectangle.__test(height)

    def get_width(self):
        return self.__w

    def get_height(self):
        return self.__h

    @staticmethod
    def __test(value):
        return abs(value)

    def __str__(self):
        return "Rectangle {0}x{1}".format(self.__w, self.__h)


a = Rectangle(3, 4)
print(a.get_width())
a.set_width(5)
print(a)

b = Rectangle(-2, 4)
print(b)