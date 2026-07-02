# =====================================
# LAB 2: ATM WITHDRAWAL VALIDATOR
# =====================================
DAILY_LIMIT = 70000

print("======= ATM WITHDRAWAL VALIDATOR =======")

balance = float(input("Enter current balance: KES "))
withdrawal = float(input("Enter withdrawal amount: KES "))

print(f"\nBalance        : KES {balance:,.2f}")
print(f"Withdrawal      : KES {withdrawal:,.2f}")
print("-" * 40)

if withdrawal <= 0:
    print("Declined: Withdrawal amount must be greater than 0.")
elif withdrawal > balance:
    print("Declined: Withdrawal amount exceeds available balance.")
elif withdrawal > DAILY_LIMIT:
    print(f"Declined: Withdrawal amount exceeds daily limit of KES {DAILY_LIMIT:,.2f}.")
else:
    new_balance = balance - withdrawal
    print("Approved: Withdrawal successful.")
    print(f"New Balance     : KES {new_balance:,.2f}")
