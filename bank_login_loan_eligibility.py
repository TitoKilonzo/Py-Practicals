# ---- BANK LOGIN SYSTEM ----
username = input("Username: ")
password = input("Password: ")

if username == "admin":
    if password == "fac2025":
        print("Access Granted. Welcome, Admin!")
    else:
        print("Wrong password. Account may be locked.")
else:
    print("User not found in the system.")

# ---- LOAN ELIGIBILITY (two conditions required) ----
age = int(input("Age : "))
salary = float(input("Salary : KES "))

if age >= 21:
    if salary >= 30000:
        max_loan = salary * 3
        print(f"Loan Approved! Maximum: KES {max_loan:,.0f}")
    else:
        print("Salary below minimum (KES 30,000)")
else:
    print("Age below minimum requirement (21 years)")


# =====================================
# Logical AND Alternative
# =====================================

# Combine with 'and' - cleaner!
if age >= 21 and salary >= 30000:
    print("Loan Approved")
else:
    print("Not Eligible")

# Use 'or' for alternatives:
if age > 65 or salary < 5000:
    print("Apply for subsidy")

# Use 'not' to reverse:
if not username == "admin":
    print("Access denied")
