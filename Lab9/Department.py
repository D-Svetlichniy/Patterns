from typing import List
from Lab9.Employee import Employee


class Department:
    def __init__(self, employees: List[Employee]):
        self.employees = employees

    def accept(self, visitor):
        for employee in self.employees:
            employee.accept(visitor)
        visitor.visit_department(self)
