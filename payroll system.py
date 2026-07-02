# =====================================
# COMPLETE REUSABLE PAYROLL SYSTEM
# FAC Academy W2S3 - Assignment
# =====================================

# --- Constants ---
NHIF_RATE  = 0.015   # 1.5%
NSSF_RATE  = 0.060   # 6%
PAYE_RATE  = 0.100   # 10% simplified
HOUSING    = 0.150   # 15% housing allowance
TRANSPORT  = 5000    # flat transport allowance (KES)


# --- Function 1: Calculate Gross Pay ---
def calculate_gross(basic):
    housing_allowance = basic * HOUSING
    gross = basic + housing_allowance + TRANSPORT
    return gross


# --- Function 2: Calculate Deductions ---
def calculate_deductions(basic):
    nhif = basic * NHIF_RATE
    nssf = basic * NSSF_RATE
    paye = basic * PAYE_RATE
    total_deductions = nhif + nssf + paye
    return nhif, nssf, paye, total_deductions


# --- Function 3: Calculate Net Pay ---
def calculate_net(gross, total_deductions):
    net = gross - total_deductions
    return net


# --- Function 4: Print Payslip ---
def print_payslip(name, employee_id, basic):
    gross              = calculate_gross(basic)
    nhif, nssf, paye, total_ded = calculate_deductions(basic)
    net                = calculate_net(gross, total_ded)

    print("=" * 42)
    print("         SOLUTIONS LTD - PAYSLIP")
    print("=" * 42)
    print(f"  Name         : {name}")
    print(f"  Staff No     : {employee_id}")
    print("-" * 42)
    print(f"  Basic Salary : KES {basic:>10,.2f}")
    print(f"  Housing (15%): KES {basic * HOUSING:>10,.2f}")
    print(f"  Transport    : KES {TRANSPORT:>10,.2f}")
    print(f"  Gross Pay    : KES {gross:>10,.2f}")
    print("-" * 42)
    print(f"  NHIF  (1.5%) : KES {nhif:>10,.2f}")
    print(f"  NSSF  (6.0%) : KES {nssf:>10,.2f}")
    print(f"  PAYE  (10%)  : KES {paye:>10,.2f}")
    print(f"  Total Deduct.: KES {total_ded:>10,.2f}")
    print("=" * 42)
    print(f"  NET PAY      : KES {net:>10,.2f}")
    print("=" * 42)
    print()


# --- Employee Data ---
employees = [
    {"name": "Brian Ochieng",  "id": "EMP001", "basic": 50000},
    {"name": "Amina Wanjiru",  "id": "EMP002", "basic": 75000},
    {"name": "John Mutua",     "id": "EMP003", "basic": 32000},
    {"name": "Grace Akinyi",   "id": "EMP004", "basic": 60000},
    {"name": "Peter Kamau",    "id": "EMP005", "basic": 45000},
]

# --- Process All Employees Using a Loop ---
print("\n===== SOLUTIONS LTD - MONTHLY PAYROLL =====\n")

total_gross_payroll = 0
total_net_payroll   = 0

for emp in employees:
    print_payslip(emp["name"], emp["id"], emp["basic"])

    gross = calculate_gross(emp["basic"])
    _, _, _, total_ded = calculate_deductions(emp["basic"])
    net = calculate_net(gross, total_ded)

    total_gross_payroll += gross
    total_net_payroll   += net

# --- Company Payroll Summary ---
print("=" * 42)
print("         COMPANY PAYROLL SUMMARY")
print("=" * 42)
print(f"  Total Employees : {len(employees)}")
print(f"  Total Gross     : KES {total_gross_payroll:>10,.2f}")
print(f"  Total Net       : KES {total_net_payroll:>10,.2f}")
print("=" * 42)