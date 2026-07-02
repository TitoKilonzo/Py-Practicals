# =====================================
# LAB 3: UNIVERSITY ADMISSION SYSTEM
# =====================================

# Grades ranked from highest to lowest
GRADE_RANK = {"A": 5, "B": 4, "C": 3, "D": 2, "E": 1}

# Minimum grade required for each course
COURSE_REQUIREMENTS = {
    "medicine": "A",
    "engineering": "B",
    "business": "C",
    "education": "D",
    "certificate course": "E",
}

print("======= UNIVERSITY ADMISSION SYSTEM =======")
print("Available courses:")
for course in COURSE_REQUIREMENTS:
    print(f"  - {course.title()}")

grade = input("\nEnter your KCSE grade (A, B, C, D, E): ").strip().upper()
course_choice = input("Enter your course choice: ").strip().lower()

print("\n========================")
print(f"  KCSE Grade   : {grade}")
print(f"  Course Choice: {course_choice.title()}")
print("========================")

if grade not in GRADE_RANK:
    print("Decision: Invalid grade entered. Must be one of A, B, C, D, E.")
elif course_choice not in COURSE_REQUIREMENTS:
    print("Decision: Course not found. Please choose from the list above.")
else:
    required_grade = COURSE_REQUIREMENTS[course_choice]
    if GRADE_RANK[grade] >= GRADE_RANK[required_grade]:
        print(f"Decision: ADMITTED to {course_choice.title()}.")
    else:
        print(f"Decision: NOT ADMITTED to {course_choice.title()}.")
        print(f"Minimum grade required: {required_grade}")
