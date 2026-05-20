class employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
        def caculate_salary():
            pass
        def show_details():
            print(f"Name: {self.name}, Employee ID: {self.employee_id}")
class FullTimeEmployee(employee):
    def __init__(self, name, employee_id, salary):
        super().__init__(name, employee_id)
        self.salary = salary
    def caculate_salary(self):
        return self.salary
class PartTimeEmployee(employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    def caculate_salary(self):
        return self.hourly_rate * self.hours_worked
class contractor(employee):
    def __init__(self, name, employee_id, daily_rate, days_worked):
        super().__init__(name, employee_id)
        self.daily_rate = daily_rate
        self.days_worked = days_worked
    def caculate_salary(self):
        return self.daily_rate * self.days_worked
employee1 = FullTimeEmployee("Fareed", "E001", 50000)
employee2 = PartTimeEmployee("Ali", "E002", 20, 80)
employee3 = contractor("Ahmed", "E003", 100, 15)
print(f" Employee 1, {employee1.name} Salary: {employee1.caculate_salary()}")
print(f" Employee 2, {employee2.name} Salary: {employee2.caculate_salary()}")
print(f" Employee 3, {employee3.name} Salary: {employee3.caculate_salary()}")
