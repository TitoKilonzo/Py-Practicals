class InsufficientFundsError(Exception):
    """Raised when withdrawal exceeds account balance."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f'Cannot withdraw KES {amount:,.2f} - balance: KES {balance:,.2f}')


class AccountLockedError(Exception):
    """Raised after too many failed PIN attempts."""
    pass


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount


try:
    new_balance = withdraw(8000, 6000)
except InsufficientFundsError as e:
    print(f'Transaction failed: {e}')