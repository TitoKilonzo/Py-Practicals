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