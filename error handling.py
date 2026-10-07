new mini bank project 
class InsufficientBalanceError(Exception):
    """Raised when there is not enough balance."""
    pass


class InvalidAmountError(Exception):
    """Raised when amount is invalid."""
    pass


class BankAccount:
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.__balance = balance   # Encapsulation

    def deposit(self, amount):
        try:
            if amount <= 0:
                raise InvalidAmountError("Deposit amount must be greater than 0.")

            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
            print(f"Current balance: ₹{self.__balance}")

        except InvalidAmountError as e:
            print("Error:", e)

    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise InvalidAmountError(
                    "Withdrawal amount must be greater than 0."
                )

            if amount > self.__balance:
                raise InsufficientBalanceError(
                    "Insufficient balance."
                )

            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")
            print(f"Current balance: ₹{self.__balance}")

        except (InvalidAmountError, InsufficientBalanceError) as e:
            print("Error:", e)

    def check_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ₹{self.__balance}")


# Creating object
account = BankAccount("Kesava", "ACC1001", 5000)

account.check_balance()

print("\n--- Deposit ---")
account.deposit(2000)

print("\n--- Withdraw ---")
account.withdraw(1000)

print("\n--- Invalid Withdraw ---")
account.withdraw(10000)

print("\n--- Invalid Deposit ---")
account.deposit(-500)