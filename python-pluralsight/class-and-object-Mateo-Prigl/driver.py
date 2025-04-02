from employee import *

# Use mypy to typecheck
# p = Project("Pname","payment(int)","Cli")
p = Project()
e = Employee("emplo",24,20000,p)
# e = Employee(2,1,2,3)
print(e.project)
# print(p.__dict__)
print(p.__slots__)