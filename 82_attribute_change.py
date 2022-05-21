class a:
    a = 'a'

    @staticmethod
    def greet():
        return f"Hello User"
a = a()
a.a = 0
print(a.a)
print(a.greet())