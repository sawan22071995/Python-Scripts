# recursion demonstration

def factorial_iter(number):
    if number == 1 or number == 1:
        return 1
    return number*factorial_iter(number-1)

f = factorial_iter(5)
print(f)

