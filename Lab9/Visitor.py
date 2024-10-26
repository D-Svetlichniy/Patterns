from abc import ABC, abstractmethod
from Lab9.Company import Company
from Lab9.Department import Department
from Lab9.Employee import Employee


class Visitor(ABC):
    @abstractmethod
    def visit_employee(self, employee: Employee):
        pass

    @abstractmethod
    def visit_department(self, department: Department):
        pass

    @abstractmethod
    def visit_company(self, company: Company):
        pass
