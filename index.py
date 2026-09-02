class BankAccount:

    bank_name = "ABC Bank"

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")

        self._balance = amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self._balance:
            raise ValueError("Insufficient balance")

        self._balance -= amount

    @classmethod
    def from_string(cls, data):
        name, balance = data.split(",")
        return cls(name, float(balance))

    @staticmethod
    def validate_account_number(number):
        return len(number) == 10 and number.isdigit()


account = BankAccount("Rahul", 5000)

account.deposit(1000)
account.withdraw(500)

print(account.owner)
print(account.balance)

print(
    BankAccount.validate_account_number("1234567890")
)