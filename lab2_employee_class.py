# =====================================
# LAB 2: EMPLOYEE CLASS
# FAC Academy
# =====================================
# Author: Tito Kinyambu
# =====================================

class Employee:
    """Represents an employee at a company."""

    TAX_RATE = 0.10        # 10% tax - class constant
    total_employees = 0    # Class attribute - shared by ALL instances

    def __init__(self, emp_id: str, name: str, department: str, salary: float):
        self.emp_id = emp_id
        self.name = name.strip().title()
        self.department = department.strip().title()
        self.salary = salary
        Employee.total_employees += 1   # Update class variable

    # --- Instance method: display employee details ---
    def display(self):
        print(f'Employee ID : {self.emp_id}')
        print(f'Name        : {self.name}')
        print(f'Department  : {self.department}')
        print(f'Salary      : KES {self.salary:,.2f}')
        print(f'Net Pay     : KES {self.get_net_pay():,.2f}')

    # --- Instance method: calculate salary after tax ---
    def get_net_pay(self) -> float:
        return self.salary - (self.salary * self.TAX_RATE)

    # --- Instance method: increase salary ---
    def promote(self, amount: float):
        if amount <= 0:
            raise ValueError('Promotion amount must be positive')
        self.salary += amount
        print(f'{self.name} promoted! New salary: KES {self.salary:,.2f}')

    # --- Class method: operates on the class, not instance ---
    @classmethod
    def get_total_employees(cls) -> int:
        return cls.total_employees

    # --- String representation - for print() and str() ---
    def __str__(self) -> str:
        return f'Employee({self.emp_id}, {self.name})'


# =====================================
# DEMO - runs only when this file is executed directly
# =====================================
if __name__ == "__main__":
    emp1 = Employee('EMP001', 'brian ochieng', 'engineering', 80000)
    emp2 = Employee('EMP002', 'mary wanjiru', 'finance', 65000)

    emp1.display()
    print()
    emp2.display()

    print("\n--- Promotion ---")
    emp1.promote(10000)

    print("\n--- String Representation ---")
    print(emp1)
    print(emp2)

    print(f"\nTotal employees: {Employee.get_total_employees()}")
