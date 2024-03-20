class Rectangle:
    def __init__(self, hight, widht):
        self.hight = hight
        self.widht = widht

    def calcul_area(self):
        s = self.hight * self.widht
        return s


area = Rectangle(5, 5)
print(area.calcul_area())
