# ==== BANK ACCOUNT CLASS - FAC Academy W4S1 ====

class BankAccount:
    """Models a simple bank savings account."""

    INTEREST_RATE = 0.08  # 8% annual - class constant

    def __init__(self, acc_no: str, owner: str, balance: float = 0.0):
        self.acc_no = str(acc_no)
        self.owner = str(owner).strip().title()
        self._balance = float(balance)
        self._history = []

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += float(amount)
        self._history.append(
            f"Deposit KES {float(amount):10,.2f}  Balance: KES {self._balance:10,.2f}"
        )
        print(f"Deposited KES {amount:,.2f}. New balance: KES {self._balance:,.2f}")

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= float(amount)
        self._history.append(
            f"Withdraw KES {float(amount):10,.2f}  Balance: KES {self._balance:10,.2f}"
        )
        print(f"Withdrew KES {amount:,.2f}. New balance: KES {self._balance:,.2f}")

    def get_balance(self) -> float:
        return self._balance

    def mini_statement(self):
        print(f'{"=" * 15} {self.owner} {"=" * 15}')
        for entry in self._history[-5:]:
            print(f"  {entry}")
        print(f"  Current Balance: KES {self._balance:,.2f}")


def main():
    acc = BankAccount("KC8-001", "brian ochieng", 10000)
    acc.deposit(5000)
    acc.withdraw(2000)
    acc.mini_statement()


if __name__ == "__main__":
    main()