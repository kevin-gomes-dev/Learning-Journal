from employee import Employee,HourlyEmployee,SalaryEmployee,CommissionEmployee

class Company:
    def __init__(self):
        self.employees = []
        
    def add_employee(self, new_emp):
        self.employees.append(new_emp)
        print("Successfully added %s" % new_emp)
        
    def display_employees(self):
        print("Current Employees:")
        for i in self.employees:
            print(i.fname,i.lname)
        print('----------')
    
    def pay_employees(self):
        print("Paying Employees:")
        for i in self.employees:
            print(f'Paycheck for {i.fname} {i.lname}')
            print(f'Amount: ${i.calculate_paycheck():,.2f}')
            print('------------')