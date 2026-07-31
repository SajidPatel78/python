class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def Test(self):
        print(self.r + self.i)

x = Complex(3.0, -4.0)
print(x.Test())
print(x.r, x.i)

