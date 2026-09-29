class BankAccount:
    """A simple bank account that protects its balance."""

    def __init__(self, owner, starting_balance=0):
        # A name beginning with two underscores is name-mangled by Python.
        # This discourages code outside the class from changing the balance
        # directly. Use the deposit and withdraw methods instead.
        self.owner = owner
        self.__balance = starting_balance

    def deposit(self, amount):
        """Add a positive amount of money to the account."""
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return

        self.__balance += amount
        print(f"Deposited ${amount:.2f}.")

    def withdraw(self, amount):
        """Take money out if the amount is valid and affordable."""
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.__balance:
            print("Not enough money in the account.")
        else:
            self.__balance -= amount
            print(f"Withdrew ${amount:.2f}.")

    def get_balance(self):
        """Return the current balance without allowing direct access to it."""
        return self.__balance

    def display_balance(self):
        """Show the account owner's current balance."""
        print(f"{self.owner}'s balance: ${self.get_balance():.2f}")


# A short example that runs when this file is started directly.
if __name__ == "__main__":
    account = BankAccount("Alex", 100)
    account.display_balance()
    account.deposit(50)
    account.withdraw(30)
    account.display_balance()
