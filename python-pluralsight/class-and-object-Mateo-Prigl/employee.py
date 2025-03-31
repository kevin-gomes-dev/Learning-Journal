class Employee():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def __str__(self):
        return f'{self.fname} {self.lname} |'
    
    def __repr__(self):
        return (
            f'Employee('
            f'{repr(self.fname)},'
            f'{repr(self.lname)})'
            )
        
    def __add__(self,*args):
        raise Exception (f'Cannot add employees together.')

class HourlyEmployee(Employee):
    def __init__(self, fname, lname, weekly_hours, hourly_rate):
        super().__init__(fname, lname)
        self.weekly_hours = weekly_hours
        self.hourly_rate = hourly_rate
        
    def calculate_paycheck(self):
        return self.weekly_hours * self.hourly_rate
    
    def __str__(self):
        return (super().__str__() + 
                f' Weekly Hours: {self.weekly_hours} Hourly Rate: {self.hourly_rate}'
        )

class SalaryEmployee(Employee):
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname)
        self.salary = salary
        self._monthly_salary = None
    
    # Use class decorater "property" so when accessing e.salary, calls this instead
    @property
    def salary(self):
        return self._salary
    
    # When doing something like e.salary = 3, call this instead with salary = 3.
    # Note that whenever salary is changed, update anything reliant on it.
    @salary.setter
    def salary(self,salary):
        if salary < 1000:
            raise ValueError(f'{salary} is less than minimum wage salary, $1,000')
        else:
            self._salary = salary
            self._monthly_salary = None # Removes cache, will be computed again
    
    # Computed property. Note it isn't cached, so every time it's rerquested, computes.
    # ^ Cached by adding _monthly_salary data member in init and the if condition here.
    @property
    def monthly_salary(self):
        if self._monthly_salary is None:
            self._monthly_salary = self.salary/12
        return self._monthly_salary
    
    def calculate_paycheck(self):
        return self.salary/52

    def increase_salary(self, percent):
        self.salary = self.salary + self.salary * (percent/100)
        
    def __str__(self):
        return super().__str__() + f' Salary: {self.salary}'

class CommissionEmployee(SalaryEmployee):
    def __init__(self, fname, lname, salary, sales_num, com_rate):
        super().__init__(fname, lname, salary)
        self.sales_num = sales_num
        self.com_rate = com_rate
    
    def calculate_paycheck(self):
        reg_sal = super().calculate_paycheck()
        total_commission = self.sales_num * self.com_rate
        return reg_sal + total_commission

    def __str__(self):
        return (super().__str__() +
                f' Number of Sales: {self.sales_num}' +
                f' Commission Rate: {self.com_rate}'
        )