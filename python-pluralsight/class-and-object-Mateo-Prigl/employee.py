from dataclasses import dataclass
# Old way
# class Project:
#     def __init__(self,name,payment,client):
#         self.name = name
#         self.payment = payment
#         self.client = client
        
#     def __repr__(self):
#         return (f'Project('
#                 f'name={repr(self.name)},'
#                 f'payment={repr(self.payment)},'
#                 f'client={repr(self.client)})'
#             )

# New way, type hints but not enforced. Use mypy to check. Has default values
# We can make it quick with p = Project() and defaults will be used
# After 3.10, to use slots, just do slots=True. Before, have to define slots manually
@dataclass(slots=True)
class Project:
    name: str = "name"
    payment: int = "0"
    client: str = "client"
    
    # Can also do methods, etc cause it's still a class
    def notify_client(self):
        print(f'Notifying {self.client} of {self.name}')

class Employee:
    def __init__(self,name: str,age: int,salary: int,project: Project = Project()):
        self.name = name
        self.age = age
        self.salary = salary
        self.project = project # not a string
    