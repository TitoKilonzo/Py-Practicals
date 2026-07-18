class Student:
    def __init__(self, name, marks, course):
        self.name = name
        self.marks = marks
        self.course = course

    def display(self):
        print(f'{self.name}: {self.marks}% in {self.course}')


brian = Student('Brian', 85, 'Python')
brian.display()  # Clean, readable, scalable!
