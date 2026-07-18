# 100 separate variables, no organisation
name1 = 'Brian'; marks1 = 85; course1 = 'Python'
name2 = 'Mary'; marks2 = 92; course2 = 'Django'


def print_student(name, marks, course):
    print(f'{name}: {marks}% in {course}')


print_student(name1, marks1, course1)
print_student(name2, marks2, course2)

# As you add 50 more fields, this EXPLODES in complexity!
