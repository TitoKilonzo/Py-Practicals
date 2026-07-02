# =====================================
# STUDENT GRADING SYSTEM - FAC Academy W251
# =====================================

print("====== STUDENT GRADE CALCULATOR ======")

name = input("Student Name  : ").strip().title()
course = input("Course : ").strip().title()
marks = float(input("Marks (0-100)  : "))

# Validate marks
if marks < 0 or marks > 100:
    print("Invalid marks! Must be between 0-100.")
else:
    # Determine grade
    if marks >= 70:
        grade, remark = "A", "Distinction"
    elif marks >= 60:
        grade, remark = "B", "Merit"
    elif marks >= 50:
        grade, remark = "C", "Pass"
    elif marks >= 40:
        grade, remark = "D", "Supplementary"
    else:
        grade, remark = "E", "Fail"

    # Display results
    print("\n========================")
    print(f"  Student : {name}")
    print(f"  Course  : {course}")
    print(f"  Marks   : {marks:.1f}%")
    print(f"  Grade   : {grade}")
    print(f"  Remark  : {remark}")
    print("========================")
