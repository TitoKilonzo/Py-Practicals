# =====================================
# ATM PIN RETRY SYSTEM - FAC Academy W2S2
# =====================================
CORRECT_PIN = "1234"
MAX_ATTEMPTS = 3
attempts = 0
locked = False

print("======= ATM MACHINE =======")
print("Please enter your 4-digit PIN")

while attempts < MAX_ATTEMPTS:
    pin = input(f"\nPIN ({MAX_ATTEMPTS - attempts} attempt(s) left): ")

    if pin == CORRECT_PIN:
        print("\nPIN Accepted. Processing...")
        print("Current Balance: KES 45,280.00")
        print("\nSelect option:")
        print("1. Withdraw Cash")
        print("2. Check Balance")
        print("3. Mini Statement")
        break
    else:
        attempts += 1
        remaining = MAX_ATTEMPTS - attempts
        if remaining >= 0:
            print(f"Wrong PIN! {remaining} attempt(s) remaining.")
        else:
            locked = True
            print("\nCARD BLOCKED!")
