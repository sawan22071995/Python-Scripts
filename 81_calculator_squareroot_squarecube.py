class Calculator:
    def __init__(self,num):
        self.num = num
    def SquareRoot(self):
        for i in range(self.num):
            square = i*i
            if self.num == square:
                return i
    def SquareCube(self):
        for i in range(self.num):
            cube = i*i*i
            if self.num == cube:
                return i
    def Square(self):
        print(f"The value of {self.num} is {self.num **2}")
    def Cube(self):
        print(f"The cube of {self.num} is {self.num **3}")
    def squareroot(self):
        print(f"The value of {self.num} is {self.num **0.5}")

number = int(input("Enter the number for square root and square cube:"))
cal = Calculator(number)
squareroot = cal.SquareRoot()
squarecube = cal.SquareCube()

print(f"The squareroot of {number} is {squareroot}")
print(f"The squarecube of {number} is {squarecube}")
cal.Square()
cal.Cube()
cal.squareroot()

