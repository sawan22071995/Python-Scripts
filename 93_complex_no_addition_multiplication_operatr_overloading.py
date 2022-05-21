#(a+bi)(c+di) = (ac-bd) + (ad+bc)
class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i
    def __add__(self,c):
        return Complex(self.r + c.r,self.i + c.i)
    
    def __mul__(self,c):
        mulreal = self.r*c.r - self.i*c.i
        mulimgi = self.r*c.i + self.i*c.r
        return Complex(mulreal,mulimgi)

    def __str__(self):
        return f"{self.r} + {self.i}i"

c1 = Complex(3,2)
c2 = Complex(1,7)
print(c1+c2)
print(c1*c2)
