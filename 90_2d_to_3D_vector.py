class vec2d:
    def __init__(self,i,j):
        self.i = i
        self.j = j
    def __str__(self):
        return f"{self.i}i + {self.j}j"

class vec3d(vec2d):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

d2 = vec2d(1,3)
d3 = vec3d(1,9,7)
print(d2)
print(d3)