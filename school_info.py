"""
school_info.py
Person A (Driver) Task
School Info Display Script
"""

# Today's date (single-line comment)
# Date: 25 June 2026

# --------------------------------------------
# Multi-line comment (using triple quotes)
# This script displays:
# - School name and logo
# - Favourite 3 subjects
# - Teacher's name
# --------------------------------------------

# ASCII "logo" for the school
logo = """
   _   _____  ____    _    _   ____  _____ ___  ____
  | | | |  _ \\|  _ \\  / \\  | | / / | | __ \\|_ _|/ ___|
  | |_| | |_) | |_) |/ _ \\ | |/ /| | |_) || | \\___ \\
  |  _  |  _ <|  __//  ___ \\   < | |  __/ | |  ___) |
  |_| |_|_| \\_\\_|   /_/   \\_\\_|\\_\\|_|_|    |_| |____/
"""

school_name = "Kabarak University"  # Replace with your own school name

print(logo)
print(f"Welcome to {school_name}!")

# Favourite 3 subjects
subject_1 = "Computer Science"
subject_2 = "Mathematics"
subject_3 = "Web Development"

print("\nMy Favourite 3 Subjects:")
print(f"1. {subject_1}")
print(f"2. {subject_2}")
print(f"3. {subject_3}")

# Teacher's name
teacher_name = "Mr. John Doe"  # Replace with your actual teacher's name

print(f"\nMy Teacher: {teacher_name}")