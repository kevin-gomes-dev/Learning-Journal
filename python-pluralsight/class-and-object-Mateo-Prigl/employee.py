# Super class in hierarchy
class Employee():
    __slots__ = ("name","salary")
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def increase_salary(self,percent):
        self.salary += self.salary * (percent/100)
        
    def has_slots(self):
        print("In employee")
        return hasattr(self,"__slots__")

# Parent: Employee
class Tester(Employee):
    def run_tests(self):
        print(f'Testing started by {self.name}...')
        print('Tests done.')
    
# Parent: Employee   
# class Developer(Employee):
#     def __init__(self,name,salary,framework):
#         super().__init__(name,salary)
#         self.framework = framework
    
#     def increase_salary(self, percent, bonus=0):
#         super().increase_salary(percent)
#         self.salary += bonus

# For multiple inherit, anyone can use this. Not class specific
class SlotsInspectorMixin:
    # Need this to ensure children do not have empty dict if they use slots
    __slots__ = ()
    def has_slots(self):
        print("In slots")
        return hasattr(self,"__slots__")

# Optimal using Slots
class Developer(Employee, SlotsInspectorMixin):
    # Value needs to be iterable with all instance attributes. Using tuple, could be list
    __slots__ = ("framework")
    def __init__(self,framework):
        self.framework = framework