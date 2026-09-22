class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return

        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            return

        if amount > self.balance:
            return

        self.balance -= amount


bank_account = BankAccount("Test_User", 1000)

visual_split = "----------------------------------"

print(visual_split)

print("User:", bank_account.owner)       # output: Test_User
print("Balance:", bank_account.balance)  # output: 1000

print(visual_split)

bank_account.deposit(100)
print("Balance after deposit(100):", bank_account.balance)   # output: 1100

bank_account.withdraw(200)
print("Balance after withdraw(200):", bank_account.balance)  # output: 900

print(visual_split)
