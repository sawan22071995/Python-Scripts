class pets:
    pass
class animal(pets):
    name = 'dog'
    def getdetails(self):
        return f"the animal name is {self.name}"
class dog(animal):
    sound = 'bark'
    def getdetails(self):
        super().getdetails()
        return f"the animal {self.name} is {self.sound}"

d = dog()
print(d.getdetails())
    