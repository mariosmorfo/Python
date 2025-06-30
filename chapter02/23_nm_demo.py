class Point:
    __count = 0

    def __init__(self, x=0, y=0):
        self._x = x
        self.__y = y

    def __str__(self):
        return f"({self._x}, {self.__y})"

def main():
    p1 = Point(10, 20)
    p2 = Point(11, 20)

    print(p1)              
    print(p2)

    print(p1._x)
    print(p1.__y)
    # print(p1._Point__y)

if __name__ == '__main__':
    main()
