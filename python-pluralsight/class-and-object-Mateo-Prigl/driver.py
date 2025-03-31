from company import Company
from employee import *
company = Company()
# for i in range(3):
#     company.add_employee(Employee("K","G" + str(i)))
# company.display_employees()
# a = Employee("A","A2")
# b = Employee("B","B2")
# print(str(a))
# print(repr(a))
# c = eval(repr(a))
# print(b)
ea = Employee("Normal","Employee")
ha = HourlyEmployee("Hourly","Employee",20,15)
sa = SalaryEmployee("Salary","Emlpoyee",1500)
ca = CommissionEmployee("Commission","Employee",1000,4,5)
employees = [ea,ha,sa,ca]
for i in employees:
    company.add_employee(i)
company.display_employees()