from company import Company
import employee
company = Company()
for i in range(3):
    company.add_employee(employee.Employee("K","G" + str(i)))
company.display_employees()