try:
    # Code that MIGHT raise an exception
    age = int(input('Enter age: '))
    result = 100 / age

except ValueError:
    # Runs if ValueError occurs (e.g. user types 'abc')
    print('Invalid age - please enter a number!')

except ZeroDivisionError:
    # Runs if age is 0
    print('Age cannot be zero!')

except Exception as e:
    # Catches ANY other exception - always last
    print(f'Unexpected error: {e}')

else:
    # Runs ONLY if NO exception occurred
    print(f'Result: {result:.2f}')  # Safe to use result here

finally:
    # ALWAYS runs - exceptions or not
    print('Program continues safely.')

def calculate_grade(marks):
    if not isinstance(marks, (int, float)):
        raise TypeError(f'Marks must be numeric, got {type(marks).__name__}')
    if marks < 0 or marks > 100:
        raise ValueError(f'Marks must be 0-100, got {marks}')
    return 'A' if marks >= 70 else 'B' if marks >= 60 else 'C'


try:
    print(calculate_grade(65))  # Raises ValueError
except ValueError as e:
    print(f'Error: {e}')