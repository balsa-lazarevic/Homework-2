from math import pow, sqrt

class Line:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def slope(self):
        x1, x2 = self.__a[0], self.__b[0]
        y1, y2 = self.__a[1], self.__b[1]
        result = (y2 - y1)/(x2 - x1)
        return result

    def distance(self):
        x1, x2 = self.__a[0], self.__b[0]
        y1, y2 = self.__a[1], self.__b[1]
        result = pow((x2 - x1), 2) + pow((y2 - y1), 2)
        result = sqrt(result)

        return result
    
linija = Line((3, 2), (8, 10))

print(linija.slope())
print(linija.distance())