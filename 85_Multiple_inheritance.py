class Employee:
    company = 'tcs'
class Language:
    Language = 'python'
class newjoinee(Employee,Language):
    name = 'sawan'
nj = newjoinee()
print(nj.company)   #inherit from Employee class
print(nj.Language)  #inherit from Language class
print(nj.name)

