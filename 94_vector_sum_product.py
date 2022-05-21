class vector:
    def __init__(self,vec):
        self.vec = vec

    def __add__(self,vec2):
        if vector.status(self,vec2) ==  True:
            newlist = []
            for i in range(len(self.vec)):
                newlist.append(self.vec[i]+ vec2.vec[i])        
            return vector(newlist)
        else:
            return f"Vector length mismatch..Addition of vector not possible"
    
    def __mul__(self,vec2):
        if vector.status(self,vec2) ==  True:
            sum = 0
            for i in range(len(self.vec)):
                sum += self.vec[i] * vec2.vec[i]        
            return sum
        else:
            return f"Vector length mismatch..Multiplication of vector not possible"
    def __str__(self):
        str = ""
        index = 0
        for i in self.vec:
            str += f" {i}a{index} +"
            index +=1
        return str[:-1]

    def __len__(self):
        return len(self.vec)
    
    def status(self,vec2):
        if len(self.vec)==len(vec2.vec):
            return True
        else:
            return False
        


v1 = vector([1,4,6,9])
v2 = vector([1,6,9])
print(v1+v2)
print(v1*v2) #vector dot product/multiplication is vector quantity
print(f"The length of vector 1 : {len(v1)}")
print(f"The length of vector 2 : {len(v2)}")
