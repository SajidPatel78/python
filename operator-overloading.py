class vector:
    def init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'vector (%d, %d)' % (self.a, self.b)
    def __add__(self, other):
        return vector(self.a + other.a, self.b + other.b)
        v1 = vector(2, 10)
        v2 = vector(5, -2)
    print(v1 + v2)

class a:
    def x(self):
        print('x of a called')

class b(a):
    def x(self):
        print('x of b called')
        super().x()

class c(a):
    def x(self):
        print('x of c called')
        super().x()

class d(b, c):
    def x(self):
        print('x of d called')
        super().x()


from super5 import D
y = D()
y.x()
