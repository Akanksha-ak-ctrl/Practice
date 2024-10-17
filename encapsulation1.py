class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number  # Protected attribute
        self._balance = balance  # Protected attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self._balance

# Creating an object of the BankAccount class
account = BankAccount("123456789", 1700)

# Depositing and withdrawing funds
account.deposit(900)
account.withdraw(200)

# Retrieving and displaying the balance (encapsulation)
print("Current Balance:", account.get_balance())

