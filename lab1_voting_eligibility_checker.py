# =====================================
# LAB 1: VOTING ELIGIBILITY CHECKER
# =====================================
from datetime import datetime

print("======= VOTING ELIGIBILITY CHECKER =======")

age = int(input("Enter your age: "))
id_number = input("Enter your ID number: ").strip()

# Check age >= 18 AND ID is 8 digits long
is_age_valid = age >= 18
is_id_valid = id_number.isdigit() and len(id_number) == 8

if is_age_valid and is_id_valid:
    print("\nStatus: ELIGIBLE to vote.")

    # Kenya holds general elections every 5 years, last held in 2022
    current_year = datetime.now().year
    next_election = 2022
    while next_election <= current_year:
        next_election += 5

    print(f"Next general election year: {next_election}")
else:
    print("\nStatus: INELIGIBLE to vote.")
    if not is_age_valid:
        print(f"Reason: Age must be 18 or older (you entered {age}).")
    if not is_id_valid:
        print("Reason: ID number must be exactly 8 digits.")
