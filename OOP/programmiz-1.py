# class trianlge
# 3 atributes a b c
# object
# triangle class has two methods: init and to calculate perimeter
# perimeter should be printed

class Triangle():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate(self):
        perimeter = self.a + self.b + self.c
        print("Perimeter of your triangle is",perimeter)

triangle1 = Triangle(15, 20, 35)

triangle1.calculate()

