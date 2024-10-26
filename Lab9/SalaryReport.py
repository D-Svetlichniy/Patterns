from Lab9.Company import Company
from Lab9.Department import Department
from Lab9.Employee import Employee
from Lab9.Visitor import Visitor


class SalaryReport(Visitor):
    def __init__(self):
        self.total_salary = 0

    def visit_employee(self, employee: Employee):
        print(f"{employee.position}: {employee.salary}")
        self.total_salary += employee.salary

    def visit_department(self, department: Department):
        print("Total salary in department:", self.total_salary)

    def visit_company(self, company: Company):
        print("Total salary in company:", self.total_salary)
