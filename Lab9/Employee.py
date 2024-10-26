class Employee:
    def __init__(self, position: str, salary: float):
        self.position = position
        self.salary = salary

    def accept(self, visitor):
        visitor.visit_employee(self)
