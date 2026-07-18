# 4. Class definition syntax
class Student:                              # Class name: CapitalCase
    """Represents a student at FAC Academy."""

    # Class attribute - shared by ALL instances
    institution = "FAC Academy"
    student_count = 0

    # __init__ constructor - runs when object is created
    def __init__(self, name, reg_no: str, marks: float):
        # Instance attributes - unique to each object
        self.name = name.title()
        self.reg_no = reg_no.upper()
        self.marks = marks
        self.grade = self._calc_grade()      # Call method on init
        Student.student_count += 1           # Update class variable

    # Instance method - operates on this specific object
    def display(self):
        print(f'Name: {self.name}')
        print(f'Reg No: {self.reg_no}')
        print(f'Marks: {self.marks}%')
        print(f'Grade: {self.grade}')

    # Private method - convention: starts with _
    def _calc_grade(self):
        if self.marks >= 70: return 'A'
        elif self.marks >= 60: return 'B'
        elif self.marks >= 50: return 'C'
        else: return 'Fail'

    # Class method - operates on the class, not instance
    @classmethod
    def get_count(cls) -> int:
        return cls.student_count

    # String representation - for print() and str()
    def __str__(self) -> str:
        return f'Student({self.name}, {self.reg_no}, Grade {self.grade})'


# =====================================
# DEMO - runs only when this file is executed directly
# =====================================
if __name__ == "__main__":
    brian = Student('brian', 'reg001', 85.0)
    mary = Student('mary', 'reg002', 45.0)

    brian.display()
    print()
    print(brian)      # Uses __str__
    print(mary)

    print(f"\nTotal students created: {Student.get_count()}")