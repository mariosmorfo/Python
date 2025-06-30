class Point:
    __count = 0

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
        Point.__count += 1

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def __repr__(self):
        return f"Point(x={self.__x}, y={self.__y})"

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.__x == other.__x and self.__y == other.__y
        return False

    @classmethod
    def get_count(cls):
        return cls.__count

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value



def main():
    p1 = Point(10, 20)
    p2 = Point(11, 20)

    print(p1)              # Calls __str__
    print(p2)
    print(f"p1 == p2: {p1 == p2}")  # Calls __eq__
    print(f"Total Points: {Point.get_count()}")


if __name__ == '__main__':
    main()
