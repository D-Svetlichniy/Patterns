from typing import List
from Lab9.Department import Department


class Company:
    def __init__(self, departments: List[Department]):
        self.departments = departments

    def accept(self, visitor):
        for department in self.departments:
            department.accept(visitor)
        visitor.visit_company(self)
