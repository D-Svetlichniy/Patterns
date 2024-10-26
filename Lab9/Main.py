from Lab9.Company import Company
from Lab9.Department import Department
from Lab9.Employee import Employee
from Lab9.SalaryReport import SalaryReport

if __name__ == "__main__":
    employee1 = Employee("Manager", 5000)
    employee2 = Employee("Engineer", 4000)
    department = Department([employee1, employee2])
    company = Company([department])

    report = SalaryReport()

    print("Salary report for the company:")
    company.accept(report)

    print("\nSalary report for the department:")
    department.accept(report)
